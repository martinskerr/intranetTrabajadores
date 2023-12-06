import React from 'react';
import Sidebar from '../components/sideBarUser';

const Documentos = () => {
  return (
    <div className="flex">
      <aside className="w-1/4 p-4">
        <Sidebar/>
      </aside>
      <main className="w-3/4 p-4">
        {/* Contenido del cuerpo de la página */}
      </main>
    </div>
  );
};

export default Documentos;