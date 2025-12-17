import axios from "axios";

const docApi = {
  registerDocument: async (fromData: FormData) => {
    return await axios.post("http://localhost:8800/api/v1/doc", fromData, {
      withCredentials: true,
    });
  },

  getDocuments: async () => {
    return await axios.get("http://localhost:8800/api/v1/doc", {
      withCredentials: true,
    });
  },

  getDocumentFile: async (documentId: number) => {
    return await axios.get(`http://localhost:8800/api/v1/doc/${documentId}`, {
      withCredentials: true,
      responseType: "blob",
    });
  },
};

export default docApi;
