import { useRouteError } from "react-router-dom";
import { Link } from "react-router-dom";
import './Error.css';

export default function Error() {
    const error = useRouteError();
    let errorMessage = "Lo siento, ha ocurrido un error inesperado";
    
    // Manejo de diferentes tipos de errores
    if (error.status === 404) {
        errorMessage = "Lo siento, la página que buscas no se encuentra";
    } else if (error.status === 500) {
        errorMessage = "Lo siento, algo salió mal en nuestros servidores";
    }
    
    // Estilos más atractivos
    return (
        <div id="error-page">
            <h1>¡Oops!</h1>
            <p>{errorMessage}</p>
            <p>
                <i>
                    {error.statusText || error.message}
                </i>
            </p>
            <Link to='/'>Volver al inicio</Link>
        </div>
    );
}