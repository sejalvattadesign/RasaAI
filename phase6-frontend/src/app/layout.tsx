import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "RASA.AI - Culinary Intelligence",
  description: "Find your next great meal, curated by AI.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased min-h-screen text-rasa-text bg-rasa-bg overflow-x-hidden selection:bg-rasa-red selection:text-white">
        {children}
      </body>
    </html>
  );
}
