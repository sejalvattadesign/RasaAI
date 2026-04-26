"use client";
import React, { useState, useRef, useEffect } from 'react';
import { Search, Activity, History, ChevronDown, Zap, Star, MapPin } from 'lucide-react';

export default function RasaApp() {
  const [view, setView] = useState<'home' | 'calibrate' | 'loading' | 'results'>('home');
  // Form State
  const [location, setLocation] = useState("Select Location");
  const [isLocationOpen, setIsLocationOpen] = useState(false);
  const locationOptions = ["BTM", "Banashankari", "Banaswadi", "Bannerghatta Road", "Basavanagudi", "Bellandur", "Brigade Road", "Brookefield", "CV Raman Nagar", "Commercial Street", "Domlur", "Electronic City", "Frazer Town", "HSR", "Indiranagar", "JP Nagar", "Jayanagar", "Kalyan Nagar", "Kammanahalli", "Koramangala", "Lavelle Road", "MG Road", "Malleshwaram", "Marathahalli", "New BEL Road", "Old Airport Road", "Rajajinagar", "Residency Road", "Richmond Road", "Sarjapur Road", "Shanti Nagar", "Shivajinagar", "St. Marks Road", "Ulsoor", "Vasanth Nagar", "Whitefield"];
  
  const [budgetTier, setBudgetTier] = useState<number | null>(null); // 0=low, 1=medium, 2=high
  const [rating, setRating] = useState(0);
  const [selectedCuisines, setSelectedCuisines] = useState<string[]>([]);
  const [additionalParams, setAdditionalParams] = useState("");
  
  // API State
  const [apiResults, setApiResults] = useState<any>(null);

  const budgetMap = ["low", "medium", "high", "high"];

  // Use environment variable for API URL in production
  const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

  const handleExecuteScan = async () => {
    if (location === "Select Location") {
      return; // Or show a toast/tooltip
    }

    setView('loading');
    try {
      const response = await fetch(`${API_BASE_URL}/api/recommend`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          location: location,
          budget: budgetTier !== null ? budgetMap[budgetTier] : "medium",
          cuisines: selectedCuisines.length > 0 ? selectedCuisines : ["Any"],
          min_rating: rating,
          additional_preferences: additionalParams ? [additionalParams] : []
        })
      });
      const data = await response.json();
      setApiResults(data);
      setView('results');
    } catch (error) {
      console.error("Failed to fetch recommendations:", error);
      // Fallback in case backend is not running
      setApiResults({
        query_summary: "Error connecting to backend.",
        recommendations: []
      });
      setView('results');
    }
  };

  const toggleCuisine = (cuisine: string) => {
    if (selectedCuisines.includes(cuisine)) {
      setSelectedCuisines(selectedCuisines.filter(c => c !== cuisine));
    } else {
      setSelectedCuisines([...selectedCuisines, cuisine]);
    }
  };

  const Header = () => (
    <header className="flex items-center justify-between border-b border-rasa-border px-8 py-4 bg-rasa-bg/90 backdrop-blur-sm sticky top-0 z-50">
      <div className="flex items-center gap-3">
        <div className="w-8 h-8 bg-rasa-red flex items-center justify-center rotate-45 rounded-sm">
          <div className="w-3 h-3 border-2 border-white -rotate-45" />
        </div>
        <span className="font-bold text-white text-xl tracking-wide cursor-pointer" onClick={() => setView('home')}>
          RASA<span className="text-rasa-red">.AI</span>
        </span>
      </div>
      
      <div className="flex items-center gap-3">
        <div className="w-10 h-10 border border-rasa-border flex items-center justify-center text-rasa-muted hover:text-rasa-red transition-colors cursor-pointer rounded-sm">
          <Activity size={18} />
        </div>
      </div>
    </header>
  );

  if (view === 'home') {
    return (
      <div className="min-h-screen flex flex-col">
        <Header />
        <main className="flex-1 flex flex-col justify-center px-8 md:px-24 py-12 max-w-7xl mx-auto w-full">
          <div className="max-w-3xl">
            <div className="inline-flex items-center gap-2 border border-rasa-border px-3 py-1 mb-8 text-[10px] font-mono text-rasa-red tracking-widest uppercase rounded-sm">
              <Zap size={10} />
              RASA.AI - The AI Concierge for Indian Diners
            </div>
            
            <h1 className="text-6xl md:text-8xl font-bold text-white leading-[1.1] mb-2 tracking-tight">
              Find your next<br/>great meal,<br/>
              <span className="font-serif italic text-rasa-red font-semibold">curated by AI.</span>
            </h1>
            
            <p className="text-lg text-rasa-muted mt-8 max-w-2xl leading-relaxed">
              Find your perfect dining spot with precision. Our AI analyzes 
              thousands of restaurants to match your unique taste — giving you 
              thoughtful recommendations with clear reasoning.
            </p>

            <div className="mt-12 flex items-center gap-6">
              <button 
                onClick={() => setView('calibrate')}
                className="bg-rasa-red hover:bg-[#ff3b53] text-white font-bold px-8 py-4 flex items-center gap-3 transition-colors rounded-sm uppercase tracking-wider text-sm shadow-[0_0_20px_rgba(244,42,65,0.3)]"
              >
                Get Started <ChevronDown size={18} />
              </button>
              <div className="flex items-center gap-4 text-[10px] font-mono text-rasa-muted uppercase tracking-widest">
                <span>Personalized for you</span>
                <span>Instant curation</span>
              </div>
            </div>
          </div>
        </main>
      </div>
    );
  }

  if (view === 'calibrate') {
    const cuisineOptions = ['North Indian', 'South Indian', 'Chinese', 'Continental', 'Italian', 'Cafe', 'Biryani', 'Desserts', 'Street Food', 'Fast Food', 'Mughlai', 'Asian'];
    
    return (
      <div className="min-h-screen flex flex-col">
        <Header />
        <main className="flex-1 px-8 md:px-24 py-12 max-w-7xl mx-auto w-full grid grid-cols-1 lg:grid-cols-12 gap-16">
          
          <div className="lg:col-span-4">
            <div className="text-[10px] font-mono text-rasa-red uppercase tracking-widest mb-4">Step 01 / Your Preferences</div>
            <h2 className="text-4xl font-bold text-white mb-6 leading-tight">What are you in the mood for?</h2>
            <p className="text-rasa-muted text-sm leading-relaxed mb-12">
              Share your preferences to help our AI narrow down the best choices. The more details you provide, the better we can match you with the perfect dining experience.
            </p>
            

          </div>

          <div className="lg:col-span-8 border border-rasa-border bg-rasa-panel p-8 md:p-12 relative rounded-sm">
            <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-rasa-red to-transparent opacity-50" />
            
            <div className="flex justify-between items-center border-b border-rasa-border pb-6 mb-8 text-[10px] font-mono uppercase tracking-widest">
              <div className="flex items-center gap-2 text-rasa-muted">
                <div className="w-1.5 h-1.5 rounded-full bg-rasa-red animate-pulse" />
                Personalizing your search
              </div>
              <div className="text-rasa-muted">Privacy Protected</div>
            </div>

            {/* Your Location */}
            <div className="mb-10 relative">
              <label className="text-[10px] font-mono text-rasa-muted uppercase tracking-widest mb-4 block">Your Location</label>
              <div 
                className="relative cursor-pointer"
                onClick={() => setIsLocationOpen(!isLocationOpen)}
              >
                <MapPin className="absolute left-4 top-4 text-rasa-muted" size={16} />
                <div className={`w-full bg-[#0a0808] border ${isLocationOpen ? 'border-rasa-red' : 'border-rasa-border'} p-4 pl-12 text-sm outline-none transition-colors rounded-sm font-mono flex justify-between items-center ${location === 'Select Location' ? 'text-rasa-muted' : 'text-white'}`}>
                  <span>{location}</span>
                  <ChevronDown size={16} className={`text-rasa-muted transition-transform ${isLocationOpen ? 'rotate-180' : ''}`} />
                </div>
                <div className="absolute right-12 top-4 w-1.5 h-1.5 rounded-full bg-rasa-red" />
              </div>

              {isLocationOpen && (
                <div className="absolute top-full left-0 w-full mt-2 bg-[#0a0808] border border-rasa-border rounded-sm max-h-60 overflow-y-auto z-10 shadow-[0_10_40px_rgba(0,0,0,0.5)] scrollbar-thin scrollbar-thumb-rasa-border scrollbar-track-transparent">
                  {locationOptions.map(opt => (
                    <div 
                      key={opt}
                      onClick={() => { setLocation(opt); setIsLocationOpen(false); }}
                      className={`p-4 text-sm font-mono cursor-pointer transition-colors ${location === opt ? 'bg-rasa-red/10 text-rasa-red border-l-2 border-rasa-red' : 'text-rasa-muted hover:bg-rasa-border/20 hover:text-white border-l-2 border-transparent'}`}
                    >
                      {opt}
                    </div>
                  ))}
                </div>
              )}
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-10 mb-10">
              {/* Price Complexity */}
              <div>
                <div className="flex justify-between items-end mb-4">
                  <label className="text-[10px] font-mono text-rasa-muted uppercase tracking-widest">Select Budget Range</label>
                  <span className="text-[10px] font-mono text-rasa-red uppercase tracking-widest">{budgetTier !== null ? `Tier 0${budgetTier + 1}` : 'Not Selected'}</span>
                </div>
                <div className="flex gap-2">
                  {['₹', '₹₹', '₹₹₹', '₹₹₹₹'].map((tier, i) => (
                    <button 
                      key={tier} 
                      onClick={() => setBudgetTier(i)}
                      className={`flex-1 py-3 text-sm font-mono border rounded-sm transition-colors ${budgetTier === i ? 'border-rasa-red text-rasa-red bg-rasa-red/5' : 'border-rasa-border text-rasa-muted hover:border-rasa-muted'}`}
                    >
                      {tier}
                    </button>
                  ))}
                </div>
              </div>

              {/* Min Rating Threshold */}
              <div>
                <div className="flex justify-between items-end mb-4">
                  <label className="text-[10px] font-mono text-rasa-muted uppercase tracking-widest">Minimum Rating</label>
                  <span className="text-[10px] font-mono text-rasa-red uppercase tracking-widest">{rating.toFixed(1)} / 5.0</span>
                </div>
                <div className="pt-2">
                  <input 
                    type="range" min="0" max="5" step="0.1" value={rating} onChange={(e) => setRating(parseFloat(e.target.value))}
                    className="w-full h-1 bg-rasa-border appearance-none cursor-pointer accent-rasa-red"
                  />
                  <div className="flex justify-between text-[10px] font-mono text-rasa-muted mt-2">
                    <span>0.0</span>
                    <span>2.5</span>
                    <span>5.0</span>
                  </div>
                </div>
              </div>
            </div>

            <div className="mb-10">
              <div className="flex justify-between items-end mb-4">
                <label className="text-[10px] font-mono text-rasa-muted uppercase tracking-widest">Preferred Cuisines · Multi-Select</label>
                <span className="text-[10px] font-mono text-rasa-muted uppercase tracking-widest">{selectedCuisines.length} Selected</span>
              </div>
              <div className="flex flex-wrap gap-2">
                {cuisineOptions.map((c) => {
                  const isSelected = selectedCuisines.includes(c);
                  return (
                    <button 
                      key={c}
                      onClick={() => toggleCuisine(c)}
                      className={`px-4 py-2 border text-[10px] font-mono uppercase tracking-widest rounded-sm transition-colors ${isSelected ? 'border-rasa-red text-rasa-red bg-rasa-red/5' : 'border-rasa-border text-rasa-muted hover:border-rasa-muted'}`}
                    >
                      {c}
                    </button>
                  );
                })}
              </div>
            </div>

            {/* Anything else? */}
            <div className="mb-10">
              <label className="text-[10px] font-mono text-rasa-muted uppercase tracking-widest mb-4 block">Anything else? · Optional</label>
              <textarea 
                value={additionalParams}
                onChange={(e) => setAdditionalParams(e.target.value)}
                className="w-full bg-[#0a0808] border border-rasa-border p-4 text-white text-sm focus:border-rasa-red outline-none transition-colors h-24 resize-none rounded-sm"
              ></textarea>
            </div>

            <button 
              onClick={handleExecuteScan}
              disabled={location === "Select Location"}
              className={`w-full font-bold py-5 flex items-center justify-center gap-3 transition-colors text-sm uppercase tracking-widest rounded-sm ${location === "Select Location" ? 'bg-rasa-border text-rasa-muted cursor-not-allowed opacity-50' : 'bg-rasa-red hover:bg-[#ff3b53] text-white shadow-[0_0_30px_rgba(244,42,65,0.2)]'}`}
            >
              <Zap size={16} /> Find Restaurants
            </button>
          </div>

        </main>
      </div>
    );
  }

  if (view === 'loading') {
    return (
      <div className="min-h-screen flex flex-col">
        <Header />
        <main className="flex-1 flex flex-col justify-center items-center">
           <div className="w-16 h-16 border-t-2 border-r-2 border-rasa-red animate-spin rounded-full mb-8"></div>
            <div className="text-rasa-red font-mono uppercase tracking-widest text-sm animate-pulse">Curating your perfect list...</div>
        </main>
      </div>
    );
  }

  // Results View
  const recommendations = apiResults?.recommendations || [];
  const querySummary = apiResults?.query_summary || "No recommendations found.";

  return (
    <div className="min-h-screen flex flex-col pb-24">
      <Header />
      <main className="px-8 md:px-24 py-12 max-w-7xl mx-auto w-full">
        
        {/* Summary Box */}
        <div className="border border-rasa-border bg-rasa-panel p-6 md:p-8 mb-12 flex gap-6 relative rounded-sm">
          <div className="absolute left-0 top-0 h-full w-1 bg-rasa-red" />
          <div className="text-rasa-red opacity-80 pt-1 hidden md:block">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M3 21c3 0 7-1 7-8V5c0-1.25-.756-2.017-2-2H4c-1.25 0-2 .769-2 2.019v8c0 1.25.75 2.019 2 2.019h2c0 3.018-1 4-3 4z"></path><path d="M15 21c3 0 7-1 7-8V5c0-1.25-.757-2.017-2-2h-4c-1.25 0-2 .769-2 2.019v8c0 1.25.75 2.019 2 2.019h2c0 3.018-1 4-3 4z"></path></svg>
          </div>
          <div className="flex-1">
            <div className="flex justify-between items-center mb-3">
               <span className="text-[10px] font-mono text-rasa-red uppercase tracking-widest">Your Search Results</span>
               <span className="text-[10px] font-mono text-rasa-muted uppercase tracking-widest hidden md:block">{recommendations.length} Matches · Sorted by Best Match</span>
            </div>
            <p className="text-white text-xl md:text-2xl leading-snug font-medium">
              {querySummary}
            </p>
          </div>
        </div>

        {/* Results List */}
        <div className="space-y-6">
          {recommendations.length === 0 && (
            <div className="text-rasa-muted font-mono text-center py-12">No results found matching your preferences.</div>
          )}
          {recommendations.map((r: any, idx: number) => {
            
            return (
              <div key={r.rank || idx} className="group border border-rasa-border bg-[#0a0808] transition-all duration-300 rounded-sm overflow-hidden hover:border-rasa-red hover:shadow-[0_0_30px_rgba(244,42,65,0.1)]">
                
                {/* Content side */}
                <div className="p-6 md:p-10 flex-1 flex flex-col justify-between relative">
                  <div className="absolute top-0 right-0 flex">
                      <div className="bg-rasa-red text-white text-[10px] font-mono px-4 py-2 uppercase font-bold tracking-widest">
                        RANK #{r.rank}
                      </div>
                  </div>
                  <div className="mt-8 md:mt-4">
                    <div className="flex justify-between items-start mb-2">
                      <h3 className="text-2xl md:text-3xl font-bold text-white group-hover:text-rasa-red transition-colors">{r.restaurant_name}</h3>
                      <div className="text-right">
                        <div className="flex items-center justify-end text-rasa-red font-bold text-lg mb-1">
                          <Star size={16} className="fill-rasa-red mr-1" /> {r.rating}
                        </div>
                        <div className="text-[10px] font-mono text-rasa-muted uppercase tracking-widest">
                          ₹ {r.estimated_cost} / for two
                        </div>
                      </div>
                    </div>
                    
                    <div className="text-xs font-mono text-rasa-muted mb-6 flex items-center gap-2 uppercase tracking-widest">
                      <span className="w-1 h-1 rounded-full bg-rasa-border" />
                      {r.location}
                      <span className="w-1 h-1 rounded-full bg-rasa-border" />
                      {r.cuisine}
                    </div>

                    <div className="bg-[#121010] border border-rasa-border p-5 mb-6 rounded-sm transition-colors group-hover:border-rasa-red/30">
                      <div className="flex items-center gap-2 mb-3 text-[10px] font-mono text-rasa-red uppercase tracking-widest">
                        <Zap size={12} /> Why we recommend this
                      </div>
                      <p className="text-rasa-text text-sm leading-relaxed">
                        {r.explanation}
                      </p>
                    </div>
                  </div>

                  <div className="flex flex-wrap gap-2">
                    {(r.match_tags || []).map((b: string) => (
                      <span key={b} className="bg-[#1a1717] text-rasa-muted text-[10px] font-mono uppercase tracking-widest px-3 py-1.5 rounded-sm border border-rasa-border hover:border-rasa-muted transition-colors cursor-default">
                        {b}
                      </span>
                    ))}
                  </div>
                </div>

              </div>
            );
          })}
        </div>

      </main>
    </div>
  );
}
