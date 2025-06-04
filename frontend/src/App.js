import React, { useState, useRef, useEffect } from "react";
import TextChat from "./components/TextChat";

export default function App() {
  const [messages, setMessages] = useState([]);
  const chatRef = useRef(null);

  // Append user message when TextChat notifies us
  const handleUserInput = (userText) => {
    setMessages((prev) => [...prev, { role: "user", text: userText }]);
  };

  // Append streaming AI response chunks
  const appendResponse = (chunk) => {
    setMessages((prev) => {
      const lastMsg = prev[prev.length - 1];
      if (lastMsg && lastMsg.role === "ai") {
        const updated = [...prev];
        updated[updated.length - 1] = { ...lastMsg, text: lastMsg.text + chunk };
        return updated;
      } else {
        return [...prev, { role: "ai", text: chunk }];
      }
    });
  };

  useEffect(() => {
    chatRef.current?.scrollTo(0, chatRef.current.scrollHeight);
  }, [messages]);

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        height: "100vh",
        fontFamily: "sans-serif",
      }}
    >
      <div
        ref={chatRef}
        style={{
          flexGrow: 1,
          overflowY: "auto",
          padding: "1rem",
          backgroundColor: "#f5f5f5",
          display: "flex",
          flexDirection: "column",
          gap: "8px",
        }}
      >
        {messages.map((msg, i) => (
          <div
            key={i}
            style={{
              maxWidth: "60%",
              alignSelf: msg.role === "user" ? "flex-end" : "flex-start",
              backgroundColor: msg.role === "user" ? "#0b60ff" : "#e0e0e0",
              color: msg.role === "user" ? "white" : "black",
              padding: "10px",
              borderRadius: "12px",
              whiteSpace: "pre-wrap",
            }}
          >
            {msg.text}
          </div>
        ))}
      </div>

      {/* Pass onResponse and onUserInput handlers */}
      <TextChat onResponse={appendResponse} onUserInput={handleUserInput} />
    </div>
  );
}