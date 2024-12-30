'use client'

import { useState } from 'react'

export default function BetaSignupForm() {
  const [email, setEmail] = useState('')
  const [notifyBeta, setNotifyBeta] = useState(false)
  const [source, setSource] = useState('')

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    // Handle form submission logic here
    console.log({ email, notifyBeta, source })
  }

  return (
    <form onSubmit={handleSubmit} className="beta-signup-form bg-white bg-opacity-10 backdrop-blur-lg p-6 rounded-lg shadow-md" data-netlify="true">
      <h3 className="text-xl font-heading mb-4 text-white">Join our waitlist and try us completely free!</h3>
      <p className="mb-4 text-white">We will email you a link to the email provided once we beta launch.</p>
      
      <div className="mb-4">
        <label htmlFor="email" className="block mb-2 text-white">Email *</label>
        <input
          type="email"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
          className="w-full px-3 py-2 border border-white rounded bg-white bg-opacity-10 text-white"
        />
      </div>
      
      <div className="mb-4">
        <label className="flex items-center text-white">
          <input
            type="checkbox"
            checked={notifyBeta}
            onChange={(e) => setNotifyBeta(e.target.checked)}
            className="mr-2"
          />
          Yes, I would like to know when the app is available to beta test.
        </label>
      </div>
      
      <div className="mb-4">
        <p className="mb-2 text-white">How'd you hear about us?</p>
        {['Google Search', 'Facebook', 'LinkedIn', 'Reddit', 'Family or Friend', 'Other'].map((option) => (
          <label key={option} className="flex items-center mb-2 text-white">
            <input
              type="radio"
              name="source"
              value={option}
              checked={source === option}
              onChange={(e) => setSource(e.target.value)}
              className="mr-2"
            />
            {option}
          </label>
        ))}
      </div>
      
      <button type="submit" className="w-full py-2 px-4 bg-white bg-opacity-10 border border-white rounded text-white hover:bg-opacity-20 transition duration-300">
        Submit
      </button>
    </form>
  )
}
