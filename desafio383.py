from enum import Enum

# Definimos el Enum de idiomas
class Idiomas(Enum):
    ESPAÑOL = 'es'
    INGLES = 'en'
    FRANCES = 'fr'
    ALEMAN = 'de'
    ITALIANO = 'it'

# Función que devuelve un saludo en el idioma dado
def saludar(idioma: Idiomas) -> str:
    if idioma == Idiomas.ESPAÑOL:
        return "¡Hola!"
    elif idioma == Idiomas.INGLES:
        return "Hello!"
    elif idioma == Idiomas.FRANCES:
        return "Bonjour!"
    elif idioma == Idiomas.ALEMAN:
        return "Hallo!"
    elif idioma == Idiomas.ITALIANO:
        return "Ciao!"
    else:
        return "Idioma no soportado."

# Ejemplo de uso
print(saludar(Idiomas.ESPAÑOL))   # ¡Hola!
print(saludar(Idiomas.INGLES))    # Hello!
print(saludar(Idiomas.FRANCES))   # Bonjour!
