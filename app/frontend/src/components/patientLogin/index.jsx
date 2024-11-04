import {
  Grid2,
  TextField,
  Button,
  Typography,
  IconButton,
} from "@mui/material";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

const PatientLogin = () => {
  const navigate = useNavigate();
  const { setHealthCareNumber, patientLogin } = useAuth();

  const handleBack = () => {
    navigate("/home");
  };

  return (
    <Grid2
      container
      direction="column"
      alignItems="center"
      justifyContent="center"
      spacing={2}
      style={{ minHeight: "100vh" }}
    >
      <IconButton
        onClick={handleBack}
        style={{
          position: "absolute",
          top: 16,
          left: 16,
          backgroundColor: "lightgray",
        }}
      >
        <ArrowBackIcon />
      </IconButton>
      <Grid2 item>
        <Typography variant="h4" component="h1" align="center">
          MisterED Patient Login
        </Typography>
      </Grid2>
      <Grid2 item>
        <TextField
          label="Health Care Number"
          type="healthCareNumber"
          variant="outlined"
          fullWidth
          onChange={(e) => setHealthCareNumber(e.target.value)}
        />
      </Grid2>
      <Grid2 item>
        <Button variant="contained" color="primary" fullWidth onClick={patientLogin}>
          Login
        </Button>
      </Grid2>
    </Grid2>
  );
};

export default PatientLogin;
