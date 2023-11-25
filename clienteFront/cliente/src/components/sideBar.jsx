import React from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';

const Sidebar = () => {
  return (

  <Router>  

      <Route path="/inicio" component={UsuarioPage} />
      <Route path="/solicitudes" component={Solicitudes} />
      <Route path="/documentos" component={Documentos} />
      <Route path="/directorio" component={Directorio} />

  </Router> 
  );
};

export default Sidebar;