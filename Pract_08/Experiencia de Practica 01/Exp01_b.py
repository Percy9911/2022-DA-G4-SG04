def primos(num):
    if num < 2: 
       return ("No es primo")
    for i in range(2, num):
       if num % i == 0: 
            return ("No es primo")
    return ("Es primo")

    
def menu():
    print("########### - MENU DE OPCIONNES - ##############");
    print("1.Comprobar numeros primos");
    print("2.Salir");
    opc = int(input("Selecciona una opcion: "));
    print("################################################");
    if (opc==1):
        cant=int(input("Cuantos numeros va evaluar?: "));
        cont=0
        for i in range(cant):
            num=int(input("Ingrese el numero: "));
            cont=cont+1;
            print(primos(num));
        menu();
            
                    
    elif(opc==2):
        exit();

def main():
    menu();

if __name__ == "__main__":
    main();


              
    
