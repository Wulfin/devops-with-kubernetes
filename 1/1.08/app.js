const express = require('express');
const app = express();

const PORT = process.env.PORT || 3000;

// Route to handle GET requests
app.get('/home', (req, res) => {
  // Simple HTML response
  const htmlResponse = `
    <html>
      <head>
        <title>Todo App</title>
      </head>
      <body>
        <h1>Welcome to Todo App!</h1>
        <p>This is a simple Todo application.</p>
      </body>
    </html>
  `;
  res.send(htmlResponse);
});

// kubectl port-forward deployment/todo-app 3000:3000 

app.listen(PORT, () => {
  console.log(`Server started in port ${PORT}`);
});
