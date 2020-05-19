const express = require("express");
const mongoose = require("mongoose");
const path = require('path')
const bodyParser = require('body-parser')
const cookieParser = require('cookie-parser')
const config = require("./config/index.js")


const app = express();
let appWs = require('express-ws')(app)

app.use(bodyParser())
app.use(cookieParser());


app.use("/lab",require('./routes/lab'))




async function start(){
    try{
        app.listen(config.PORT);
    }
    catch (e) {
        console.log("Ошибка подключения к базе данных ", e.message)
        process.exit(1);
    }
}



start();