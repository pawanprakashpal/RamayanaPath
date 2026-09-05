/**
 * The नवाह्न पारायण — the traditional nine-day division of the Ramcharitmanas,
 * recited over the nine nights of Navratri.
 *
 * Boundaries 1-8 are the printed विश्राम points, cross-checked against the verse
 * text in data/tulsidas: the closing line of each was located in our own data
 * before the doha number was recorded here. Day 8's start and day 9 follow by
 * contiguity —
 * day 7 closes at the end of Kishkindha and day 8 closes at the end of Lanka,
 * which leaves Sundar+Lanka for day 8 and Uttar Kand for day 9.
 *
 * Two boundaries fall *inside* a doha group rather than between two groups
 * (Bal Kand 120 and Aranya Kand 29 both carry क/ख sub-dohas in one group), so
 * those days are marked `sharesGroup` and the page says so rather than
 * pretending the split is clean.
 */

export interface ParayanDay {
  day: number;
  startKand: string;
  startDoha: number;
  endKand: string;
  endDoha: number;
  /** The विश्राम as traditionally printed, e.g. "बालकाण्ड 120(क)". */
  vishramHi: string;
  vishramEn: string;
  /** True when the traditional break falls within a doha group we render whole. */
  sharesGroup?: boolean;
  titleHi: string;
  titleEn: string;
  summaryHi: string;
  summaryEn: string;
}

export const PARAYAN_DAYS: ParayanDay[] = [
  {
    day: 1,
    startKand: "bal-kand",
    startDoha: 0,
    endKand: "bal-kand",
    endDoha: 120,
    vishramHi: "बालकाण्ड — मंगलाचरण से दोहा 120(क) तक",
    vishramEn: "Bal Kand — invocation to doha 120(a)",
    sharesGroup: true,
    titleHi: "मंगलाचरण और शिव-पार्वती प्रसंग",
    titleEn: "Invocation and the Shiva–Parvati narrative",
    summaryHi:
      "श्रीरामचरितमानस का मंगलाचरण, ग्रन्थ की महिमा, शिव-सती प्रसंग, सती का देहत्याग, पार्वती का जन्म एवं तप और शिव-पार्वती विवाह।",
    summaryEn:
      "The invocation, the greatness of the Manas, the Shiva–Sati narrative, Sati's renunciation of her body, Parvati's birth and penance, and the marriage of Shiva and Parvati.",
  },
  {
    day: 2,
    startKand: "bal-kand",
    startDoha: 120,
    endKand: "bal-kand",
    endDoha: 239,
    vishramHi: "बालकाण्ड — दोहा 120(ख) से दोहा 239 तक",
    vishramEn: "Bal Kand — doha 120(b) to doha 239",
    sharesGroup: true,
    titleHi: "श्रीराम जन्म और बाल्यकाल",
    titleEn: "The birth and childhood of Shri Ram",
    summaryHi:
      "श्रीराम एवं उनके भाइयों का जन्म, बाल-लीला, विश्वामित्र का यज्ञ-रक्षा हेतु ले जाना, ताड़का वध, अहल्या उद्धार और जनकपुर आगमन।",
    summaryEn:
      "The birth of Shri Ram and his brothers, their childhood, Vishwamitra taking them to guard his sacrifice, the slaying of Tadaka, the redemption of Ahalya, and the arrival at Janakpur.",
  },
  {
    day: 3,
    startKand: "bal-kand",
    startDoha: 240,
    endKand: "bal-kand",
    endDoha: 361,
    vishramHi: "बालकाण्ड — दोहा 240 से बालकाण्ड की पूर्णाहुति तक",
    vishramEn: "Bal Kand — doha 240 to the close of Bal Kand",
    titleHi: "धनुष भंग और श्रीराम-सीता विवाह",
    titleEn: "The breaking of the bow and the marriage of Ram and Sita",
    summaryHi:
      "सीता स्वयंवर में शिव धनुष का भंग, परशुराम-लक्ष्मण संवाद, श्रीराम-सीता विवाह और अयोध्या वापसी के साथ बालकाण्ड की पूर्णाहुति।",
    summaryEn:
      "The breaking of Shiva's bow at Sita's swayamvar, the exchange between Parashuram and Lakshman, the marriage of Ram and Sita, and the return to Ayodhya that closes Bal Kand.",
  },
  {
    day: 4,
    startKand: "ayodhya-kand",
    startDoha: 0,
    endKand: "ayodhya-kand",
    endDoha: 116,
    vishramHi: "अयोध्याकाण्ड — मंगलाचरण से दोहा 116 तक",
    vishramEn: "Ayodhya Kand — invocation to doha 116",
    titleHi: "कैकेयी के वरदान और वनवास",
    titleEn: "Kaikeyi's boons and the exile",
    summaryHi:
      "राज्याभिषेक की तैयारी, मंथरा का कुमंत्र, कैकेयी के दो वरदान, श्रीराम का सीता और लक्ष्मण सहित वन गमन तथा केवट प्रसंग।",
    summaryEn:
      "Preparations for the coronation, Manthara's counsel, Kaikeyi's two boons, Shri Ram's departure for the forest with Sita and Lakshman, and the episode of Kevat the boatman.",
  },
  {
    day: 5,
    startKand: "ayodhya-kand",
    startDoha: 117,
    endKand: "ayodhya-kand",
    endDoha: 236,
    vishramHi: "अयोध्याकाण्ड — दोहा 117 से दोहा 236 तक",
    vishramEn: "Ayodhya Kand — doha 117 to doha 236",
    titleHi: "दशरथ का देहावसान और भरत",
    titleEn: "Dasharath's passing and Bharat",
    summaryHi:
      "चित्रकूट में निवास, राजा दशरथ का शोक और देहावसान, भरत का लौटना और श्रीराम को मनाने के लिए चित्रकूट की ओर प्रस्थान।",
    summaryEn:
      "Life at Chitrakoot, King Dasharath's grief and death, Bharat's return, and his journey to Chitrakoot to plead with Shri Ram.",
  },
  {
    day: 6,
    startKand: "ayodhya-kand",
    startDoha: 237,
    endKand: "aranya-kand",
    endDoha: 29,
    vishramHi: "अयोध्याकाण्ड दोहा 237 से अरण्यकाण्ड दोहा 29(क) तक",
    vishramEn: "Ayodhya Kand doha 237 to Aranya Kand doha 29(a)",
    sharesGroup: true,
    titleHi: "भरत मिलाप और वन-प्रवेश",
    titleEn: "Bharat Milap and entering the forest",
    summaryHi:
      "भरत मिलाप, चरण-पादुका लेकर भरत की वापसी, नन्दिग्राम में तप, तथा अरण्यकाण्ड में ऋषि-मुनियों से भेंट।",
    summaryEn:
      "Bharat Milap, Bharat's return carrying Ram's sandals, his austerity at Nandigram, and in Aranya Kand the meetings with the forest sages.",
  },
  {
    day: 7,
    startKand: "aranya-kand",
    startDoha: 29,
    endKand: "kishkindha-kand",
    endDoha: 30,
    vishramHi: "अरण्यकाण्ड दोहा 29(ख) से किष्किन्धाकाण्ड की पूर्णाहुति तक",
    vishramEn: "Aranya Kand doha 29(b) to the close of Kishkindha Kand",
    sharesGroup: true,
    titleHi: "सीताहरण और हनुमान मिलन",
    titleEn: "The abduction of Sita and the meeting with Hanuman",
    summaryHi:
      "शूर्पणखा प्रसंग, मारीच का स्वर्ण मृग, रावण द्वारा सीताहरण, जटायु का बलिदान, शबरी पर कृपा, हनुमान एवं सुग्रीव से मिलन और बालि वध।",
    summaryEn:
      "The episode of Shurpanakha, Maricha's golden deer, Ravan's abduction of Sita, Jatayu's sacrifice, the grace shown to Shabari, the meeting with Hanuman and Sugriv, and the slaying of Bali.",
  },
  {
    day: 8,
    startKand: "sundar-kand",
    startDoha: 0,
    endKand: "lanka-kand",
    endDoha: 121,
    vishramHi: "सुन्दरकाण्ड के आरम्भ से लंकाकाण्ड दोहा 121(ख) तक",
    vishramEn: "The opening of Sundar Kand to Lanka Kand doha 121(b)",
    titleHi: "सुन्दरकाण्ड और लंका का युद्ध",
    titleEn: "Sundar Kand and the war at Lanka",
    summaryHi:
      "हनुमानजी का समुद्र लाँघना, अशोक वाटिका में सीता से भेंट, लंका दहन, रामसेतु निर्माण, लंका का महायुद्ध, रावण वध और अयोध्या वापसी।",
    summaryEn:
      "Hanuman's leap across the ocean, the meeting with Sita in the Ashok Vatika, the burning of Lanka, the building of the Ram Setu, the great war, the slaying of Ravan, and the return to Ayodhya.",
  },
  {
    day: 9,
    startKand: "uttar-kand",
    startDoha: 0,
    endKand: "uttar-kand",
    endDoha: 130,
    vishramHi: "उत्तरकाण्ड — आरम्भ से ग्रन्थ की पूर्णाहुति तक",
    vishramEn: "Uttar Kand — from its opening to the close of the work",
    titleHi: "राज्याभिषेक और रामराज्य",
    titleEn: "The coronation and Ram Rajya",
    summaryHi:
      "श्रीराम का राज्याभिषेक, रामराज्य की स्थापना, काकभुशुण्डि एवं गरुड़ का संवाद और ग्रन्थ की पूर्णाहुति।",
    summaryEn:
      "Shri Ram's coronation, the establishment of Ram Rajya, the dialogue of Kakbhushundi and Garud, and the completion of the work.",
  },
];

const KAND_ORDER = [
  "bal-kand",
  "ayodhya-kand",
  "aranya-kand",
  "kishkindha-kand",
  "sundar-kand",
  "lanka-kand",
  "uttar-kand",
];

export interface DaySegment {
  kand: string;
  from: number;
  to: number;
}

/**
 * Expands a day into per-Kand spans, so a day crossing a Kand boundary links
 * into each Kand's paath page separately.
 */
export function daySegments(day: ParayanDay, lastDoha: Record<string, number>): DaySegment[] {
  const startIndex = KAND_ORDER.indexOf(day.startKand);
  const endIndex = KAND_ORDER.indexOf(day.endKand);
  if (startIndex < 0 || endIndex < 0) return [];

  const segments: DaySegment[] = [];
  for (let i = startIndex; i <= endIndex; i++) {
    const kand = KAND_ORDER[i];
    segments.push({
      kand,
      from: i === startIndex ? day.startDoha : 0,
      to: i === endIndex ? day.endDoha : (lastDoha[kand] ?? day.endDoha),
    });
  }
  return segments;
}
