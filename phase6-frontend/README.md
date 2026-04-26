# Phase 6: Frontend Experience Layer

This directory contains the source code for the Next.js frontend, styled strictly according to the provided UI mockups.

## Setup & Running

*Note: You will need Node.js and npm installed on your system to run this.*

1. Navigate to this directory:
   ```bash
   cd phase6-frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```
   *(This will install Next.js, React, TailwindCSS, and Lucide React icons).*

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Features Implemented
- **Landing Form:** A beautiful, glassmorphism-styled form matching the "Find Your Next Great Meal" mockup with functional UI components for budget toggles, rating sliders, and cuisine pills.
- **Loading State:** Displays the skeleton loaders and the "Curating your experience" text while simulating an API call.
- **Results View:** Renders the Epicurean AI recommendation cards identically to the provided design, including the ranking badge, tags over the image, star ratings, and the "AI Insight" breakdown box.
