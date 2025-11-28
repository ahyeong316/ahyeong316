// server.js
const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const html = `
<!doctype html>
<html>
<head><meta charset="utf-8"><title>Simple Node Server</title></head>
<body>
  <h1>Hello from Node.js!</h1>
  <p>현재 시간: ${new Date().toLocaleString()}</p>
</body>
</html>`;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/html; charset=utf-8');
  res.end(html);
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
