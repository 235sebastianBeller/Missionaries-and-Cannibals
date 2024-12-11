from AgenteMapu import AgenteMapu
from Rio import Rio

if __name__ == "__main__":
    juego = Rio()
    juan = AgenteMapu()
    juan.set_cantidad_maxima_pacificos(3)
    juego.insertar(juan)
    juego.run()
