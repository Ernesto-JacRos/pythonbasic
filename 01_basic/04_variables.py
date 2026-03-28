##
# 04 - variables
# las variables siorven para guardar datos en memoria 
# python e sun lenguaje de tipado dinamico y tipado fuerte 
##
my_name = 'devjacros'
print(my_name)


#tipado dinamico: el tipo de dato se determina en iempo de ejecucion 
#no tienes que declararlo explicitamente 
name = 'devjacros'
print(type(name))
name = 45 
print(type(name))
# Tipado fueste: Pytthon no realiza conversiones de tipo automaticas 
# print(10 + "45") lo toma como error no concaten en realidad 
# pones f par una fStrings como kotlin m y entre las llaves puedes hacer cual expresion que se pueda evalues
print(f"Hola my name is: {my_name}, {name} anhos")
# forma no recomendada pero que existe
name, age, city = 'devjacros', 36, 'CDMX'
print(name , age,  city)

# convensiones de nombre de varianles en python es snake_case
variable_name = 'ok' #snake_case
name = 'ok'
MiNameIs = 'ok' #PascalCase
mynameis = 'ok' #todojunto
my_name_iss_123 = 'ok' #norecomdado
MICONSTANTTE = 3.14
# EN OYTTHON NO HAY CONSTANTES PERO SE PUEDEN SIMULAR CON CLASES, USANDO EL UPER_CASE
# SE ENTIENDE QUE E SUAN CONSTANTE Y QUE NO DEBE DE CAMBIAR SIN SIMULARDA
# AUNQUE AUN ASI SE OUEDE REASIGANAR 


# TYPE ANOTATION 
#AUN QUE PUEDES DARELE UN TIPO A LA VARIABLE AUN ASI PUEDE CAMABIAR DE TIPO Y ENTOENCES 
# SOLO ES UN TYPE ANOTATION
is_black: bool = True # aqui es donde solo se ve que es una anotation solo para documentar
print(is_black)
is_black = True
print(f"es is_black jacros:  {is_black}") 

# para hacerlo afectivo podemos activar el typecheck del IDE



