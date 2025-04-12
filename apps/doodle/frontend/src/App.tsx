import { useState } from 'react';
import './App.css';
import { FrappeProvider, useFrappeAuth } from 'frappe-react-sdk';
import { Login } from './pages/Login';
import { Home } from './pages/Home';
import { Routes, Route } from 'react-router';
import ProtectedRoute from '@/auth/ProtectedRoute';

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className='App flex flex-col items-center justify-center min-h-screen bg-gray-100'>
      <FrappeProvider
        socketPort={import.meta.env.VITE_SOCKET_PORT}
        siteName={import.meta.env.VITE_SITE_NAME}
      >
        <Routes>
          <Route path='/' element={<ProtectedRoute><Home /></ProtectedRoute>} />
          <Route path='/login' element={<Login />} />
        </Routes>
      </FrappeProvider>
    </div>
  );
}

export default App;
