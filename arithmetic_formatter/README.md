en la funcion propuesta recibire una lista de problemas aritmeticos, esta funcion regresa los problemas ordenados verticalmente lado a lado
esta funcion opcionalmente toma un segundo argumento que cuando su valor es verdadero debe de mostrar la respuesta de los problemas aritmeticos

reglas:

- limite de 5 problemas, si se excede de 5 mostrar el error "too many problems."
- los unicos operadores que se aceptan son el de suma y resta, multiplicacion y divicion deben mostrar un error, cualquier otro operador de los mencionados no necesitara ser evaluado
- cada numero (operando) debe contener solamente numeros, de lo contrario mostrara un error
- cada operando tiene un maximo de 4 digitos de largo, de lo contrario mostrara un error

informacion correcta

- tiene que haber un espepacio entre el operador y el mas largo de los dos operandos, el operador debe de estar en la misma linea que el segundo operando y ambos operandos mantendran el mismo orden en el que fueron proporcionados, el primero sera el de arriba y el segundo el de abajo
- los numeros deben de estar alineados a la derecha
- tiene que haber cuatro espacios entre cada problema
- tiene que haber guiones abajo de cada problema, los guiones los guiones tienen que tener el mismo largo de cada problema individualmente

segun la funcion arithmetic_arranger, debo de utilizar una funcion lambda con el argumento problem y utilizar la funcion map para iterar en la lista problems
