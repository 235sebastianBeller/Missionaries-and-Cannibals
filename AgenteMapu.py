from AgenteIA.AgenteBuscador import AgenteBuscador


class AgenteMapu(AgenteBuscador):

    def __init__(self):
        AgenteBuscador.__init__(self)
        self.acciones = None
        self.maxima_cantidad_pacificos=None
    def set_estado_inicial(self,estado_inicial):
        self.estado_inicial=estado_inicial
    def set_estado_meta(self,estado_meta):
        self.estado_meta=estado_meta
    def es_estado_fin_de_juego(self,estado):
        # Retorna True si no  existen mas pacificos que verdugos,
        # False en caso contrario
        return (estado[1]>estado[0]>0  or  estado[1]<estado[0]<self.maxima_cantidad_pacificos)
    
    def set_cantidad_maxima_pacificos(self,cantidad):
        self.maxima_cantidad_pacificos=cantidad
    
    def esta_estado_dentro_de_limites(self,estado):
        # Retorna True si el estado esta fuera de los limites 
        # y False en caso contrario.
        return estado[1]>=0 and estado[0]>=0  and  estado[1]<=self.maxima_cantidad_pacificos and estado[0]<=self.maxima_cantidad_pacificos
    def es_estado_valido(self,estado):
        # Retorna True si no es fin del juego 
        # y no esta fuera de los limites del juego. 
        # Caso contrario False.
        return (not self.es_estado_fin_de_juego(estado)) and self.esta_estado_dentro_de_limites(estado)
    def el_bote_esta_a_la_izquierda(self,estado):
        # Retorna True si el bote esta en la orilla izquierda, False en caso contrario
        return estado[2]
    def cambiar_direccion_del_bote(self,estado):
        # Retorna la direccion del bote en el proximo estado.
        # 0 es la orilla izquierda, 1 es la orilla derecha.
        return (estado[2]+1)%2
    def get_nuevo_estado(self,estado,acciones):
        # Retorna el nuevo estado que se obtiene al ejecutar
        # las posibles acciones en el estado actual.
        accion_mapu,accion_verdugo=acciones
        if self.el_bote_esta_a_la_izquierda(estado):
            accion_mapu*=-1
            accion_verdugo*=-1
        estado[0]+=accion_mapu
        estado[1]+=accion_verdugo
        estado[2]=self.cambiar_direccion_del_bote(estado)
        return estado
    def generar_hijos(self, e):
        # Retorna una lista de estados, que son los posibles estados
        # que se pueden alcanzar desde el estado actual.
        acciones_pacificos=[1,1,0,2,0]
        acciones_verdugos=[1,0,2,0,1]
        if not self.es_estado_valido(e):
            return []
        hijos=[
                self.get_nuevo_estado(e.copy(),acciones) 
                for acciones in zip(acciones_pacificos,acciones_verdugos)
                     if self.es_estado_valido(self.get_nuevo_estado(e.copy(),acciones))
               ]
        return hijos
