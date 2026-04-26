# Prompt for Frontend UI Generation (Google Stitch / AI Assistants)

**System Prompt / Context to provide to the AI:**

```text
You are an expert Frontend Developer and UI/UX Designer. We are building the frontend for a premium, AI-powered Zomato Restaurant Recommendation System. The backend is a FastAPI application that returns tailored restaurant recommendations with AI-generated explanations based on user preferences.

Your task is to design and implement the "Frontend Experience Layer" (Phase 6) using Next.js (App Router), React, and Tailwind CSS. The design must be highly aesthetic, modern, and engaging.

### 1. Requirements & Tech Stack
- **Framework:** Next.js (App Router preferred) with React.
- **Styling:** Tailwind CSS. Use a cohesive color palette (e.g., Zomato's signature crimson red combined with modern dark mode or clean off-white backgrounds).
- **Icons:** Lucide-React or Heroicons.
- **Animations:** Framer Motion for smooth transitions, hover effects, and list stagger animations.

### 2. Pages and Layouts to Generate

**A. Landing / Input Form Page:**
- A hero section with a captivating headline (e.g., "Find Your Next Great Meal, Curated by AI").
- A premium, card-based form where users can input their preferences:
  - **Location:** (Text Input)
  - **Budget:** (Dropdown or Toggle: Low, Medium, High)
  - **Cuisines:** (Multi-select or Tags)
  - **Minimum Rating:** (Slider from 0 to 5)
  - **Additional Preferences:** (Optional text area, e.g., "Good ambiance, outdoor seating")
- A prominent, stylish "Get Recommendations" button with a loading/spinning state for when the API is being called.

**B. Recommendations Results View:**
- A skeleton loading state while waiting for the LLM to process.
- **Query Summary Section:** A beautifully formatted quote block at the top displaying the `query_summary` returned by the backend.
- **Restaurant Cards Grid/List:** A layout displaying the top-N restaurants. Each card must include:
  - A prominent "Rank" badge (e.g., #1, #2).
  - Restaurant Name, Location, Cuisine, and Rating (with a star icon).
  - Estimated Cost.
  - A section for the AI's "Explanation" (the rationale behind why it was picked).
  - Match Tags styled as aesthetic pill badges.
- **History/Saved Section (Optional Sidebar/Drawer):** To show past requests (from the `/api/history` endpoint).

### 3. API Contract Reference
The Next.js app will make a POST request to `/api/recommend` with this JSON body:
{
  "location": "Bellandur",
  "budget": "high",
  "cuisines": ["Italian", "Continental"],
  "min_rating": 4.0,
  "additional_preferences": ["Rooftop"]
}

And expect this JSON response:
{
  "query_summary": "Here are 5 highly-rated Italian and Continental places in Bellandur with a high budget.",
  "recommendations": [
    {
      "rank": 1,
      "restaurant_name": "Mocha",
      "location": "Bellandur, Bangalore",
      "cuisine": "Continental, Italian",
      "rating": 4.1,
      "estimated_cost": "1500",
      "explanation": "Perfect for your rooftop dining requirement with an excellent continental menu.",
      "match_tags": ["high_budget", "rooftop"]
    }
  ],
  "history_id": 12
}

### 4. Design Guidelines
- Prioritize visual excellence. Avoid generic or flat designs. Implement subtle glassmorphism, soft shadows, and clean typography (e.g., Inter or Outfit fonts).
- Ensure the interface feels alive with micro-interactions (e.g., cards lifting on hover).
- Fully responsive on mobile, tablet, and desktop.

Please generate the Next.js page components, UI components, and the necessary Tailwind configuration to bring this vision to life.
```
