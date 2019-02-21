#Entradas: Tres Numeros enteros
#Salidas: Promedio y Producto de los 3 Numeros o Mensaje de Error
#Restricciones: Tres Numeros enteros positivos

def quiz1(n1,n2,n3):
    if(n1+n2>n3):
        prom=(n1+n2+n3)/3
        produc=n1*n2*n3
        print("El promedio de los 3 numeros es: ",round(prom,2),"\nEl producto de los 3 numeros es: ",produc)
    else:
        print("La suma de los numeros ",n1," , ",n2," es menor a ",n3,"\nEntonces no se puede imprimir el rsultado")
