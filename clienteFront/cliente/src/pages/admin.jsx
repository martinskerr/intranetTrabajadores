import React from 'react';
import Sidebar from '../components/sideBarUser';
import MainWidget from '../components/mainWidget';


const adminPage = () => {
    (
        <div className="flex h-screen bg-gray-200">
            <Sidebar />
            <MainWidget />
        </div>
    )
};