import "../../styles/login.css";
import { useState } from "react";
import useAuth from "../../hooks/useAuth";

function LoginForm() {
    const { login } = useAuth();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const [errors, setErrors] = useState({});
    const [showPassword, setShowPassword] = useState(false);

    const handleSubmit = async (event) => {
        event.preventDefault();

        const newErrors = {};

        if ( !email.trim() || !email.includes("@") ) {
            newErrors.email = "Ingresa un email valido"
        }

        if (!password.trim()) {
            newErrors.password = "La contraseña es obligatoria";
        }

        setErrors(newErrors);

        if (Object.keys(newErrors).length > 0) {
            return;
        }

        try {
            const data = await login(email, password);

            console.log('login exitoso: ', data);
        
        } catch (error) {
            console.log('Error en login: ', error);
        }
    };

    return (
        <form className='login-form' onSubmit={handleSubmit}>
            <h1 className="login-title">Iniciar sesión</h1>

            <div className="form-group">
                <label htmlFor="email">Email</label>
                <input
                    type="email"
                    id="email"
                    name="email"
                    placeholder="Ingrese email"
                    value={email}
                    onChange={(event) => setEmail(event.target.value)}
                />
                {errors.email && (
                    <span className="input-error">
                        {errors.email}
                    </span>
                )}
            </div>

            <div className="form-group">
                <label htmlFor="password">Contraseña</label>
                <div className="password-input">
                    <input
                        type={showPassword ? "text" : "password"}
                        id="password"
                        name="password"
                        placeholder="Ingrese su contraseña"
                        value={password}
                        onChange={(event) => setPassword(event.target.value)}
                    />
                    <button
                        type="button"
                        className="toggle-password"
                        onClick={(event) => setShowPassword(!showPassword)}
                    >
                        {showPassword ? "◉" : "👁"}
                    </button>

                </div>

                {errors.password && (
                    <span className="input-error">
                        {errors.password}
                    </span>
                )}

            </div>

            <button type="submit">Ingresar</button>

            <a href="#">Recuperar usuario o clave</a>
            <a href="#">Registrarse</a>
        </form>
    );
}

export default LoginForm;