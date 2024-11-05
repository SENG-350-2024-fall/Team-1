import { createContext, useContext, useState } from "react";
import { useNavigate } from "react-router-dom";

const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [userType, setUserType] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [healthCareNumber, setHealthCareNumber] = useState("");
  const navigate = useNavigate();

  const staffLogin = async () => {
    try {
      const response = await fetch("http://localhost:5000/api/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
      });

      if (response.ok) {
        setIsAuthenticated(true);
        setUserType("staff");
        navigate("/");
      }
    } catch (error) {
      console.error("Login failed:", error);
    }
    setUsername("");
    setPassword("");
  };

  const patientLogin = async () => {
    try {
      const response = await fetch("http://localhost:5000/api/patient_login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ healthCareNumber }),
      });

      if (response.ok) {
        setIsAuthenticated(true);
        setUserType("patient");
        navigate("/");
      } else {
        setHealthCareNumber("");
      }
    } catch (error) {
      console.error("Login failed:", error);
    }
  };

  const logout = () => {
    setIsAuthenticated(false);
    setHealthCareNumber("");
    navigate("/home");
    setUserType("");
  };

  return (
    <AuthContext.Provider
      value={{
        isAuthenticated,
        staffLogin,
        patientLogin,
        logout,
        setUsername,
        setPassword,
        setHealthCareNumber,
        healthCareNumber,
        userType,
        username,
        password,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};
