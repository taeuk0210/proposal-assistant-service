import chatApi from "@/api/chatApi";
import type { ChatRequest } from "@/types/chat";

const chatService = {
  sendMessage: async (request: ChatRequest) => {
    const response = await chatApi.sendMessage(request);
    return response.data.reply;
  },
};

export default chatService;
