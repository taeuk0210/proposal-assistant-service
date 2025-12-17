import { useEffect, useState } from "react";
import { styled } from "@mui/material/styles";
import { Alert, Box, Snackbar, type AlertColor } from "@mui/material";
import PDFViewer from "@/components/file/PDFViewer";
import FileDropZone from "@/components/file/FileDropZone";
import FileUploadList from "@/components/file/FileUploadList";
import docService from "@/services/docService";
import FileDownlaodList from "./FileDownloadList";
import { type DocResponse } from "@/types/doc";

const StyledBox = styled(Box)(({ theme }) => ({
  display: "flex",
  flexDirection: "row",
  width: "125vh",
  justifySelf: "center",
  gap: theme.spacing(1),
}));

const StyledBox2 = styled(Box)(({ theme }) => ({
  display: "flex",
  flexDirection: "column",
  width: "125vh",
  justifySelf: "center",
  gap: theme.spacing(2),
}));

const FileContainer: React.FC = () => {
  const [fetchs, setFetchs] = useState<DocResponse[]>([]);
  const [files, setFiles] = useState<File[]>([]);
  const [file, setFile] = useState<File | null>(null);
  const [alert, setAlert] = useState<{
    open: boolean;
    color: AlertColor;
    message: string;
  }>({
    open: false,
    color: "success",
    message: "",
  });

  useEffect(() => {
    const fetch = async () => {
      const response = await docService.getDocuments();
      console.log(response);
      setFetchs(response.data.items);
    };

    fetch();
  }, []);

  const handleDrop = (acceptedFiles: File[]) => {
    setFiles((prev) => [...prev, ...acceptedFiles]);
  };

  const handleUpload = async (file: File) => {
    const formData = new FormData();
    formData.append("title", file.name);
    formData.append("file", file);

    const response = await docService.registerDocument(formData);
    if (response.status === 201) {
      setAlert({
        open: true,
        color: "success",
        message: "문서를 성공적으로 저장했어요 😊",
      });
    }
  };

  return (
    <StyledBox>
      <PDFViewer file={file} />
      <StyledBox2>
        <FileDropZone onDrop={handleDrop} />
        <FileUploadList
          files={files}
          setFile={setFile}
          onUpload={handleUpload}
        />
        <FileDownlaodList
          files={fetchs}
          setFile={setFile}
          onDownload={() => {}}
        />
      </StyledBox2>
      <Snackbar
        open={alert.open}
        onClose={() => setAlert((prev) => ({ ...prev, open: false }))}
        autoHideDuration={2000}
      >
        <Alert severity={alert.color}>{alert.message}</Alert>
      </Snackbar>
    </StyledBox>
  );
};

export default FileContainer;
