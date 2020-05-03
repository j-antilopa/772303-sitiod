const express = require('express');
const app = express();
const port = 3000;

app.use(require('./getData.js')); //промежуточный обработчик событий для запросов на все URL

app.listen(port); //метод прослушивания порта

console.log('Server run on port ' + port);
