Algoritmo siguiemiento_pacientes
	definir listapacientes Como Entero
	listapacientes <- 0
	Definir opcion Como Entero
	Mientras Verdadero Hacer
		Escribir "menu principal"
		Escribir  "1 registrar el paciente "
		Escribir "2 progrmar cita"
		Escribir "3  actualizar la informacion"
		Escribir "4 consultar informacion del pasiente"
		Escribir " 5 salir"
		leer opcion
		Segun opcion Hacer
			1:
				Escribir "registrar al paciente"
				Definir edad Como entero
				Definir telefono Como entero
				Definir nombre Como Caracter
				Escribir "PORPOCIONARR LA edad DEL PACIENTE"
				leer edad
				Escribir " porpociona el telefono del paciente"
				Leer telefono
				Escribir "porpociona el nombre del paciente"
				leer nombre
				listapacientes <- listapacientes + 1
			2:
				
				Escribir "actualizar informacion"
				Escribir "selecccionar paciente"
				Definir paciente_seleccionado Como Entero
				Leer paciente_seleccionado
				Escribir "nuevo nombre"
				Leer nombre 
				Escribir "nueva edad"
				leer edad
				Escribir "nuevo telefono"
				Leer telefono 
				Escribir "informacion actualizada"
				
				
			3:
				Escribir "programar cita"
				Leer cita
				Escribir "seleccionar al paciente"
				Leer  paciente_seleccionado
				definir  Fecha como entero
				definir hora como entero
				Escribir "ingrese la fecha  del paciene"
				Escribir "la cita : /   /    /   :"
				Escribir "ingrese la hora : /  /  :"
				Escribir "cita progrmada"
			4:
				Escribir "cita programada"
				Escribir "consultar informacion"
				Escribir "seleccionar al paciente"
				leer paciente_seleccionado
				Escribir "Datos del paciente y citas programas"
				Escribir "saliendo del programa"
				
		Fin Segun
	Fin Mientras
	
FinAlgoritmo
