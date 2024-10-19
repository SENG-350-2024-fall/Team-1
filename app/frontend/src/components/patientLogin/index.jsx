import { Grid, TextField, Button, Typography } from '@mui/material';

const patientLogin = () => {
  return (
    <Grid
      container
      direction="column"
      alignItems="center"
      justifyContent="center"
      spacing={2}
      style={{ minHeight: '100vh' }}
    >
      <Grid item>
        <Typography variant="h4" component="h1" align="center">
         MisterED Staff Login
        </Typography>
      </Grid>
      <Grid item>
        <TextField 
          label="Health Care Number" 
          type="healthCareNumber" 
          variant="outlined" 
          fullWidth 
        />
      </Grid>
      <Grid item>
        <Button 
          variant="contained" 
          color="primary" 
          fullWidth
        >
          Login
        </Button>
      </Grid>
    </Grid>
  );
};

export default patientLogin;
