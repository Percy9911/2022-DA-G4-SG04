var http = require('http');

var server = http.createServer();

let age = 20
let name = 'Elliot'

function verEdad(petic, resp) {
    resp.writeHead(200, { 'content-type': 'text/plain' });
    if (age >= 18) {
        resp.write("Hola " + name + " eres mayor de edad")
    } else {
        console.write("Hola " + name + " eres menor de edad")
    }
    resp.end();
}

server.on('request', verEdad);

server.listen(5000, function () {
    console.log('Aplicacion en el puerto 5000');
});