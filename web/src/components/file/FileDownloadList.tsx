import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemText from "@mui/material/ListItemText";
import { Button, Chip, Paper } from "@mui/material";
import { styled } from "@mui/material/styles";
import { handleFileSize } from "@/utils/handlers";
import type { DocResponse } from "@/types/doc";
import docService from "@/services/docService";

const StyledPaper = styled(Paper)(() => ({
  height: "25vh",
  width: "50vh",
  overflowY: "auto",
  scrollbarGutter: "stable",
}));

type FileDownlaodListProps = {
  files: DocResponse[];
  setFile: (f: File) => void;
  onDownload: (f: File) => void;
};

const FileDownlaodList: React.FC<FileDownlaodListProps> = ({
  files,
  setFile,
  onDownload,
}) => {
  const handleClick = async (documentId: number) => {
    setFile(await docService.getDocumentFile(documentId));
  };
  return (
    <StyledPaper>
      <List>
        {files.map((f, i) => (
          <ListItem key={i}>
            <ListItemButton
              role={undefined}
              onClick={() => handleClick(f.id)}
              dense
            >
              <ListItemText id={`${i}`} primary={f.title} />
              <Chip label={handleFileSize(f.size)} />
            </ListItemButton>
            <Button variant="outlined" onClick={() => {}}>
              DOWNLOAD
            </Button>
          </ListItem>
        ))}
      </List>
    </StyledPaper>
  );
};

export default FileDownlaodList;
