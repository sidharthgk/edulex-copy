import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        teal: {
          100: '#b2d8d8', // Adjust this value to match the background in the image
        },
        brown: {
          500: '#8d6e63', // Adjust this value to match the submit button color
          600: '#795548',
        },
      },
    },
  },
  plugins: [],
}

export default config