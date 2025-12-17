import { TextField } from "@mui/material";

type TextFieldProps = {
  label: string;
  value: string;
  setValue: (value: string) => void;
  inputType?: string;
};

const TextInput: React.FC<TextFieldProps> = ({
  label,
  value,
  setValue,
  inputType = "text",
}) => {
  return (
    <TextField
      label={label}
      value={value}
      onChange={(e) => setValue(e.target.value)}
      variant="filled"
      type={inputType}
    />
  );
};

export default TextInput;
