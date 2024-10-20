import { Grid2, Button, Typography } from '@mui/material';
import { useNavigate } from 'react-router-dom'; // Import useNavigate for navigation

const LandingPage = () => {
  const navigate = useNavigate(); // useNavigate hook for programmatic navigation

  return (
    <Grid2
      container
      direction="column"
      alignItems="center"
      justifyContent="center"
      spacing={2}
      style={{ minHeight: '100vh' }}
    >
      <Grid2 item>
        <Typography variant="h4" component="h1" align="center">
          Mister ED
        </Typography>
      </Grid2>
      
      <Grid2 item>
        <Button 
          variant="contained" 
          color="primary" 
          fullWidth
          onClick={() => navigate('/patient-login')} // Navigate to Patient Login
        >
          Patient Login
        </Button>
      </Grid2>

      <Grid2 item>
        <Button 
          variant="contained" 
          color="secondary" 
          fullWidth
          onClick={() => navigate('/staff-login')} // Navigate to Staff Login (if needed)
        >
          Staff Login
        </Button>
      </Grid2>
    </Grid2>
  );
};

export default LandingPage;