// server.js
const express = require('express');
const path = require('path');

const app = express();

app.use(express.static(path.join(__dirname, 'html&css','index.html')));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'html&css', 'index.html'));
});

app.get('html &css/visualize', (req, res) => {
    // Fetch data from SQLite and pass to visualise.html
    const sqlite3 = require('sqlite3').verbose();
    const db = new sqlite3.Database('/noticedb.db');

    db.all('SELECT * FROM users', (err, rows) => {
        if (err) {
            console.error(err.message);
        }
        res.render(path.join(__dirname,'html&css', 'visualize.html'), { users: rows });
    });

    db.close();
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
