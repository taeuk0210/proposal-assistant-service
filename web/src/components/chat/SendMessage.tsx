import { Box, Button, TextField } from "@mui/material";
import { styled } from "@mui/material/styles";

const StyledTextField = styled(TextField)(({ theme }) => ({
  padding: theme.spacing(2),
  width: "80%",
  ...theme.typography.body1,
}));

const StyledButton = styled(Button)(({ theme }) => ({
  padding: theme.spacing(2),
  width: "20%",
  ...theme.typography.body1,
}));

const StyledBox = styled(Box)(() => ({
  display: "flex",
  alignItems: "center",
}));

type SendMessageProps = {
  message: string;
  setMessage: (text: string) => void;
  onSend: (text: string) => void;
};

const SendMessage: React.FC<SendMessageProps> = ({ message, setMessage, onSend }) => {
  return (
    <StyledBox>
      <StyledTextField
        id="send-message"
        label=""
        multiline
        maxRows={4}
        value={message}
        onKeyDown={(e) => {
          if (e.key == "Enter" && !e.shiftKey) {
            e.preventDefault();
            onSend(message);
          }
        }}
        onChange={(e) => setMessage(e.target.value)}
      />
      <StyledButton variant="contained" onClick={() => onSend(message)}>
        전송
      </StyledButton>
    </StyledBox>
  );
};

export default SendMessage;
