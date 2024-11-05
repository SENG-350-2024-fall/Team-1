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

  const login = async (userType, credentials) => { // Exception handling example
    let endpoint, body;
    
    // Determine the endpoint and body based on userType
    if (userType === "staff") { // The login function acts as a facade for the different login endpoints
      endpoint = "http://localhost:5000/api/login";
      body = JSON.stringify({ username: credentials.username, password: credentials.password });
    } else if (userType === "patient") {
      endpoint = "http://localhost:5000/api/patient_login";
      body = JSON.stringify({ healthCareNumber: credentials.healthCareNumber });
    }
  
    try {
      const response = await fetch(endpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body,
      });
  
      if (response.ok) {
        setIsAuthenticated(true);
        setUserType(userType);
        navigate("/");
      } else if (userType === "patient") {
        setHealthCareNumber("");
      }
    } catch (error) {
      console.error("Login failed:", error);
    }
  
    // Clear credentials
    if (userType === "staff") {
      setUsername("");
      setPassword("");
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
        login,
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
