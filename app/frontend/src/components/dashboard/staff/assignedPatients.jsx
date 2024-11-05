import { useState } from "react";
import Grid from "@mui/material/Grid2";
import React from "react";
import Typography from "@mui/material/Typography";
import { patients } from "../../../constants/applicationConstants";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import IconButton from "@mui/material/IconButton";
import { Button, Chip, Collapse } from "@mui/material";
import CardContent from "@mui/material/CardContent";
import Box from "@mui/material/Box";

const getColor = (score) => {
  const maxScore = 20; // TODO: Adjust this value based on the maximum possible score
  const red = Math.min(255, (score / maxScore) * 255);
  const green = Math.min(255, ((maxScore - score) / maxScore) * 255);
  return `rgb(${red}, ${green}, 0)`;
};

const AssignedPatients = () => {
  const [expanded, setExpanded] = useState(null);
  return (
    <Grid container spacing={2} sx={{ m: 2 }}>
      <Grid size={12}>
        <Typography variant="h4">Assigned Patients</Typography>
      </Grid>
      {patients.map((patient) => (
        <>
          <Grid key={patient.id} size={9}>
            <Typography
              variant="body1"
              sx={{
                cursor: "pointer",
                background: "white",
                border: "none",
                padding: 0,
                fontWeight: "bold",
              }}
            >
              {patient.name}
            </Typography>
          </Grid>
          <Grid size={2}>
            <Chip
              sx={{
                backgroundColor: getColor(
                  patient.symptoms.reduce(
                    (acc, symptom) => acc + symptom.score,
                    0
                  )
                ),
              }}
              label={patient.symptoms.reduce(
                (acc, symptom) => acc + symptom.score,
                0
              )}
            />
          </Grid>
          <Grid size={1}>
            <IconButton
              key={patient.healthCareNumber}
              color="primary"
              onClick={() => {
                setExpanded(expanded ? null : patient.healthCareNumber);
              }}
              sx={{
                transform:
                  patient.healthCareNumber === expanded
                    ? "rotate(180deg)"
                    : "rotate(0deg)",
              }}
            >
              <ExpandMoreIcon />
            </IconButton>
          </Grid>
          <Collapse in={patient.healthCareNumber === expanded}>
            <CardContent>
              {patient.symptoms.map((symptom) => (
                <Typography variant="body1">{symptom.symptom}{" "}({symptom.score})</Typography>
              ))}
            </CardContent>
            <Button
              variant="contained"
              color="primary"
              onClick={null}
            >
              Add to Queue
            </Button>
          </Collapse>
        </>
      ))}
    </Grid>
  );
};

export default AssignedPatients;
