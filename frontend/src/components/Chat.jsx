import React, { useState, useEffect, useRef } from "react";
import axios from "axios";

export default function Chat() {
  const [messages, setMessages] = useState(() => {
    const saved = localStorage.getItem("chatHistory");
    return saved ? JSON.parse(saved) : [];
  });
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    localStorage.setItem("chatHistory", JSON.stringify(messages));
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSend = async () => {
    if (!query.trim()) return;

    const newMessages = [...messages, { role: "user", text: query }];
    setMessages(newMessages);
    setQuery(""); // ✅ Clears the input immediately
    setLoading(true);

    try {
      const res = await axios.post("http://127.0.0.1:8000/chat", { query });
      setMessages([
        ...newMessages,
        { role: "bot", text: res.data.answer }
      ]);
    } catch (error) {
      console.error("❌ Backend error:", error);
      setMessages([
        ...newMessages,
        { role: "bot", text: "⚠️ Unable to fetch response. Try again later." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleClearHistory = () => {
    if (window.confirm("Are you sure you want to clear the chat history?")) {
      setMessages([]);
      localStorage.removeItem("chatHistory");
    }
  };

  return (
    <div className="p-4 max-w-2xl mx-auto"> {/* ✅ made container slightly wider */}
      <h1 className="text-3xl font-bold text-center mb-1 text-blue-700">
        Ask NUST
      </h1>
      <p className="text-center text-gray-500 mb-4">
        💡 Ask me about UG/PG programs, admissions, and more!
      </p>

      {/* Chat Window */}
      <div className="border rounded-xl p-3 h-[600px] overflow-y-auto bg-gray-50 shadow-sm mb-4">
        {/* ✅ h-[600px] → much taller chat box */}
        {messages.length === 0 ? (
          <p className="text-gray-400 text-center">
            👋 Hi! What would you like to know about NUST?
          </p>
        ) : (
          messages.map((msg, idx) => (
            <div
              key={idx}
              className={`flex mb-2 ${
                msg.role === "user" ? "justify-end" : "justify-start"
              }`}
            >
              <div
                className={`px-3 py-2 rounded-2xl max-w-[75%] ${
                  msg.role === "user"
                    ? "bg-blue-600 text-white"
                    : "bg-gray-200 text-gray-900"
                }`}
              >
                {msg.text}
              </div>
            </div>
          ))
        )}
        {loading && (
          <p className="italic text-gray-500 text-center">Bot is typing...</p>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Input & Buttons */}
      <div className="flex gap-2">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSend()}
          placeholder="Ask about UG/PG programs..."
          className="flex-1 border rounded-lg px-3 py-2 shadow-sm"
        />
        <button
          onClick={handleSend}
          className="bg-blue-600 hover:bg-blue-700 text-white px-4 rounded-lg"
        >
          Send
        </button>
        <button
          onClick={handleClearHistory}
          className="bg-gray-300 hover:bg-gray-400 text-black px-4 rounded-lg"
        >
          Clear
        </button>
      </div>
    </div>
  );
}
