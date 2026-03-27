interface RamIconProps {
  className?: string;
}

export default function RamIcon({ className = "" }: RamIconProps) {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 120 160"
      fill="currentColor"
      className={className}
      aria-label="Shree Ram with bow and arrow"
      role="img"
    >
      {/* Head */}
      <circle cx="62" cy="18" r="10" />
      {/* Crown/Mukut */}
      <path d="M54 10 L58 2 L62 6 L66 1 L70 10 Z" />
      <path d="M56 10 L62 3 L68 10" />
      {/* Crown jewel */}
      <circle cx="62" cy="5" r="2" />
      {/* Neck */}
      <rect x="58" y="27" width="8" height="5" rx="2" />
      {/* Torso */}
      <path d="M48 32 L76 32 L78 70 L62 76 L46 70 Z" />
      {/* Necklace */}
      <ellipse cx="62" cy="40" rx="12" ry="4" fill="none" stroke="currentColor" strokeWidth="1.5" />
      {/* Left arm - holding bow */}
      <path d="M48 34 L28 56 L30 58 L48 40" />
      {/* Right arm - drawing string */}
      <path d="M76 34 L92 46 L90 48 L76 40" />
      {/* Bow */}
      <path d="M18 36 Q10 56 22 76" stroke="currentColor" strokeWidth="3.5" fill="none" strokeLinecap="round" />
      {/* Bowstring */}
      <line x1="18" y1="36" x2="22" y2="76" stroke="currentColor" strokeWidth="1.5" />
      {/* Arrow */}
      <line x1="22" y1="56" x2="100" y2="40" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" />
      {/* Arrowhead */}
      <path d="M100 40 L94 35 L102 38 Z" />
      <path d="M100 40 L94 45 L102 42 Z" />
      {/* Arrow feathers */}
      <path d="M24 55 L20 50 L26 54" />
      <path d="M24 57 L20 62 L26 58" />
      {/* Dhoti/lower garment */}
      <path d="M46 70 L62 76 L78 70 L80 72 L68 90 L62 100 L56 90 L44 72 Z" />
      {/* Flowing cloth/uttariya */}
      <path d="M46 36 L32 44 L28 68 L34 72 L40 52 L48 40" opacity="0.8" />
      {/* Left leg */}
      <path d="M52 90 L48 130 L54 130 L56 94" />
      {/* Right leg */}
      <path d="M68 90 L72 130 L66 130 L64 94" />
      {/* Left foot */}
      <ellipse cx="50" cy="132" rx="6" ry="3" />
      {/* Right foot */}
      <ellipse cx="70" cy="132" rx="6" ry="3" />
      {/* Quiver on back */}
      <rect x="70" y="28" width="6" height="30" rx="2" opacity="0.7" />
      {/* Arrow tips in quiver */}
      <path d="M71 28 L73 22 L75 28" opacity="0.7" />
      <path d="M72 28 L74 24 L76 28" opacity="0.7" />
    </svg>
  );
}
