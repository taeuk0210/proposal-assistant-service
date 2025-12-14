import type { ChatRequest } from "@/types/chat";
import axios from "axios";

const chatApi = {
  sendMessage: async (request: ChatRequest) => {
    return await axios.post(
      "http://localhost:8800/api/v1/chat", 
      request,
      {withCredentials: true});
  },
};

export default chatApi;
