class Bote:

    # constructor
    def __init__(self, x, y, pos, imagen1, imagen2, superficie):
        self.x = x
        self.y = y
        self.pos = pos
        self.imagen1 = imagen1
        self.imagen2 = imagen2
        self.superficie = superficie
        self.ancho = 40
        self.altura = 100

    def mover(self, posx, posy, tipo_imagen):
        if self.pos in [2, 3]:
            x = posx + 20
        elif self.pos in [4, 5]:
            x = posx + 180
        if tipo_imagen == 'M':
            self.superficie.blit(self.imagen1, (x, posy - 50))
        elif tipo_imagen == 'C':
            self.superficie.blit(self.imagen2, (x, posy - 50))
    


