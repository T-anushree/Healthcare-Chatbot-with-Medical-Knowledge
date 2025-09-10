import React, { useState } from "react";
import axios from "axios";

function ChatComponent() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);

  const sendMessage = async () => {
    const res = await axios.post("http://localhost:8000/chat", { message });
    setChat([...chat, { user: "You", text: message }, { user: "Bot", text: res.data.reply }]);
    setMessage("");
  };

  return (
    <div className="chat-container">
      <div className="chat-box">
        {chat.map((msg, i) => (
          <p key={i}><b>{msg.user}:</b> {msg.text}</p>
        ))}
      </div>
      <input value={message} onChange={(e) => setMessage(e.target.value)} placeholder="Ask a medical question..." />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

export default ChatComponent;
