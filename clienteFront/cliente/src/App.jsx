import React from 'react';
import Login from './pages/login';
import UsuarioPage from './pages/usuario';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Sidebar from './components/sideBarUser';
import AdminPage from './pages/admin';

function App() {
  const showSidebar = window.location.pathname !== '/login';

  return (
    <BrowserRouter>
      <div className="flex">
      {/* {showSidebar && <Sidebar />} */}
        <div className="flex-grow p-4">
          <Routes>
            <Route path='/admin' element={<AdminPage />} />
            <Route path='/login' element={<Login />} />
            <Route path='/index' element={<UsuarioPage />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
}

export default App;
