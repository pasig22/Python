# Ejercicios de repaso: Introducción a python
---

## 1. Elaborar un programa para evaluar una palabra si es palíndromo o  no.
```javascript
palabra = "malayalam"
rev = palabra[::-1]
if palabra == rev:
	print("Si")
else
	print("No")
```
## 2. Obtener el factorial de un número
##### El factorial de un número es el producto de los números enteros positivos, de uno hasta n.

formula:

n! = n(n-1)
```python
def factorial(n):
	if n == 1 or n == 0:
    	return 1
    else:
    	return n * factorial (n - 1) # en este punto se efectua la recursión
num = 20
print("El factorial de ", num, "es: ", factorial(num) )
```

## 3. Contar digitos de un número dado
```python
 num = int(input("Ingresa un número: "))
 count = 0
 i = num

 while (i > 0):
 	count = count + 1
    i = i // 10

print(f"El número de digitos de {num}: ", count)
```

## 4.- Tablas de multiplicación
```python
num = int(input("Ingresa el número para la tabla de multiplicación: "))

print("Tabla de multiplicar", num)

for i in range (1, 11):
	print (num, 'x', i, '=', num * i)
```

## 5. Convertir kilómetros a miles
1 kilómetro es igual a 0.621371 miles
```python
km = float(input("Ingresa los kilómetros a convertir: "))

convertKmToMiles(km)

def convertKmToMiles(km):
	const = 0.621371
    return miles = km * const
```

## 6. Encontrar dentro de una lista el número más grande
```python
list = [100, 1000, 20, 10000, 30, 40, 3000000, 2, 1]

maxNum = list[0]
for i in list:
	if i > maxNum:
    	maxNum = i
print("El número más grande es: ", maxNum)
```

## 7. Número fibonacci- El algoritmo más común y mínimo para generar la secuencia de Fibonacci requiere que codifique una función recursiva que se llama a sí misma tantas veces como sea necesario hasta que calcule el número
```python
def fib(n):
    if n <= 0:
        print("Valor incorrecto")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input("Ingresa un número: "))
fibVlr = fib(n)
print("El fibonacci de:", n, "es", fibVlr)
```

## 8. Calculadora con python
```python
def menu():
	print("Calculadora con python"\n)
    print("Elija su opción: "\n)
    print("1 - suma\n2 - resta\n3 - multiplicación\n4 - División")
menu()

opcDeseada = int(input("Ingrese su opción": ))
v1 = float(input("Ingrese el primer valor: "))
v2 = float(input("Ingrese el segundo valor: "))

def suma(v1,v2):
	suma = v1 + v2
    print("La suma es: ",suma)

def resta(v1,v2):
	resta = v1 - v2
    print("La resta es: ",resta)

def multi(v1,v2):
	multi = v1 + v2
    print("La multiplicación es: ",multi)

def div(v1,v2):
	div = v1 - v2
    print("La división es: ",div)

if opcDeseada == 1:
	suma(v1,v2)
elif opcDeseada == 2
	resta(v1,v2)
elif opcDeseada == 3
	multi(v1,v2)
elif opcDeseada == 4
	div(v1,v2)
else:
	print("Opción invalida")

cerrar = int(input("Ingrese 1 para reiniciar o cualquier tecla para cerrar: "))
if cerrar == 1:
	python = sys.executable
    os.execl(python,python, * sys.argv)
else:
	print("Gracias, hasta pronto")
    exit()
```