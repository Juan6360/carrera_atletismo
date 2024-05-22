import random
import pygame, sys

probabilidades = {
    "USA": 0.20,
    "Francia": 0.07,
    "Jamaica": 0.15,
    "Etiopía": 0.18,
    "Polonia": 0.11,
    "Holanda": 0.09,
    "Bélgica": 0.07,
    "Kenia": 0.13
}

tiempos_totales = {pais: 0 for pais in probabilidades}

carriles = random.sample(range(1, 9), len(probabilidades))

print("¡Comienza la competencia!")
print("Carriles asignados a los equipos:")
for pais, carril in zip(probabilidades.keys(), carriles):
    print(f"{pais} en el carril {carril}")

for vuelta in range(4):
    print(f"\nInicio de la vuelta {vuelta+1}:")
    for pais in probabilidades:
        
        if random.random() <= probabilidades[pais]:
            tiempo_vuelta = random.uniform(40, 60)
            tiempos_totales[pais] += tiempo_vuelta
            print(f"El atleta de {pais} en el carril {carriles[list(probabilidades.keys()).index(pais)]} terminó en {tiempo_vuelta:.2f} segundos.")
        else:
            tiempo_vuelta = random.uniform(65, 120)
            tiempos_totales[pais] += tiempo_vuelta
            print(f"El atleta de {pais} en el carril {carriles[list(probabilidades.keys()).index(pais)]} terminó en {tiempo_vuelta:.2f} segundos.")
equipos_ordenados = sorted(tiempos_totales.items(), key=lambda x: x[1])



print("\n¡Resultado Final!")
print(f"Medalla de Oro: {equipos_ordenados[0][0]} - Tiempo total: {equipos_ordenados[0][1]:.2f} segundos")
print(f"Medalla de Plata: {equipos_ordenados[1][0]} - Tiempo total: {equipos_ordenados[1][1]:.2f} segundos")
print(f"Medalla de Bronce: {equipos_ordenados[2][0]} - Tiempo total: {equipos_ordenados[2][1]:.2f} segundos")

#Window
class Game:
    def __init__(self):
        pygame.init() #initiates pygame

        pygame.display.set_caption("Carrera de atletismo")

        self.width = 640
        self.height = 480
        self.screen = pygame.display.set_mode((self.width,self.height)) #initiate window

        self.clock = pygame.time.Clock()

        #Tracks
        self.dark_orange_1 = pygame.Rect(0, 0, self.width, self.height//8)
        self.dark_orange_2 = pygame.Rect(0, 2*self.height//8, self.width, self.height//8)
        self.dark_orange_3 = pygame.Rect(0, 4*self.height//8, self.width, self.height//8)
        self.dark_orange_4 = pygame.Rect(0, 6*self.height//8, self.width, self.height//8)
        self.light_orange_1 = pygame.Rect(0, self.height//8, self.width, self.height//8)
        self.light_orange_2 = pygame.Rect(0, 3*self.height//8, self.width, self.height//8)
        self.light_orange_3 = pygame.Rect(0, 5*self.height//8, self.width, self.height//8)
        self.light_orange_4 = pygame.Rect(0, 7*self.height//8, self.width, self.height//8)

        #Flag imports
        self.usa_flag = pygame.image.load('assets/Flags/USA.png')
        self.usa_flag = pygame.transform.scale(self.usa_flag, (75, 75))
        self.france_flag = pygame.image.load('assets/Flags/FRANCE.png')

        #Flags starting positions
        self.usa_flag_pos = [0, -10]
        self.france_flag_pos = [0, self.height//8-10]
    
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

            #Rendered flags
            self.screen.blit(self.usa_flag, self.usa_flag_pos)
            self.usa_flag_pos[0] += 1
            self.screen.blit(self.france_flag, self.france_flag_pos)
            self.france_flag_pos[0] += 1

            pygame.display.update() #renders screen stuff
            self.clock.tick(60) #limits fps

if __name__ == "__main__":
    game = Game()
    game.run()