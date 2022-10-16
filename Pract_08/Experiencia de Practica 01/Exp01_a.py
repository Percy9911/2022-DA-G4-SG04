
array=[];
may=0;
men=9999;
cont=0;
while(cont<=5):
    num = int(input("Ingresa un numero: "));
    if(num > may):
        may=num;
    if(num < men):
        men=num;
    array.append(num);
    cont = cont+1;

print(array);
print(f'El numero mayor es: {may} ');
print(f'El numero menor es: {men} ');

    
    


