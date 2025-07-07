import React, { useState } from 'react';

const TextChat = ({ onResponse }) => {
  const [input, setInput] = useState("");

  const sendText = async () => {
    const response = await fetch("http://localhost:8000/chat/text", {
      method: "POST",
      body: new URLSearchParams({ prompt: input }),
    });
    setInput(""); // Clear input after sending

    const reader = response.body.getReader();
    const decoder = new TextDecoder("utf-8");
    let text = "";

    const read = async () => {
      const { done, value } = await reader.read();
      if (done) return;
      const chunk = decoder.decode(value);
      text += chunk;
      onResponse(chunk);
      read();
    };

    read();
  };

  return (
    <div style={{ display: "flex", gap: 8, padding: "1rem", borderTop: "1px solid #ccc" }}>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && sendText()}
        placeholder="Ask C.A.S.E something..."
        style={{
          flexGrow: 1,
          padding: "10px",
          fontSize: "1rem",
          borderRadius: "8px 0 0 8px",
          border: "1px solid #ccc",
          outline: "none",
        }}
      />
      <button
        onClick={sendText}
        style={{
          padding: "10px 16px",
          fontSize: "1rem",
          borderRadius: "0 8px 8px 0",
          border: "none",
          backgroundColor: "#0b60ff",
          color: "white",
          cursor: "pointer",
        }}
      >
        Send
      </button>
    </div>
  );
};

export default TextChat;