import { useState } from 'react';
import { Box, Typography, Button, Paper, Tabs, Tab } from '@mui/material';
import { useAuth } from '../../context/AuthContext';
import PatientVirtualTriageReport from './patient-virtual-triage';

const Dashboard = () => {
  const { logout, userType } = useAuth();
  const [value, setValue] = useState(0);

  return (
    <Box style={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
      {/* Logout Button Positioned at the Top Right */}
      <Button 
        variant="contained" 
        color="primary" 
        onClick={logout} 
        style={{ position: 'absolute', top: '20px', right: '20px' }}
      >
        Logout
      </Button>

      {/* Welcome Title */}
      <Typography variant="h4" component="h1" align="left" style={{ marginTop: '20px' }}>
        MisterED
      </Typography>

      {/* Main Content Section */}
      <Box style={{ flex: 1, display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        {userType === 'patient' && (
          <>
            {value === 0 && (
              <Typography variant="h5" component="h2" align="center">Appointments Page</Typography>
            )}
            {value === 1 && (
              <Typography variant="h5" component="h2" align="center">Medical Records Page</Typography>
            )}
            {value === 2 && (
              // <Typography variant="h5" component="h2" align="center">Virtual Triage Page</Typography>
              <PatientVirtualTriageReport />
            )}
          </>
        )}
        {userType === 'staff' && (
          <>
            {value === 0 && (
              <Typography variant="h5" component="h2" align="center">Shift Schedule Page</Typography>
            )}
            {value === 1 && (
              <Typography variant="h5" component="h2" align="center">Assigned Patients Page</Typography>
            )}
            {value === 2 && (
              <Typography variant="h5" component="h2" align="center">Reports Page</Typography>
            )}
          </>
        )}
      </Box>

      {/* Tabs Positioned at the Bottom */}
      <Paper square>
      <Tabs
  value={value}
  onChange={(event, newValue) => setValue(newValue)}
  indicatorColor="primary"
  textColor="primary"
  
>
  {userType === 'patient' /* Role-Based Conditional Rendering Design Pattern */
    ? [
        <Tab key="appointments" label="Appointments" />,
        <Tab key="medical-records" label="Medical Records" />,
        <Tab key="virtual-triage" label="Virtual Triage" />
      ]
    : [
        <Tab key="shift-schedule" label="Shift Schedule" />,
        <Tab key="assigned-patients" label="Assigned Patients" />,
        <Tab key="reports" label="Reports" />
      ]
  }
</Tabs>

      </Paper>
    </Box>
  );
};

export default Dashboard;
