sc = str(input('Ingrese un texto: '))
scb = str(input('Ingrese el texto que busca: '))
scr = str(input('Ingrese el texto reemplazo: '))

for s in range(len(sc)):
    lb = len(scb) + s
    if (sc[s:lb] == scb):
        sc = sc[:s] + scr + sc[lb:]
print(sc)
