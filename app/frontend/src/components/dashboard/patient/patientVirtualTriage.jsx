import { useEffect, useState } from "react";
import Divider from "@mui/material/Divider";
import Typography from "@mui/material/Typography";
import OutlinedInput from "@mui/material/OutlinedInput";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import ListItemText from "@mui/material/ListItemText";
import Select from "@mui/material/Select";
import Checkbox from "@mui/material/Checkbox";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import Grid from "@mui/material/Grid2";
import { symptoms } from "../../../constants/applicationConstants";
import { useAuth } from "../../../context/AuthContext";

const ITEM_HEIGHT = 48;
const ITEM_PADDING_TOP = 8;
const MenuProps = {
  PaperProps: {
    style: {
      maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
      width: 250,
    },
  },
};

const PatientVirtualTriageReport = () => {
  const [selectedSymptoms, setSelectedSymptoms] = useState([]);
  const [patientTriageScore, setPatientTriageScore] = useState(0);
  const { healthCareNumber } = useAuth();

  const handleChange = (event) => {
    const {
      target: { value },
    } = event;
    setSelectedSymptoms(typeof value === "string" ? value.split(",") : value);
  };

  useEffect(() => {
    let score = 0;
    selectedSymptoms.forEach((symptom) => {
      const foundSymptom = symptoms.find((s) => s.symptom === symptom);
      if (foundSymptom) {
        score += foundSymptom.score;
      }
    });
    setPatientTriageScore(score);
  }, [selectedSymptoms]);

  const onSubmitHandler = async () => {
    if (!selectedSymptoms.length) return;
    // TODO: Submit the triage report to the backend
  };

  return (
    <Grid container spacing={3} sx={{ m: 2 }}>
      <Grid size={12}>
        <Typography variant="h4">Virtual Triage Report</Typography>
      </Grid>

      <Grid size={12}>
        <Divider />
      </Grid>

      <Grid size={12}>
        <Typography variant="subtitle1">
          Select Symptoms from the List below
        </Typography>
      </Grid>

      <Grid size={12}>
        <InputLabel id="demo-multiple-checkbox-label">Symptoms</InputLabel>
        <Select
          labelId="demo-multiple-checkbox-label"
          id="demo-multiple-checkbox"
          multiple
          value={selectedSymptoms}
          onChange={handleChange}
          input={<OutlinedInput label="Symptoms" />}
          renderValue={(selected) => selected.join(", ")}
          MenuProps={MenuProps}
          fullWidth
        >
          {symptoms.map((symptom) => (
            <MenuItem key={symptom.symptom} value={symptom.symptom}>
              <Checkbox checked={selectedSymptoms.includes(symptom.symptom)} />
              <ListItemText primary={symptom.symptom} />
            </MenuItem>
          ))}
        </Select>
      </Grid>

      <Grid size={12}>
        <Typography variant="subtitle1">
          Enter any Additional Information below
        </Typography>
      </Grid>

      <Grid size={12}>
        <TextField
          id="outlined-multiline-static"
          label="Additional Information"
          multiline
          minRows={4}
          placeholder="Write any additional comments or information here"
          fullWidth
        />
      </Grid>

      <Grid size={12}>
        <Button variant="contained" sx={{ mt: 3 }} onClick={onSubmitHandler}>
          Submit
        </Button>
      </Grid>
    </Grid>
  );
};

export default PatientVirtualTriageReport;
