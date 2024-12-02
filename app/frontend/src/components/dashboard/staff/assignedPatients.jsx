import { useState } from "react";
import Grid from "@mui/material/Grid2";
import React from "react";
import Typography from "@mui/material/Typography";
import { patients } from "../../../constants/applicationConstants";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import IconButton from "@mui/material/IconButton";
import { Button, Chip, Collapse } from "@mui/material";
import CardContent from "@mui/material/CardContent";
import Card from '@mui/material/Card';

const getColor = (score) => {
  const maxScore = 20; // TODO: Adjust this value based on the maximum possible score
  const red = Math.min(255, (score / maxScore) * 255);
  const green = Math.min(255, ((maxScore - score) / maxScore) * 255);
  return `rgb(${red}, ${green}, 0)`;
};

const AssignedPatients = () => {
  const [expanded, setExpanded] = useState(null);
  return (
    <Grid container direction={"column"} spacing={2} sx={{ m: 2 }}>
    <Grid item xs={12}>
      <Typography variant="h4" gutterBottom>
        Assigned Patients
      </Typography>
    </Grid>
    {patients.map((patient) => (
      <React.Fragment key={patient.id}>
        <Grid container item xs={12} spacing={2} alignItems="center" sx={{ mb: 2, p: 2, background: "#f9f9f9", borderRadius: 1, boxShadow: "0 2px 4px rgba(0, 0, 0, 0.1)" }}>
          <Grid item xs={12}>
            <Typography
              variant="body1"
              sx={{
                fontWeight: "bold",
                cursor: "pointer",
              }}
            >
              {patient.name}
            </Typography>
          </Grid>
            <Grid item xs={2}>
            <Chip
              sx={{
                backgroundColor: getColor(
                  patient.symptoms.reduce((acc, symptom) => acc + symptom.score, 0)
                ),
                fontWeight: "bold",
                color: "white",
              }}
              label={patient.symptoms.reduce(
                (acc, symptom) => acc + symptom.score,
                0
              )}
            />
          </Grid>
            <Grid item xs={2}>
            <IconButton
              color="primary"
              onClick={() =>
                setExpanded(
                  expanded === patient.healthCareNumber ? null : patient.healthCareNumber
                )
              }
              sx={{
                transform:
                  patient.healthCareNumber === expanded
                    ? "rotate(180deg)"
                    : "rotate(0deg)",
                transition: "transform 0.3s",
              }}
            >
              <ExpandMoreIcon />
            </IconButton>
          </Grid>
        </Grid>
          <Grid item xs={12}>
          <Collapse in={patient.healthCareNumber === expanded}>
            <Card variant="outlined" sx={{ p: 2, mb: 2, boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)" }}>
              <CardContent>
                <Typography variant="h6" gutterBottom>
                  Symptoms
                </Typography>
                {patient.symptoms.map((symptom, index) => (
                  <Typography key={index} variant="body2" sx={{ mb: 0.5 }}>
                    {symptom.symptom} ({symptom.score})
                  </Typography>
                ))}
              </CardContent>
              <Button variant="contained" color="primary" sx={{ mt: 1 }}>
                Add to Queue
              </Button>
            </Card>
          </Collapse>
        </Grid>
      </React.Fragment>
    ))}
  </Grid>
  );
};

export default AssignedPatients;
