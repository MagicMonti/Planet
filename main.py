import pygame
import planet as pl

class main:
    pygame.init()
    screen = pygame.display.set_mode((3000, 2000))
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 30)

    planet1 = pl.Planet("Earth", (0,128,0), 100, pygame.Vector2(1000, 500))
    planet2 = pl.Planet("Mars", (255, 100, 0) , 7, pygame.Vector2(700, 1000))
    planet3 = pl.Planet("Venus", (0,0,255), 8, pygame.Vector2(100,800))
    planet4 = pl.Planet("Uranus", (0, 255, 255), 300, pygame.Vector2(1500, 1000))


    planet2.setVelocity(pygame.math.Vector2(-0.5, 0.5))
    planet1.setVelocity(pygame.math.Vector2(-2,1))
    planet3.setVelocity(pygame.math.Vector2(0,-1))
    planets = [planet1, planet2, planet3, planet4]
    #planets = [planet1, planet2]
    def update(self):
        for planet in self.planets:
            planet.update(self.planets) #a planet knows every other planet

    def draw(self):
        #fps stuff
        self.screen.fill(pygame.Color('black'))
        fps = self.font.render(str(int(self.clock.get_fps())), True, pygame.Color('white'))
        self.screen.blit(fps, (50, 50))
        #----

        for planet in self.planets:
            planet.draw(self.screen)

    def __init__(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            self.draw()
            self.update()
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    main()
