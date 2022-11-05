class Juego (object):
    
    def __init__(self, fecha, estado, equipos, scores):
        self.fecha = fecha
        self.estado = estado
        self.equipos = equipos
        self.scores = scores


    def get_id_home_team(self):
        local = self.equipos["home"]
        id_home = int(local["id"]) - 1

        return id_home    
    
    
    def get_id_visitor_team(self):
        visitante = self.equipos["visitors"]
        id_visitors = int(visitante["id"]) - 1
        
        return id_visitors 


    def imprimir_imagen_home(self):
        return "/static/images/logos/imagen_equipo_" + str(self.get_id_home_team()) + ".png"


    def imprimir_imagen_visitor(self):
        return "/static/images/logos/imagen_equipo_" + str(self.get_id_visitor_team()) + ".png"

    
    def partido_en_juego(self):
        if self.estado["long"] == "In Play":
            return True
        else:
            return False

    
    def partido_terminado(self):
        if self.estado["long"] == "Finished":
            return True
        else:
            return False

    
    def score_home(self):
        return int(self.scores["home"]["points"])


    def score_visitor(self):
        return int(self.scores["visitors"]["points"])

    
    def get_hour(self):
        hour = self.fecha["start"]
        hour = hour[11:16]
        hour += " UTC"

        return hour

        