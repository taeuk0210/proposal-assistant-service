import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemText from "@mui/material/ListItemText";
import Checkbox from "@mui/material/Checkbox";
import { Button, Chip, Paper } from "@mui/material";
import { styled } from "@mui/material/styles";
import { handleFileSize } from "@/utils/handlers";

const StyledPaper = styled(Paper)(() => ({
  height: "25vh",
  width: "50vh",
  overflowY: "auto",
  scrollbarGutter: "stable",
}));

type FileUploadListProps = {
  files: File[];
  setFile: (f: File) => void;
  onUpload: (f: File) => void;
};

const FileUploadList: React.FC<FileUploadListProps> = ({
  files,
  setFile,
  onUpload,
}) => {
  return (
    <StyledPaper>
      <List>
        {files.map((f, i) => (
          <ListItem key={i}>
            <ListItemButton role={undefined} onClick={() => setFile(f)} dense>
              <ListItemText id={`${i}`} primary={f.name} />
              <Chip label={handleFileSize(f.size)} />
            </ListItemButton>
            <Button variant="outlined" onClick={() => onUpload(f)}>
              UPLOAD
            </Button>
          </ListItem>
        ))}
      </List>
    </StyledPaper>
  );
};

export default FileUploadList;
