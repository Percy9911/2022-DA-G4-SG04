var arreglo = [];
var nume = 0;

function nuevaVentana(){
    document.getElementById("titulo").innerHTML = "Abrir nueva ventana";
    if (window.confirm("Ir a youtube")) {
        window.open('https://youtube.com/');
    }
}

function ingresoNum(){
    nume = window.prompt();
    arreglo.push(nume);
    return arreglo;
}

function eleArr(arre){
    let sc = '';
    for(i=0; i<arre.length; i++){
        sc += arre[i] + ' ';
    }
    return sc;
}

function mostrarnum(){
    document.getElementById("resultado").innerHTML = eleArr(arreglo);
}
