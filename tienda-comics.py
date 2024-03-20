import random;

productos = [];


opcion = 0;

ides = list(range(1,100))

almacenes = [];
almacenA = {
    "nombre" : "A",
    "cantidad": 50
    };

almacenes.append(almacenA);

almacenB = {
    "nombre" : "B",
    "cantidad": 50
    };

almacenes.append(almacenB);

almacenC = {
    "nombre" : "C",
    "cantidad": 50
}

almacenes.append(almacenC);

almacenD = {
    "nombre" : "D",
    "cantidad": 50
}

almacenes.append(almacenD);

while (opcion != 6):
    
    print("*** tienda de comics Superman ***");
    print("********************************** \f")
    print("1. Registrar producto\f2. Consultar todos los productos \f3. Consultar un producto\f4. Modificar unidades de un producto\f5. eliminar un producto\f6. Salir del programa");
    opcion = int(input("\fIngrese el numero del menu que pertenezca a la opcion que deseas realizar: "))
    if opcion == 1:
        
        producto = {};
        
        random.shuffle(ides);

        ide = ides.pop(0);
        
        producto["id"] = ide;
        producto["nombre"] = input("Ingrese el nombre del producto: ");
        producto["precio"] = int(input("Ingrese el precio unitario: $"));
        producto["ubicacion"] = input("ingrese la ubicacion del producto en la tienda (A,B,C,D): ").upper();
        producto["descripcion"] = input("Ingrese la descripcion del producto: ");
        producto["casa"] = input("Ingrese la casa a la que pertenece el producto: ");
        producto["pais"] = input("Ingrese el pais de origen del producto: ");
        producto["unidades"] = int(input("Ingrese el numero de unidades del producto: "));
        garantia = input("El producto cuenta con garantia extendida? si/no: ");
        if garantia == "si":
            producto["garantia"] = True;
        else:
            producto["garantia"] = False;

        for almacen in almacenes:
            if producto["ubicacion"] == almacen["nombre"]:
                if producto["unidades"] > almacen["cantidad"]:
                    print(f"\n El almacen {almacen["nombre"]} no permite esa cantidad de unidades");
                else:
                    print("\nProducto guardado\n")
                    almacen["cantidad"] = almacen["cantidad"] - producto["unidades"];
                    productos.append(producto)

    elif opcion == 2:
        
        garantia = "";
        for index,productoAuxiliar in enumerate(productos):
            if productoAuxiliar["garantia"] == True:
                
                garantia = "si"
            else:
                
                garantia = "no"
            print(f"\nProducto N°{index+1}\nId: {productoAuxiliar["id"]}\nTitulo: {productoAuxiliar["nombre"]}\nPrecio unitario: ${productoAuxiliar["precio"]}\nubicacion: {productoAuxiliar["ubicacion"]}\ndescripcion: {productoAuxiliar["descripcion"]}\ncasa: {productoAuxiliar["casa"]}\npais: {productoAuxiliar["pais"]}\nunidades: {productoAuxiliar["unidades"]}\ngarantia extendida: {garantia}\n");
        
    elif opcion == 3:
        
            garantia = "";
            encontrado=True;
            productoBuscado = input("Ingresa el nombre del producto a consultar: ");
        
            for productoAuxiliar in productos:
                if productoAuxiliar["garantia"] == True:
                    garantia = "si"
                else:
                    garantia = "no"
                if productoAuxiliar["nombre"] == productoBuscado :
                    
                    print(f"\nId: {productoAuxiliar["id"]}\nTitulo: {productoAuxiliar["nombre"]}\nPrecio unitario: ${productoAuxiliar["precio"]}\nubicacion: {productoAuxiliar["ubicacion"]}\ndescripcion: {productoAuxiliar["descripcion"]}\ncasa: {productoAuxiliar["casa"]}\npais: {productoAuxiliar["pais"]}\nunidades: {productoAuxiliar["unidades"]}\ngarantia extendida: {garantia}\n");
                    break;                
                else:
                    
                    encontrado = False;
            if encontrado is False:
                
                print("Producto no encontrado");
                
    elif opcion == 4:
        
            garantia = "";
            encontrado = True;
            productoBuscado = input("Ingresa el nombre del producto a modificar: ");
            for productoAuxiliar in productos:
                
                if productoAuxiliar["garantia"] == True:
                    
                    garantia = "si"
                else:
                    
                    garantia = "no"
                if productoAuxiliar["nombre"] == productoBuscado :
                    
                    print(f"\nId: {productoAuxiliar["id"]}\nTitulo: {productoAuxiliar["nombre"]}\nPrecio unitario: ${productoAuxiliar["precio"]}\nubicacion: {productoAuxiliar["ubicacion"]}\ndescripcion: {productoAuxiliar["descripcion"]}\ncasa: {productoAuxiliar["casa"]}\npais: {productoAuxiliar["pais"]}\nunidades: {productoAuxiliar["unidades"]}\ngarantia extendida: {garantia}\n");
                    nuevaCantidad = int(input("Ingrese la nueva cantidad de unidades: "));
                    if nuevaCantidad > productoAuxiliar["unidades"]:
                        print("\nLa cantidad de unidades ingresadas no puede superar a la que ya está almacenada\n");
                        break;
                    else:
                        
                        aumentoAlmacen = nuevaCantidad-productoAuxiliar["unidades"];
                        for almacen in almacenes:
                            if almacen["nombre"] == productoAuxiliar["ubicacion"]:
                                almacen["cantidad"] += aumentoAlmacen;
                        productoAuxiliar["unidades"] = nuevaCantidad;
                        print("Se modificaron las unidades del producto");
                else:
                    encontrado = False;
            if encontrado is False:
                print("Producto no encontrado");
    elif opcion == 5:
        
        productoBuscado = input("ingresa el nombre del producto a eliminar: ")
        for index,productoAuxiliar in enumerate(productos):
                if productoAuxiliar["garantia"] == True:
                    garantia = "si"
                else:
                    garantia = "no"
                if productoAuxiliar["nombre"] == productoBuscado :
                    
                    confi = input(f"Estas seguro de eliminar el producto {productoAuxiliar["nombre"]} si/no: ");
                    if confi == "si":
                        for almacen in almacenes:
                            if productoAuxiliar["ubicacion"] == almacen["nombre"]:
                                almacen["cantidad"] += productoAuxiliar["unidades"];
                                productos.pop(index)
                        print("\nProducto eliminado\n");
                    else:
                        print("\nProducto no eliminado\n")
    else:
        print("\nIngrese una opcion valida\n");