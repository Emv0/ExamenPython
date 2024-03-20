import random;

print("***Preparando salpicon***");
print("*************************");

cantidadFrutas = int(input("Ingresa la cantidad de frutas necesarias para el salpicon: "));

frutas = [];


totalSalpicon = 0;
for i in range(0 , cantidadFrutas):
    
    fruta = {};
    totalFruta = 0;
    
    ide = random.randint(1,100);
    print("");
    fruta["nombre"] = input(f"Ingresa el nombre de la fruta {i+1}: ");
    fruta["precioUnitario"] = int(input("Ingresa el precio unitario de la fruta: $"));
    fruta["cantidad"] = int(input("Ingresa la cantidad de la fruta: "));
    
    totalFruta = fruta["precioUnitario"] * fruta["cantidad"];
    
    frutas.append(fruta);
    
    totalSalpicon += totalFruta;

for i in range(len(frutas)-1):
    for j in range(len(frutas)-1):
        if frutas[j]["precioUnitario"] < frutas[j+1]["precioUnitario"]:
            aux = frutas[j];
            frutas[j] = frutas[j+1];
            frutas[j+1] = aux;

print(f"\nEl costo total del salpicon es: ${totalSalpicon}");


print("\nFrutas ordenadas de mayor a menor precio \n")
for fruta in frutas:
    print(f"Fruta: {fruta["nombre"]} - Precio: ${fruta["precioUnitario"]}");
print("");

print(f"La fruta mas barata es {frutas[cantidadFrutas-1]["nombre"]}, precio: ${frutas[cantidadFrutas-1]["precioUnitario"]}")
