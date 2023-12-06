import React from 'react';
import Sidebar from '../components/sideBar';
import MainWidget from '../components/mainWidget';


const adminPage = () => {
    (
        <div className="flex h-screen bg-gray-200">
            <Sidebar />
            <MainWidget />
        </div>
    )
};