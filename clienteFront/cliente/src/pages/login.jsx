import React from 'react';

const Login = () => {
  return (
    <div className=" min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full space-y-8">
        <div>
            <h1 className=" text-center mb-16 text-3xl font-extrabold text-gray-900">
            Cooperative Group
          </h1>
          <h2 className=" py-6 text-center text-3xl font-extrabold text-gray-900 border rounded-md">
            Bienvenido a tu Oficina Virtual
          </h2>
          <h3 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
            Iniciar Sesión
          </h3>
        </div>
        <form className="mt-8 space-y-6" action="#" method="POST">
          <input type="hidden" name="remember" defaultValue="true" />
          <div className="-space-y-px rounded-md shadow-sm">
            <div className='my-6'>
              <label htmlFor="rut" className="sr-only">
                Rut
              </label>
              <input
                id="email-address"
                name="rut"
                type="rut"
                autoComplete="rut"
                required
                className="appearance-none rounded-lg relative block w-full px-3 py-4 border border-gray-300 placeholder-gray-500 text-gray-900  focus:outline-none focus:ring-primary focus:border-primary focus:z-10 sm:text-sm"
                placeholder="Rut, sin puntos y con guion (Ejemplo: 12345678-9)"
              />
            </div>
            <div>
              <label htmlFor="password" className="sr-only">
                Contraseña
              </label>
              <input
                id="password"
                name="password"
                type="password"
                autoComplete="current-password"
                required
                className="appearance-none rounded-lg relative block w-full px-3 py-4 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-primary focus:border-primary focus:z-10 sm:text-sm"
                placeholder="Contraseña"
              />
            </div>
          </div>


          <div className=' flex justify-center'>
            <button
              type="submit"
              className="duration-700 group relative flex justify-center py-2 px-4 text-white border border-inherit bg-blue-700 hover:bg-blue-500 rounded-lg"
            >
              Iniciar Sesión
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Login;