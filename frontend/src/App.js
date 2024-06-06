import React from 'react';
import { Route, Switch } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import DashboardPage from './pages/DashboardPage';
import AnonymizePage from './pages/AnonymizePage';
import ReportsPage from './pages/ReportsPage';
import AdminDashboardPage from './pages/AdminDashboardPage';

function App() {
  return (
    <div className="App">
      <Switch>
        <Route path="/login" component={LoginPage} />
        <Route path="/register" component={RegisterPage} />
        <Route path="/dashboard" component={DashboardPage} />
        <Route path="/anonymize" component={AnonymizePage} />
        <Route path="/reports" component={ReportsPage} />
        <Route path="/admin" component={AdminDashboardPage} />
      </Switch>
    </div>
  );
}

export default App;
