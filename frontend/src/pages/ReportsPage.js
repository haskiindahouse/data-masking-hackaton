import React, { useState } from 'react';
import axios from 'axios';

function ReportsPage() {
  const [reportType, setReportType] = useState('summary');
  const [dateRange, setDateRange] = useState({ start: '', end: '' });
  const [report, setReport] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.get(`${process.env.REACT_APP_API_URL}/reports/generate`, {
        params: {
          reportType,
          dateRange
        },
        headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` }
      });
      setReport(response.data);
    } catch (error) {
      console.error('Error generating report', error);
    }
  };

  return (
    <div className="reports-page">
      <h2>Generate Reports</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Report Type</label>
          <select value={reportType} onChange={(e) => setReportType(e.target.value)}>
            <option value="summary">Summary</option>
            <option value="detailed">Detailed</option>
          </select>
        </div>
        <div>
          <label>Date Range Start</label>
          <input
            type="date"
            value={dateRange.start}
            onChange={(e) => setDateRange({ ...dateRange, start: e.target.value })}
          />
        </div>
        <div>
          <label>Date Range End</label>
          <input
            type="date"
            value={dateRange.end}
            onChange={(e) => setDateRange({ ...dateRange, end: e.target.value })}
          />
        </div>
        <button type="submit">Generate Report</button>
      </form>
      {report && (
        <div className="report-result">
          <h3>Report Result</h3>
          <pre>{JSON.stringify(report, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default ReportsPage;
