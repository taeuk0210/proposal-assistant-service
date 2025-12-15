import { useEffect, useRef, useState } from "react";
import { styled } from "@mui/material/styles";
import { Box } from "@mui/material";

import type { ChatContent } from "@/types/chat";

import ChatMessageList from "@/components/chat/ChatMessageList";
import SendMessage from "@/components/chat/SendMessage";
import chatService from "@/services/chatService";

const StyledBox = styled(Box)(() => ({
  height: "100vh",
  width: "50vh",
  justifySelf: "center",
}));

const ChatContainer: React.FC = () => {
  const [message, setMessage] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);
  const [messages, setMessages] = useState<ChatContent[]>([
    { roleType: "assistant", message: "안녕하세요 🙂 무엇을 도와드릴까요?" },
  ]);
  const scrollRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const el = scrollRef.current;
    if (!el) return;

    el.scrollTo({
      top: el.scrollHeight,
      behavior: "smooth",
    });
  }, [messages]);

  const handleSend = async (message: string) => {
    const trimemedText = message.trim();
    if (!trimemedText) return;

    setMessages((prev) => [
      ...prev,
      { roleType: "user", message: trimemedText },
    ]);
    setMessage("");
    setLoading(true);

    const reply = await chatService.sendMessage({ message: trimemedText });
    setLoading(false);
    setMessages((prev) => [...prev, { roleType: "assistant", message: reply }]);
  };

  return (
    <StyledBox>
      <ChatMessageList
        data={messages}
        scrollRef={scrollRef}
        loading={loading}
      />
      <SendMessage
        message={message}
        setMessage={setMessage}
        onSend={handleSend}
      />
    </StyledBox>
  );
};

export default ChatContainer;
