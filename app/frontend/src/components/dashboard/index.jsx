import { useEffect, useState } from "react";
import { Box, Typography, Button, Paper, Tabs, Tab } from "@mui/material";
import { useAuth } from "../../context/AuthContext";
import PatientVirtualTriageReport from "./patient/patientVirtualTriage";
import AssignedPatients from "./staff/assignedPatients";
import { If, Then } from "react-if";

const Dashboard = () => {
  const { logout, userType } = useAuth();
  const [value, setValue] = useState(0);
  const { healthCareNumber } = useAuth();
  const [queuePosition, setQueuePosition] = useState(null);

  useEffect(() => {
    let intervalId;
  
    const getQueuePosition = async () => {
      const apiEndpoint = "http://localhost:5000/api/get_queue_pos";
  
      try {
        const payload = { healthCareNumber };
  
        const response = await fetch(apiEndpoint, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(payload),
        });
  
        // Parse the response
        const result = await response.json();
  
        // Handle the response
        if (response.ok && result.success) {
          setQueuePosition(Number(result.queue_pos));
        }
      } catch (error) {
        console.error("Error while fetching queue position:", error);
      }
    };
  
    // Set up the interval
    intervalId = setInterval(getQueuePosition, 5000);
  
    // Cleanup interval on unmount or healthCareNumber change
    return () => clearInterval(intervalId);
  }, [healthCareNumber]);

  const handleLeaveQueue = async () => {
    const apiEndpoint = "http://localhost:5000/api/remove_patient";

    try {
      const payload = { healthCareNumber };

      await fetch(apiEndpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });
      setQueuePosition(null);
    } catch (error) {
      console.error("Error while leaving queue:", error);
    }
  };

  return (
    <Box
      style={{ display: "flex", flexDirection: "column", minHeight: "100vh" }}
    >
      <Button
        variant="contained"
        color="primary"
        onClick={logout}
        style={{ position: "absolute", top: "20px", right: "20px" }}
      >
        Logout
      </Button>

      <If condition={queuePosition != null}>
        <Then>
          <Button
            variant="outlined"
            color="secondary"
            onClick={null}
            style={{ position: "absolute", top: "60px", right: "20px" }}
          >
            Queue Position: {queuePosition + 1} {/* 0-based index */}
          </Button>
          <Button
            variant="contained"
            color="secondary"
            onClick={handleLeaveQueue}
            style={{ position: "absolute", top: "100px", right: "20px" }}
          >
            Leave Queue
          </Button>
        </Then>
      </If>

      {/* Welcome Title */}
      <Typography
        variant="h4"
        component="h1"
        align="left"
        style={{ marginTop: "20px" }}
      >
        MisterED
      </Typography>

      {/* Main Content Section */}
      <Box
        style={{
          flex: 1,
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        {userType === "patient" && (
          <>
            {value === 0 && (
              <Typography variant="h5" component="h2" align="center">
                Appointments Page
              </Typography>
            )}
            {value === 1 && (
              <Typography variant="h5" component="h2" align="center">
                Medical Records Page
              </Typography>
            )}
            {value === 2 && <PatientVirtualTriageReport />}
          </>
        )}
        {userType === "staff" && (
          <>
            {value === 0 && (
              <Typography variant="h5" component="h2" align="center">
                Shift Schedule Page
              </Typography>
            )}
            {value === 1 && <AssignedPatients />}
            {value === 2 && (
              <Typography variant="h5" component="h2" align="center">
                Reports Page
              </Typography>
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
          {userType ===
          "patient" /* Role-Based Conditional Rendering Design Pattern */
            ? [
                <Tab key="appointments" label="Appointments" />,
                <Tab key="medical-records" label="Medical Records" />,
                <Tab key="virtual-triage" label="Virtual Triage" />,
              ]
            : [
                <Tab key="shift-schedule" label="Shift Schedule" />,
                <Tab key="assigned-patients" label="Assigned Patients" />,
                <Tab key="reports" label="Reports" />,
              ]}
        </Tabs>
      </Paper>
    </Box>
  );
};

export default Dashboard;
