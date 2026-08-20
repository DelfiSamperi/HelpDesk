import { BrowserRouter, Routes, Route } from 'react-router-dom';

import Login from '../pages/Login';
import Dashboard from '../pages/Dashboard';
import Tickets from '../pages/Tickets';
import TicketDetail from '../pages/TicketDetail';
import Users from '../pages/Users';
import NotFound from '../pages/NotFound';

import ProtectedRoute from './ProtectedRoute';
import MainLayout from '../layouts/MainLayout';

function AppRouter() {
    return (
        <BrowserRouter>
            <Routes>
                {/*Ruta publica*/}
                <Route path='/login' element={<Login />} />

                {/*Rutas protegidas */}
                <Route element={<ProtectedRoute />}>
                    <Route element={<MainLayout />}>
                        <Route path='/dashboard' element={<Dashboard />} />
                        <Route path='/tickets' element={<Tickets />} />
                        <Route path='/tickets/:id' element={<TicketDetail />} />
                        <Route path='/users' element={<Users />} />
                    </Route> 
                </Route>

                {/*Ruta inexistente */}
                <Route path='*' element={<NotFound />} />
            </Routes>
        </BrowserRouter>
    )
};

export default AppRouter;