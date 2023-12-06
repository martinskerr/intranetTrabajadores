import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Directorio from '../pages/directorio';
import Documentos from '../pages/documentos';
import Solicitudes from '../pages/solicitudes';
import UsuarioPage from '../pages/usuario';
const Sidebar = () => {
  return (
    <BrowserRouter>

      <Router>  
        <Routes>
          <Route path="/inicio" element={<UsuarioPage/>} />
          <Route path="/solicitudes" element={<Solicitudes/>} />
          <Route path="/documentos" element={<Documentos/>} />
          <Route path="/directorio" element={<Directorio/>} />
        </Routes>
      </Router> 

  </BrowserRouter>
  );
};

export default Sidebar;