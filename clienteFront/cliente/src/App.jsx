import Login from './pages/login'
import UsuarioPage from './pages/usuario'
import './App.css'
import {BrowserRouter, Routes, Route} from 'react-router-dom'

function App() {
  
  return (
  <BrowserRouter>


    <Routes>
      <Route path='/login' element={<Login/>}/>
      <Route path='/index' element={<UsuarioPage/>}/>

    </Routes>
  
  </BrowserRouter>



  )
}

export default App
