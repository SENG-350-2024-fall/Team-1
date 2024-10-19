import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "../components/login";
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
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
};

export default AppRoutes;
