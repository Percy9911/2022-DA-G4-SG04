
let Car1 = new Object();
let Car2 = new Object();
let Car3 = new Object();

let pares = [2,4,6,8,10];
let letras = new Array('a','b','c','d','e');
let obj = [Car2,Car3];

pares.push(16);
letras.unshift('G');
obj[0] = Car1;

console.log(pares);
console.log(letras);
console.log(obj);

function mostrar(X) {
    console.log(X);
}

pares.forEach(function (pares){
    mostrar(pares);
})

letras.push('B');
obj.pop();
letras.unshift('f');
pares.shift();
console.log('posicion -> '+letras.indexOf('d'));
console.log(pares);
console.log(letras);
console.log(obj);

for(let i =0; i <pares.length;i++){
    console.log(i+" -> ",pares[i]);
}

let index=0;
letras.forEach(element => {
    console.log("Index ",index++, "valor: ",element)
});

let ind = 0;
while (true) {
    if (ind == pares.length)
    break
    console.log("I", ind, " : ", pares[ind]);
    ind++;
}

let e = 0;
do{
    if (e == letras.length)
    break
    console.log(e, "- ", letras[e]);
    e++;
    }while(true);