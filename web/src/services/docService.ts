import docApi from "@/api/docApi";

const docService = {
  registerDocument: async (formData: FormData) => {
    return await docApi.registerDocument(formData);
  },

  getDocuments: async () => {
    return await docApi.getDocuments();
  },
  getDocumentFile: async (documentId: number) => {
    const response = await docApi.getDocumentFile(documentId);
    return new File([response.data], "file.pdf", { type: "application/pdf" });
  },
};

export default docService;
