Menu.js 

import { Outlet, Link } from "react-router-dom"; 

const Menu = () => { 

 return ( 

 <> 

 <nav> 

    <ul> 

        <li> 

            <Link to="/">Menu</Link> 

        </li> 

        <li> 

            <Link to="/Imagenes">Imagenes</Link> 

        </li> 

        <li> 

            <Link to="/Redes">Redes</Link> 

        </li> 

        <li> 

            <Link to="/Peliculas">Peliculas</Link> 

        </li> 

    </ul> 

 </nav> 

 <Outlet /> 

 </> 

 ) 

}; 

export default Menu; 