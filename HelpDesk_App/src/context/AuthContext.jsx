import { createContext, useContext, useState } from "react";
import AuthService from "../services/AuthService";

const AuthContext = createContext();

export function AuthProvider({ children }) {
    const [token, setToken] = useState(
        localStorage.getItem("access_token")
    );

    const [user, setUser] = useState(() => {
        const storedUser = localStorage.getItem("user");

        return storedUser ? JSON.parse(storedUser) : null;
    });

    const login = async (email, password) => {
        const data = await AuthService.login(email, password);

        localStorage.setItem("access_token", data.access_token);
        localStorage.setItem("user", JSON.stringify(data.user));

        setToken(data.access_token);
        setUser(data.user);

        return data;
    };

    const logout = () => {
        localStorage.removeItem("access_token");
        localStorage.removeItem("user");

        setToken(null);
        setUser(null);
    };

    const isAuthenticated = Boolean(token);

    return (
        <AuthContext.Provider
        value={{
            token,
            user,
            isAuthenticated,
            login,
            logout,
        }}
        >
            {children}
        </AuthContext.Provider>
    );
}

export default AuthContext;