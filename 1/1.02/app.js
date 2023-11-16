const express = require('express');
const app = express();

const PORT = process.env.PORT || 3000; // Default port is 3000 if PORT environment variable is not set

app.listen(PORT, () => {
  console.log(`Server started in port ${PORT}`);
});
