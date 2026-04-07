"use client";

import { createContext, useCallback, useContext, useEffect, useRef, useState } from "react";

export type TtsLang = "original" | "hindi" | "english";

interface TtsState {
  supported: boolean;
  speaking: boolean;
  currentVerseId: string | null;
  lang: TtsLang;
  setLang: (lang: TtsLang) => void;
  speakVerse: (id: string, text: string) => void;
  playAll: (verses: { id: string; original: string; hindiTranslation?: string; translation: string }[]) => void;
  stop: () => void;
}

const TtsContext = createContext<TtsState>({
  supported: false,
  speaking: false,
  currentVerseId: null,
  lang: "original",
  setLang: () => {},
  speakVerse: () => {},
  playAll: () => {},
  stop: () => {},
});

export function useTts() {
  return useContext(TtsContext);
}

function cleanText(text: string): string {
  return text
    .replace(/।।\d+.*?।।/g, "")
    .replace(/॥\d+॥/g, "")
    .replace(/\n/g, " । ")
    .trim();
}

// --- Browser TTS fallback ---
function browserSpeak(
  text: string,
  lang: TtsLang,
  onEnd: () => void,
  onError: () => void
): { cancel: () => void } {
  const synth = window.speechSynthesis;
  const langCode = lang === "english" ? "en-US" : "hi-IN";
  const clean = lang === "english" ? text : cleanText(text);

  const utt = new SpeechSynthesisUtterance(clean);
  utt.lang = langCode;
  utt.rate = lang === "english" ? 0.9 : 0.85;
  const voices = synth.getVoices();
  const voice = voices.find((v) => v.lang.startsWith(langCode.split("-")[0]));
  if (voice) utt.voice = voice;
  utt.onend = onEnd;
  utt.onerror = onError;

  synth.cancel();
  synth.speak(utt);

  return { cancel: () => synth.cancel() };
}

// --- Azure TTS (returns audio blob URL, falls back on failure) ---
async function azureSpeak(
  text: string,
  lang: TtsLang
): Promise<string | null> {
  try {
    const clean = lang === "english" ? text : cleanText(text);
    const res = await fetch("/api/tts", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: clean, lang }),
    });
    if (!res.ok) return null;
    const blob = await res.blob();
    return URL.createObjectURL(blob);
  } catch {
    return null;
  }
}

export default function TtsProvider({ children }: { children: React.ReactNode }) {
  const [supported, setSupported] = useState(false);
  const [speaking, setSpeaking] = useState(false);
  const [currentVerseId, setCurrentVerseId] = useState<string | null>(null);
  const [lang, setLang] = useState<TtsLang>("original");
  const queueRef = useRef<{ id: string; text: string }[]>([]);
  const playingAllRef = useRef(false);
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const cancelBrowserRef = useRef<(() => void) | null>(null);

  useEffect(() => {
    setSupported(true); // Azure works everywhere; browser TTS is bonus
    if (typeof window !== "undefined" && "speechSynthesis" in window) {
      speechSynthesis.getVoices();
      speechSynthesis.onvoiceschanged = () => speechSynthesis.getVoices();
    }
  }, []);

  const stop = useCallback(() => {
    if (audioRef.current) {
      audioRef.current.pause();
      audioRef.current.src = "";
      audioRef.current = null;
    }
    if (cancelBrowserRef.current) {
      cancelBrowserRef.current();
      cancelBrowserRef.current = null;
    }
    if (typeof window !== "undefined" && "speechSynthesis" in window) {
      speechSynthesis.cancel();
    }
    setSpeaking(false);
    setCurrentVerseId(null);
    queueRef.current = [];
    playingAllRef.current = false;
  }, []);

  const speakText = useCallback(
    async (id: string, text: string, onEnd?: () => void) => {
      setCurrentVerseId(id);
      setSpeaking(true);

      const handleEnd = () => {
        if (onEnd) {
          onEnd();
        } else {
          setSpeaking(false);
          setCurrentVerseId(null);
        }
      };

      const handleError = () => {
        setSpeaking(false);
        setCurrentVerseId(null);
        queueRef.current = [];
        playingAllRef.current = false;
      };

      // Try Azure first
      const audioUrl = await azureSpeak(text, lang);
      if (audioUrl) {
        const audio = new Audio(audioUrl);
        audioRef.current = audio;
        audio.onended = () => {
          URL.revokeObjectURL(audioUrl);
          audioRef.current = null;
          handleEnd();
        };
        audio.onerror = () => {
          URL.revokeObjectURL(audioUrl);
          audioRef.current = null;
          // Fallback to browser TTS
          if ("speechSynthesis" in window) {
            cancelBrowserRef.current = browserSpeak(text, lang, handleEnd, handleError).cancel;
          } else {
            handleError();
          }
        };
        audio.play().catch(() => {
          // Autoplay blocked — fallback to browser
          URL.revokeObjectURL(audioUrl);
          if ("speechSynthesis" in window) {
            cancelBrowserRef.current = browserSpeak(text, lang, handleEnd, handleError).cancel;
          } else {
            handleError();
          }
        });
        return;
      }

      // Azure unavailable — use browser TTS
      if ("speechSynthesis" in window) {
        cancelBrowserRef.current = browserSpeak(text, lang, handleEnd, handleError).cancel;
      } else {
        handleError();
      }
    },
    [lang]
  );

  const playNext = useCallback(() => {
    const next = queueRef.current.shift();
    if (!next) {
      setSpeaking(false);
      setCurrentVerseId(null);
      playingAllRef.current = false;
      return;
    }
    speakText(next.id, next.text, () => {
      if (playingAllRef.current) playNext();
    });
  }, [speakText]);

  const speakVerse = useCallback(
    (id: string, text: string) => {
      if (speaking && currentVerseId === id) {
        stop();
        return;
      }
      stop();
      speakText(id, text);
    },
    [speaking, currentVerseId, stop, speakText]
  );

  const playAll = useCallback(
    (verses: { id: string; original: string; hindiTranslation?: string; translation: string }[]) => {
      if (playingAllRef.current) {
        stop();
        return;
      }
      queueRef.current = verses.map((v) => ({
        id: v.id,
        text: lang === "english" ? v.translation : lang === "hindi" ? (v.hindiTranslation || v.original) : v.original,
      }));
      playingAllRef.current = true;
      playNext();
    },
    [lang, stop, playNext]
  );

  return (
    <TtsContext.Provider value={{ supported, speaking, currentVerseId, lang, setLang, speakVerse, playAll, stop }}>
      {children}
    </TtsContext.Provider>
  );
}
