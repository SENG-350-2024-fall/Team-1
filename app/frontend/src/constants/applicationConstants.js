export const symptoms = [
  { symptom: "Coughing" },
  { symptom: "Headache" },
  { symptom: "Vomiting/Nausea" },
  { symptom: "Chest Pain" },
  { symptom: "Limb Numbness" },
  { symptom: "Vision Impacted" },
  { symptom: "Hearing Impacted" },
  { symptom: "Shortness of Breath" },
  { symptom: "Fever" },
  { symptom: "Fatigue" },
];

export const patients = [
  {
    healthCareNumber: "1234567890",
    name: "John Doe",
    age: 25,
    symptoms: [
      { symptom: "Coughing", score: 2 },
      { symptom: "Headache", score: 2 },
    ],
  },
  {
    healthCareNumber: "0987654321",
    name: "Jane Smith",
    age: 30,
    symptoms: [
      { symptom: "Chest Pain", score: 10 },
      { symptom: "Limb Numbness", score: 15 },
    ],
  },
  {
    healthCareNumber: "1122334455",
    name: "Alice Johnson",
    age: 40,
    symptoms: [
      { symptom: "Hearing Impacted", score: 3 },
      { symptom: "Vision Impacted", score: 5 },
      { symptom: "Headache", score: 2 },
    ],
  },
  {
    healthCareNumber: "6677889900",
    name: "Bob Brown",
    age: 35,
    symptoms: [
      { symptom: "Headache", score: 2 },
      { symptom: "Fatigue", score: 2 },
    ],
  },
  {
    healthCareNumber: "2233445566",
    name: "Charlie Davis",
    age: 28,
    symptoms: [
      { symptom: "Coughing", score: 2 },
      { symptom: "Fever", score: 8 },
      { symptom: "Headache", score: 2 },
      { symptom: "Vomiting/Nausea", score: 5 },
    ],
  },
];
