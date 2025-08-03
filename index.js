
const express = require('express');
const path = require('path');
const app = express();

// Serve static files from the current directory
app.use(express.static(path.join(__dirname)));

// Health check endpoint for deployment
app.get('/health', (req, res) => {
    res.status(200).json({ status: 'healthy', timestamp: new Date().toISOString() });
});

// Main route
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Match page route
app.get('/match', (req, res) => {
    res.sendFile(path.join(__dirname, 'match.html'));
});

// Dashboard route
app.get('/dashboard', (req, res) => {
    res.sendFile(path.join(__dirname, 'dashboard_ui_layout.html'));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`AI Bonds running at http://localhost:${PORT}`);
});
