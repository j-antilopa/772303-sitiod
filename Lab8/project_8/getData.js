const morgan = require('mongoose-morgan');
module.exports = [
    morgan(
        {
            connectionString: 'mongodb://localhost:27017/Lab_8',        //строка подключения к базе данных
            collection: 'log_URL',                                      //строка подключения к коллекции
        },
        {},                                                     //Выборка по значениям(не используется)
        ':url :total-time :response-time')]                      //формат выводимых данных
