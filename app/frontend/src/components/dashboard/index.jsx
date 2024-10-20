import { Grid2, Typography, Button } from '@mui/material';
import { useAuth } from "../../context/AuthContext";

const Dashboard = () => {
  const { logout } = useAuth();

  return (
    <Grid2
    container
    direction="column"
    alignItems="center"
    justifyContent="center"
    spacing={2}
    style={{ minHeight: "100vh" }}
  >
    <Grid2 item>
      <Typography variant="h4" component="h1" align="center">
        Welcome to MisterED
      </Typography>
    </Grid2>
    <Grid2 item>
      <Button variant="contained" color="primary" fullWidth onClick={logout}>
        Logout
      </Button>
    </Grid2>
  </Grid2>
  );
};

export default Dashboard;
