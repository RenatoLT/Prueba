#Renato Lavanderos 003D
from random import *
kwh=[5.9, 0.8, 4.0, 4.5, 2.1]
gasto=[]
total=0
while True:
    try:
        pers=int(input("¿Cuantas personas viven en su casa?\n"))
        if 0<pers<6:
            break
        else:print("Ingrese un numero entre 1 y 5")
    except ValueError:
        print("Ingrese un numero")
for i in range(0,pers):
    gasto.append(228)
    for j in range(1,30):
        artes=randint(0,3)
        for k in range(artes):
            indice=randint(1,4)
            gasto[i]+=kwh[indice]
for l in range(pers):
    print("Gastos persona",str(l+1)+":",round(gasto[l],1),"kWh.")
    total+=gasto[l]
print("El gasto total mensual es:",round(total,1),"kWh")
