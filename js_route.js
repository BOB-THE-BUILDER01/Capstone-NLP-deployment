import fetch from 'node-fetch';

const PORT = 6969;
const complaint = {"complaint": ""}

const res = await fetch('http://127.0.0.1:' + PORT + '/predict', {
    method: 'POST',
    body: JSON.stringify(complaint),
    headers: { 'Content-Type': 'application/json' }
});

// Data in the form of a string. Use it :)
const data = await res.json();