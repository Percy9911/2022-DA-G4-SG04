var express = require('express');
var router = express.Router();

router.get('/', function (req, res) {
    res.send('Pagina Principal');
})

router.get('/login', function (req, res) {
    res.send('Inicio Sesion');
})

router.get('/productos', function (req, res) {
    res.send('Catalogo de Productos');
})

router.get('/productos/compra', function (req, res) {
    res.send('Aqui puedes comprar tus productos');
})

module.exports = router;