import {
  Grid2,
  TextField,
  Button,
  Typography,
  IconButton,
} from "@mui/material";
import { useAuth } from "../../context/AuthContext";
import { useNavigate } from "react-router-dom";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";

const StaffLogin = () => {
  const navigate = useNavigate();
  const { setUsername, setPassword, login, username, password } = useAuth();

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
          MisterED Staff Login
        </Typography>
      </Grid2>
      <Grid2 item>
        <TextField
          label="Username"
          variant="outlined"
          fullWidth
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
      </Grid2>
      <Grid2 item>
        <TextField
          label="Password"
          type="password"
          variant="outlined"
          fullWidth
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </Grid2>
      <Grid2 item>
        <Button
          variant="contained"
          color="primary"
          fullWidth
          onClick={() => {
            login("staff", { username, password });
            setPassword("");
            setUsername("");
          }}
        >
          Login
        </Button>
      </Grid2>
    </Grid2>
  );
};

export default StaffLogin;
