var express = require('express');

var app = express();

const middleware = function (req, res, next) {
    console.log('ejecutando el middleware mientras llega petición');
    next();
};

app.use(middleware);

app.get('/', function (req, res) {
    setTimeout(function () {
        res.send('Llegó petición al servidor');
    }, 5000);
})

app.listen(3000, function () {
    console.log('servidor en escucha');
});