const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const matchmaker = require('./matchmaker');

const app = express();
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, '../client')));

app.post('/match', (req, res) => {
  const { mood, interests } = req.body;
  const match = matchmaker.scoreMatch({ mood, interests });
  res.json({ match });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`AI Bonds Matchmaker running on http://localhost:${PORT}`);
});
