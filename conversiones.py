#temperatura
def celsius_a_farenheit(celsius: int | float) -> float:
    return (celsius * 9 / 5) + 32

def farenheit_a_celsius(farenheit: int | float) -> float:
    return (farenheit - 32) * 5 / 9

#Distancia

def kilometros_a_millas(kilometros: int | float) -> float:
    return kilometros * 0.621371

def millas_a_kilometros(millas: int | float) -> float:
    return millas / 0.621371

#Masa
def kilogramos_a_libras(kilogramos: int | float) -> float:
    return kilogramos * 2.20462

def libras_a_kilogramos(libras: int | float) -> float:
    return libras / 2.20462
