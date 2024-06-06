import React, { useState, useEffect } from 'react';
import axios from 'axios';

function AnonymizePage() {
  const [schema, setSchema] = useState({});
  const [selectedTables, setSelectedTables] = useState([]);
  const [selectedColumns, setSelectedColumns] = useState({});

  useEffect(() => {
    async function fetchSchema() {
      try {
        const response = await axios.get(`${process.env.REACT_APP_API_URL}/db/schema`, {
          headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` }
        });
        setSchema(response.data);
      } catch (error) {
        console.error('Error fetching schema', error);
      }
    }
    fetchSchema();
  }, []);

  const handleTableChange = (table) => {
    setSelectedTables((prev) =>
      prev.includes(table) ? prev.filter(t => t !== table) : [...prev, table]
    );
  };

  const handleColumnChange = (table, column) => {
    setSelectedColumns((prev) => ({
      ...prev,
      [table]: prev[table] ? (
        prev[table].includes(column) ? prev[table].filter(c => c !== column) : [...prev[table], column]
      ) : [column]
    }));
  };

  const handleSubmit = async () => {
    try {
      const response = await axios.post(`${process.env.REACT_APP_API_URL}/anonymize`, {
        tables: selectedTables,
        columns: selectedColumns
      }, {
        headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` }
      });
      console.log('Anonymization result', response.data);
    } catch (error) {
      console.error('Error anonymizing data', error);
    }
  };

  return (
    <div className="anonymize-page">
      <h2>Anonymize Data</h2>
      <div className="schema">
        {Object.entries(schema).map(([table, columns]) => (
          <div key={table}>
            <h3>
              <input
                type="checkbox"
                checked={selectedTables.includes(table)}
                onChange={() => handleTableChange(table)}
              />
              {table}
            </h3>
            <ul>
              {columns.map((column) => (
                <li key={column}>
                  <input
                    type="checkbox"
                    checked={selectedColumns[table]?.includes(column)}
                    onChange={() => handleColumnChange(table, column)}
                  />
                  {column}
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
      <button onClick={handleSubmit}>Anonymize</button>
    </div>
  );
}

export default AnonymizePage;
