/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        rasa: {
          bg: "#0c0a0a",
          panel: "#121010",
          border: "#1f1a1a",
          red: "#f42a41",
          text: "#d1caca",
          muted: "#665f5f"
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        mono: ['Space Mono', 'monospace'],
        serif: ['Playfair Display', 'serif']
      }
    },
  },
  plugins: [],
};
