import React from "react";


const SectionHero = () => {
    return (
        <main>
  <section>
    <div class="bg-gray-100 sm:grid grid-cols-5 grid-rows-2 px-4 py-6 min-h-full lg:min-h-screen space-y-6 sm:space-y-0 sm:gap-4">

    <div class="h-96 col-span-4 bg-gradient-to-tr from-indigo-800 to-indigo-500 rounded-md flex items-center">
      <div class="ml-20 w-80">
      <h2 class="text-white text-4xl">Bienvenido nombre.usuario</h2>
      <p class="text-indigo-100 mt-4 capitalize font-thin tracking-wider leading-7">
        <ul>
            <li>Seccion.usuario</li>
            <li>Area.usuario</li>
            <li>Sucursal.usuario</li>
        </ul>
      </p>

      <a href="#" class="uppercase inline-block mt-8 text-sm bg-white py-2 px-4 rounded font-semibold hover:bg-indigo-100">Revisa tus tareas pendientes</a>
      </div>

    </div>
    <div class="h-96 col-span-1 mt-3 ">
      <div class="">
      </div>
      <div class="bg-white  rounded-md">

      <h1 class="text-center text-xl my-4  bg-white py-2 rounded-md border-b-2 cursor-pointer  text-gray-600">Ingreso nuevo trabajador</h1>
      <div class="bg-white rounded-md list-none space-y-2 m-4 text-center ">
        <li class="py-3 border-b-2"><a href="#" class="list-none  hover:text-indigo-600">Mis trabajadores</a></li>
        <li class="py-3 border-b-2"><a href="#" class="list-none  hover:text-indigo-600">Crear horario trabajador</a></li>
        <li class="py-3 border-b-2"><a href="#" class="list-none  hover:text-indigo-600">Ingresar tareas trabajador</a></li>
        <li class="py-3 border-b-2"><a href="#" class="list-none  hover:text-indigo-600">Ingresar archivos trabajador</a></li>
        <li class="py-3 "><a href="#" class="list-none border-b-2 hover:text-indigo-600">Ver solicitudes</a></li>
      </div>
      </div>
    </div>
    </div>

  </section>

</main>
        
    );
};

export default SectionHero;