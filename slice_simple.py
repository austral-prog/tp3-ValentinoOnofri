def slice_simple():
    texto = "Awesome"
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.
    print (str(texto[0:3]).lower())
    print(texto[2:5]) #Tomo del 2 al 5, ya que la ultima no la incluye, por lo que debo agregar una posicion mas
    print(str(texto[0:4] + texto[-3:8]).lower())
# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
