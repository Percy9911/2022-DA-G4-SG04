/*WINDOW*/
function verWindow (){
    let result = '';
    for(let i in window){
        if(window.hasOwnProperty(i)){
            result += i +  ' = ' + window[i]+'\n';
        }
    }
    return(result);
}

console.log(verWindow());

function usoWindow (){
    if (window.confirm("Ir a catolica")) {
        window.open('https://www.ucsm.edu.pe/');
      }
    else{
        r = window.prompt();
        encode = window.atob(r);
        console.log(encode);
    }
}
usoWindow();

/*ARRAY*/

const arr = ["A","B","C","D"];

function verArray (arreglo){
    let result = '';
    for(let i in arreglo){
        if(arreglo.hasOwnProperty(i)){
            result += i +  ' = ' + arreglo[i]+'\n';
        }
    }
    return(result);
}
console.log(verArray(arr));

function usoArray (arreglo){
    arreglo.push("E");
    arreglo.unshift("Prim");
    delete arreglo[2];
    return arreglo;
}
console.log(verArray(usoArray(arr)));

/*NUMBER*/

let n = Number('324');
function verNumber (num){
    console.log(num);
}
verNumber(n);

function usoNumber(num){
    r = '';
    if (Number.isInteger(num)){
        r += 'En int';
    }
    else{
        r+= 'no es int';
    }
    if (Number.isNaN){
        r += '- es NaN';
    }
    else {
        r += '- no es NaN';
    }
    return r;
}
console.log(usoNumber(n));