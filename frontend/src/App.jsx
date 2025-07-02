import { useState } from 'react'
import './App.css'
import {Routes, Route} from 'react-router-dom'
import Dashboard1 from './components/dashboard1'
import Dashboard2 from './components/Dashboard2'
import Navbar from './components/Navbar'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Navbar content={
        <Routes>
          <Route path='' element={<Dashboard1/>} />
          <Route path='/Dashboard2' element={<Dashboard2/>} />
        </Routes>
      }
      />
    </>
  )
}

export default App
