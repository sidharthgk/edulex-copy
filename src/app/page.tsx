'use client'

import { useEffect, useState } from 'react'
import BetaSignupForm from '@/components/betaSignupform'

export default function Home() {
  const [showInfo, setShowInfo] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => setShowInfo(true), 1000);
    return () => clearTimeout(timer);
  }, []);

  return (
    <main className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 overflow-hidden">
      <div className="container mx-auto px-4 py-12 relative">
        <div className="text-center mb-12 animate-fade-in-down">
          <h1 className="text-6xl font-bold mb-4 text-white font-display">
            EDULEX AI
          </h1>
          <p className="text-2xl text-white font-subheading">Empowering Dyslexic Learners</p>
        </div>
        
        <div className="flex flex-col lg:flex-row gap-12 items-stretch">
          <div className="lg:w-1/2 animate-slide-in-left">
            <div className="bg-white bg-opacity-10 backdrop-blur-lg rounded-xl shadow-lg p-8 h-full">
              <h2 className="text-3xl font-bold mb-6 text-white font-heading">Revolutionizing Dyslexia Support</h2>
              <div className="space-y-4 font-body">
                {showInfo && (
                  <>
                    <p className="text-white animate-fade-in">
                      EDULEX AI is an innovative AI-powered platform designed to support individuals with dyslexia. Our cutting-edge technology provides personalized assistance for phonemic awareness, decoding, reading comprehension, and spelling.
                    </p>
                    <p className="text-white animate-fade-in" style={{animationDelay: '0.5s'}}>
                      Featuring an AR/AI assistant teacher, interactive learning games, and a supportive community, EDULEX AI aims to make the learning journey smoother and more rewarding for dyslexic learners.
                    </p>
                    <p className="text-white animate-fade-in" style={{animationDelay: '1s'}}>
                      With multi-language support and comprehensive progress tracking, we're committed to boosting academic performance and self-esteem for individuals with dyslexia worldwide.
                    </p>
                  </>
                )}
              </div>
            </div>
          </div>
          
          <div className="lg:w-1/2 animate-slide-in-right">
            <div className="bg-white bg-opacity-10 backdrop-blur-lg rounded-xl shadow-lg p-8 h-full">
              <div className="mb-6">
                <h3 className="text-3xl font-bold text-white text-center mb-4 font-heading">Coming Soon</h3>
                <div className="flex justify-center items-center space-x-2">
                  {[...Array(3)].map((_, i) => (
                    <div key={i} className={`w-3 h-3 bg-white rounded-full animate-bounce`} style={{animationDelay: `${i * 0.2}s`}}></div>
                  ))}
                </div>
              </div>
              <BetaSignupForm />
            </div>
          </div>
        </div>
      </div>
    </main>
  )
}