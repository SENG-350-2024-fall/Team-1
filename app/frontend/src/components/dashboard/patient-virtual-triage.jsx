import * as React from 'react';
import Paper from '@mui/material/Paper';
import Divider from '@mui/material/Divider';
import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import { styled } from '@mui/material/styles';
import Typography from '@mui/material/Typography';
import OutlinedInput from '@mui/material/OutlinedInput';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import ListItemText from '@mui/material/ListItemText';
import Select from '@mui/material/Select';
import Checkbox from '@mui/material/Checkbox';
import TextField from '@mui/material/TextField';
import { spacing } from '@mui/system';
import Button from '@mui/material/Button';

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

const symptoms = [
    'coughing',
    'headache',
    'vomiting/nausea',
    'chest pain',
    'limb numbness',
    'vision impacted',
    'hearing impacted',
    'shortness of breath',
    'fever',
    'fatigue',
  ];


const Item = styled('div')(({ theme }) => ({
  ...theme.typography.h2,
  padding: theme.spacing(1),
  textAlign: 'center',
  color: theme.palette.text.secondary,
}));    

const Item2 = styled('div')(({ theme }) => ({
    ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: 'center',
  color: theme.palette.text.secondary,
}));   




const PatientVirtualTriageReport = () => {

    const [selectedSymptoms, setSelectedSymptoms] = React.useState([]);

    const handleChange = (event) => {
        const {
            target: { value },
        } = event;
        setSelectedSymptoms(
      // On autofill we get a stringified value.
        typeof value === 'string' ? value.split(',') : value,
        );
    };

  return (
    <div>
    <Stack>

        <Item> Virtual Triage Report </Item>
        <Divider/>
        <Item2  sx={{pt:6}} > Select Symptoms from the List below </Item2>
            
            <FormControl sx={{ m: 1, width:650}}>
                <InputLabel id="demo-multiple-checkbox-label">Symptoms</InputLabel>
                <Select
                    labelId="demo-multiple-checkbox-label"
                    id="demo-multiple-checkbox"
                    multiple
                    value={selectedSymptoms}
                    onChange={handleChange}
                    input={<OutlinedInput label="Tag" />}
                    renderValue={(selected) => selected.join(', ')}
                    MenuProps={MenuProps}
                    fullWidth
                >
                    {symptoms.map((symptom) => (
                        <MenuItem key={symptom} value={symptom}>
                            <Checkbox checked={selectedSymptoms.includes(symptom)} />
                            <ListItemText primary={symptom} />
                        </MenuItem>
                    ))}
                </Select>
            </FormControl>
            

        <Item2  sx={{pt:9}} > Enter any Additional Information below </Item2>
            <TextField
                id="outlined-multiline-static"
                label="Additional Information"
                multiline
                minRows={4}
                placeholder="Write any additional comments or information here"
            />

    </Stack>

    <Button variant="contained" sx={{mt:6}}  >Submit</Button>
    </div>
  );
};

export default PatientVirtualTriageReport;