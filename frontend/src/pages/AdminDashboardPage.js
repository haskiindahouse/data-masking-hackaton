import React, { useState } from 'react';
import axios from 'axios';

function AdminDashboardPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [users, setUsers] = useState([]);

  const handleCreateUser = async (event) => {
    event.preventDefault();
    try {
      await axios.post(`${process.env.REACT_APP_API_URL}/admin_dashboard/create-user`, {
        username,
        password
      }, {
        headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` }
      });
      fetchUsers();
    } catch (error) {
      console.error('Error creating user', error);
    }
  };

  const handleDeleteUser = async (username) => {
    try {
      await axios.delete(`${process.env.REACT_APP_API_URL}/admin_dashboard/delete-user`, {
        data: { username },
        headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` }
      });
      fetchUsers();
    } catch (error) {
      console.error('Error deleting user', error);
    }
  };

  const fetchUsers = async () => {
    try {
      const response = await axios.get(`${process.env.REACT_APP_API_URL}/admin_dashboard/users`, {
        headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` }
      });
      setUsers(response.data);
    } catch (error) {
      console.error('Error fetching users', error);
    }
  };

  return (
    <div className="admin-dashboard-page">
      <h2>Admin Dashboard</h2>
      <form onSubmit={handleCreateUser}>
        <div>
          <label>Username</label>
          <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
        </div>
        <div>
          <label>Password</label>
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </div>
        <button type="submit">Create User</button>
      </form>
      <div className="user-list">
        <h3>User List</h3>
        <ul>
          {users.map((user) => (
            <li key={user.username}>
              {user.username}
              <button onClick={() => handleDeleteUser(user.username)}>Delete</button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default AdminDashboardPage;
