import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LandingPage from "../components/home";
import PatientLogin from "../components/patientLogin"; // Import login components from index
import  StaffLogin  from "../components/staffLogin"; // Import login components from index
import Register from "../components/register";
import Dashboard from "../components/dashboard";
import ProtectedRoute from "./ProtectedRoute";
import { AuthProvider } from "../context/AuthContext";

const AppRoutes = () => {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route
            path="/"
            element={
              <ProtectedRoute>
                <Dashboard />
              </ProtectedRoute>
            }
          />
        <Route path="/home" element={<LandingPage/>} />           {/* Landing page */}
        <Route path="/patient-login" element={<PatientLogin />} /> {/* Patient login page */}
        <Route path="/staff-login" element={<StaffLogin />} />    {/* Staff login page */}
        </Routes>
      </Router>
    </AuthProvider>
  );
};

export default AppRoutes;
