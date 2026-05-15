import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        cream: "#F8F6F1",
        ink: "#0E1B2E",
        charcoal: "#28323F",
        mutedBlue: "#48627E",
        mutedGold: "#A58D5F",
        line: "#E3DED2",
      },
      boxShadow: {
        panel: "0 10px 30px rgba(14, 27, 46, 0.06)",
      },
      fontFamily: {
        display: ["Georgia", "Times New Roman", "serif"],
        sans: ["ui-sans-serif", "system-ui", "sans-serif"],
      },
      backgroundImage: {
        "quiet-grid": "linear-gradient(to right, rgba(72,98,126,0.08) 1px, transparent 1px), linear-gradient(to bottom, rgba(72,98,126,0.08) 1px, transparent 1px)",
      },
      backgroundSize: {
        grid: "36px 36px",
      },
    },
  },
  plugins: [],
};

export default config;
