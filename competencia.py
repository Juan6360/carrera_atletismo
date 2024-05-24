import random
import pygame, sys

probabilidades = {
    "USA": 0.20,
    "Etiopía": 0.18,
    "Jamaica": 0.15,
    "Kenia": 0.13,
    "Polonia": 0.11,
    "Holanda": 0.09,
    "Francia": 0.07,
    "Bélgica": 0.07
}

tiempos_totales = {pais: 0 for pais in probabilidades}

carriles = [1, 2, 3 ,4 , 5, 6, 7, 8]

velocidad_vuelta = {
    "USA": [], 
    "Etiopía": [],
    "Jamaica": [],
    "Kenia": [],
    "Polonia": [],
    "Holanda": [],
    "Francia": [],
    "Bélgica": []
}

print("¡Comienza la competencia!")
print("Carriles asignados a los equipos:")
for pais, carril in zip(probabilidades.keys(), carriles):
    print(f"{pais} en el carril {carril}")

for vuelta in range(4):
    print(f"\nInicio de la vuelta {vuelta+1}:")
    for pais in probabilidades:
        
        if random.random() <= probabilidades[pais]:
            tiempo_vuelta = random.uniform(40, 60)
            velocidad_vuelta[pais].append(tiempo_vuelta)
            tiempos_totales[pais] += tiempo_vuelta
            print(f"El atleta de {pais} en el carril {carriles[list(probabilidades.keys()).index(pais)]} terminó en {tiempo_vuelta:.2f} segundos.")
        else:
            tiempo_vuelta = random.uniform(65, 120)
            velocidad_vuelta[pais].append(tiempo_vuelta)
            tiempos_totales[pais] += tiempo_vuelta
            print(f"El atleta de {pais} en el carril {carriles[list(probabilidades.keys()).index(pais)]} terminó en {tiempo_vuelta:.2f} segundos.")
equipos_ordenados = sorted(tiempos_totales.items(), key=lambda x: x[1])



print("\n¡Resultado Final!")
print(f"Medalla de Oro: {equipos_ordenados[0][0]} - Tiempo total: {equipos_ordenados[0][1]:.2f} segundos")
print(f"Medalla de Plata: {equipos_ordenados[1][0]} - Tiempo total: {equipos_ordenados[1][1]:.2f} segundos")
print(f"Medalla de Bronce: {equipos_ordenados[2][0]} - Tiempo total: {equipos_ordenados[2][1]:.2f} segundos")

#ANIMATION

def calcular_velocidad(tiempos_vuelta, distancia_pixeles, fps):
    velocidades = []
    for tiempo in tiempos_vuelta:
        velocidad = distancia_pixeles / (tiempo * fps)
        velocidades.append(velocidad)
    return velocidades

#Window
class Game:
    def __init__(self):
        pygame.init() #initiates pygame

        pygame.display.set_caption("Carrera de atletismo")

        self.width = 800
        self.height = 480
        self.screen = pygame.display.set_mode((self.width,self.height)) #initiate window

        self.clock = pygame.time.Clock()
        self.anim_speed = 10
        self.fps = 60
        self.distancia_por_tramo = 160
        self.test = 0

        #Tracks
        self.dark_orange_1 = pygame.Rect(0, 0, self.width, self.height//8)
        self.dark_orange_2 = pygame.Rect(0, 2*self.height//8, self.width, self.height//8)
        self.dark_orange_3 = pygame.Rect(0, 4*self.height//8, self.width, self.height//8)
        self.dark_orange_4 = pygame.Rect(0, 6*self.height//8, self.width, self.height//8)
        self.light_orange_1 = pygame.Rect(0, self.height//8, self.width, self.height//8)
        self.light_orange_2 = pygame.Rect(0, 3*self.height//8, self.width, self.height//8)
        self.light_orange_3 = pygame.Rect(0, 5*self.height//8, self.width, self.height//8)
        self.light_orange_4 = pygame.Rect(0, 7*self.height//8, self.width, self.height//8)

        #Goal lines
        self.line_1 = pygame.Rect(self.width//5, 0, 5, self.height)
        self.line_2 = pygame.Rect(2*self.width//5, 0, 5, self.height)
        self.line_3 = pygame.Rect(3*self.width//5, 0, 5, self.height)
        self.line_4 = pygame.Rect(4*self.width//5, 0, 5, self.height)

        #Flag imports
        self.usa_flag = pygame.image.load('assets/Flags/USA.png')
        self.usa_flag = pygame.transform.scale(self.usa_flag, (75, 75))
        self.etp_flag = pygame.image.load('assets/Flags/ETP.png')
        self.etp_flag = pygame.transform.scale(self.etp_flag, (75, 75))
        self.jam_flag = pygame.image.load('assets/Flags/JAM.png')
        self.jam_flag = pygame.transform.scale(self.jam_flag, (75, 75))
        self.ken_flag = pygame.image.load('assets/Flags/KEN.png')
        self.ken_flag = pygame.transform.scale(self.ken_flag, (75, 75))
        self.pol_flag = pygame.image.load('assets/Flags/POL.png')
        self.pol_flag = pygame.transform.scale(self.pol_flag, (75, 75))
        self.hol_flag = pygame.image.load('assets/Flags/HOL.png')
        self.hol_flag = pygame.transform.scale(self.hol_flag, (75, 75))
        self.france_flag = pygame.image.load('assets/Flags/FRANCE.png')
        self.france_flag = pygame.transform.scale(self.france_flag, (75, 75))
        self.bel_flag = pygame.image.load('assets/Flags/BEL.png')
        self.bel_flag = pygame.transform.scale(self.bel_flag, (75, 75))

        #Flags starting positions
        self.usa_flag_pos = [0, -7]
        self.etp_flag_pos = [0, self.height//8-7]
        self.jam_flag_pos = [0, 2*self.height//8-7]
        self.ken_flag_pos = [0, 3*self.height//8-7]
        self.pol_flag_pos = [0, 4*self.height//8-7]
        self.hol_flag_pos = [0, 5*self.height//8-7]
        self.france_flag_pos = [0, 6*self.height//8-7]
        self.bel_flag_pos = [0, 7*self.height//8-7]
    
    def run(self):
        #Animation loop
        while True:
            self.screen.fill(("White")) #screen clearing

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #Rendered tracks
            pygame.draw.rect(self.screen, (196, 70, 14), self.dark_orange_1)
            pygame.draw.rect(self.screen, (196, 70, 14), self.dark_orange_2)
            pygame.draw.rect(self.screen, (196, 70, 14), self.dark_orange_3)
            pygame.draw.rect(self.screen, (196, 70, 14), self.dark_orange_4)
            pygame.draw.rect(self.screen, (252, 134, 70), self.light_orange_1)
            pygame.draw.rect(self.screen, (252, 134, 70), self.light_orange_2)
            pygame.draw.rect(self.screen, (252, 134, 70), self.light_orange_3)
            pygame.draw.rect(self.screen, (252, 134, 70), self.light_orange_4)

            #Rendered lines
            pygame.draw.rect(self.screen, (255, 255, 255), self.line_1)
            pygame.draw.rect(self.screen, (255, 255, 255), self.line_2)
            pygame.draw.rect(self.screen, (255, 255, 255), self.line_3)
            pygame.draw.rect(self.screen, (255, 255, 255), self.line_4)

            #Rendered flags
            self.screen.blit(self.usa_flag, self.usa_flag_pos)
            self.screen.blit(self.etp_flag, self.etp_flag_pos)
            self.screen.blit(self.jam_flag, self.jam_flag_pos)
            self.screen.blit(self.ken_flag, self.ken_flag_pos)
            self.screen.blit(self.pol_flag, self.pol_flag_pos)
            self.screen.blit(self.hol_flag, self.hol_flag_pos)
            self.screen.blit(self.france_flag, self.france_flag_pos)
            self.screen.blit(self.bel_flag, self.bel_flag_pos)

            #USA flag speed
            if self.usa_flag_pos[0] < 160:
                self.usa_flag_pos[0] += (50 * (self.distancia_por_tramo / (velocidad_vuelta["USA"][0] * self.fps)))
            elif self.usa_flag_pos[0] >= 160 and self.usa_flag_pos[0] < 320:
                self.usa_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["USA"][1] * self.fps))
            elif self.usa_flag_pos[0] >= 320 and self.usa_flag_pos[0] < 480:
                self.usa_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["USA"][2] * self.fps))
            else:
                self.usa_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["USA"][3] * self.fps))

            #ETP flag speed
            if self.etp_flag_pos[0] < 160:
                self.etp_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Etiopía"][0] * self.fps))
            elif self.etp_flag_pos[0] >= 160 and self.etp_flag_pos[0] < 320:
                self.etp_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Etiopía"][1] * self.fps))
            elif self.etp_flag_pos[0] >= 320 and self.etp_flag_pos[0] < 480:
                self.etp_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Etiopía"][2] * self.fps))
            else:
                self.etp_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Etiopía"][3] * self.fps))
            
            #JAM flag speed
            if self.jam_flag_pos[0] < 160:
                self.jam_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Jamaica"][0] * self.fps))
            elif self.jam_flag_pos[0] >= 160 and self.jam_flag_pos[0] < 320:
                self.jam_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Jamaica"][1] * self.fps))
            elif self.jam_flag_pos[0] >= 320 and self.jam_flag_pos[0] < 480:
                self.jam_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Jamaica"][2] * self.fps))
            else:
                self.jam_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Jamaica"][3] * self.fps))
            
            #KEN flag speed
            if self.ken_flag_pos[0] < 160:
                self.ken_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Kenia"][0] * self.fps))
            elif self.ken_flag_pos[0] >= 160 and self.ken_flag_pos[0] < 320:
                self.ken_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Kenia"][1] * self.fps))
            elif self.ken_flag_pos[0] >= 320 and self.ken_flag_pos[0] < 480:
                self.ken_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Kenia"][2] * self.fps))
            else:
                self.ken_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Kenia"][3] * self.fps))
            
            #POL flag speed
            if self.pol_flag_pos[0] < 160:
                self.pol_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Polonia"][0] * self.fps))
            elif self.pol_flag_pos[0] >= 160 and self.pol_flag_pos[0] < 320:
                self.pol_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Polonia"][1] * self.fps))
            elif self.pol_flag_pos[0] >= 320 and self.pol_flag_pos[0] < 480:
                self.pol_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Polonia"][2] * self.fps))
            else:
                self.pol_flag_pos[0] += 50 * (self.distancia_por_tramo) / (velocidad_vuelta["Polonia"][3] * self.fps)
            
            #HOL flag speed
            if self.hol_flag_pos[0] < 160:
                self.hol_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Holanda"][0] * self.fps))
            elif self.hol_flag_pos[0] >= 160 and self.hol_flag_pos[0] < 320:
                self.hol_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Holanda"][1] * self.fps))
            elif self.hol_flag_pos[0] >= 320 and self.hol_flag_pos[0] < 480:
                self.hol_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Holanda"][2] * self.fps))
            else:
                self.hol_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Holanda"][3] * self.fps))
            
            #FRANCE flag speed
            if self.france_flag_pos[0] < 160:
                self.france_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Francia"][0] * self.fps))
            elif self.france_flag_pos[0] >= 160 and self.france_flag_pos[0] < 320:
                self.france_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Francia"][1] * self.fps))
            elif self.france_flag_pos[0] >= 320 and self.france_flag_pos[0] < 480:
                self.france_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Francia"][2] * self.fps))
            else:
                self.france_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Francia"][3] * self.fps))
            
            #BEL flag speed
            if self.bel_flag_pos[0] < 160:
                self.bel_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Bélgica"][0] * self.fps))
            elif self.bel_flag_pos[0] >= 160 and self.bel_flag_pos[0] < 320:
                self.bel_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Bélgica"][1] * self.fps))
            elif self.bel_flag_pos[0] >= 320 and self.bel_flag_pos[0] < 480:
                self.bel_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Bélgica"][2] * self.fps))
            else:
                self.bel_flag_pos[0] += 50 * (self.distancia_por_tramo / (velocidad_vuelta["Bélgica"][3] * self.fps))


            pygame.display.update() #renders screen stuff
            self.clock.tick(60) #limits fps

if __name__ == "__main__":
    game = Game()
    game.run()