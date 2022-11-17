var express = require('express'), fs = require('fs');
var router = express.Router();

var main = fs.readFileSync("./main.html");
var login = fs.readFileSync("./login.html");
var biblio = fs.readFileSync("./biblioteca.html");
var libro = fs.readFileSync("./libro.html");

router.get('/', function (req, res) {
    res.write(main);
})

router.get('/login', function (req, res) {
    res.write(login);
})

router.get('/biblioteca', function (req, res) {
    res.write(biblio);
})

router.get('/biblioteca/libro', function (req, res) {
    res.write(libro);
})

module.exports = router;