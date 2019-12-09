import pygame
import sys

class Planet:

    #just an constant
    #G = 100
    G = 20
    planets = []
    velocity = pygame.math.Vector2(0, 0)
    acceleration = pygame.math.Vector2(0, 0)
    name = ""

    #a = G * m / r**2 * r^

    def setVelocity(self, velocity):
        self.velocity = velocity

    def getVelocity(self):
        return self.velocity

    def setAcc(self, acc):
        self.acceleration = acc
        self.acceleration

    def getAcc(self):
        return self.acceleration

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def __init__(self, name, color ,mass, position):

        self.color = color
        self.name = name
        self.mass = mass
        self.position = position

    def update(self, planets):
        self.planets = planets
        for planet in self.planets:
            if (planet.name is not self.name):
                vec = pygame.math.Vector2(planet.position.x - self.position.x, planet.position.y - self.position.y)
                nvec = vec.normalize()
                distance = vec.length()
                planet.setAcc((self.G * self.mass)/(distance**2) * nvec)
                planet.setVelocity(planet.getVelocity()-planet.getAcc())
                planet.setPosition(planet.getPosition()+planet.getVelocity())

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), int(self.mass))
        for planet in self.planets:
            #vec = pygame.math.Vector2(planet.position.x - self.position.x,  planet.position.y-self.position.y)
            #nvec = vec.normalize()
            pygame.draw.line(screen, (255,0,0), (self.position.x, self.position.y), (self.position.x + self.acceleration.x*10000, self.position.y + self.acceleration.y*10000))
            pygame.draw.line(screen, (255, 255, 0), (self.position.x, self.position.y), (self.position.x + self.velocity.x * 100, self.position.y + self.velocity.y * 100))
            font = pygame.font.Font(None, 30)
            lblName = font.render(self.name, True, pygame.Color('white'))
            lblAcc = font.render("a: "+str(self.acceleration.length()), True, pygame.Color("red"))
            lblVel = font.render("v: " + str(self.velocity.length()), True, pygame.Color("yellow"))
            screen.blit(lblName, (self.position.x-self.mass/2 +5, self.position.y-12))
            screen.blit(lblAcc, (self.position.x + self.acceleration.x*10000,self.position.y + self.acceleration.y*10000))
            screen.blit(lblVel, (self.position.x + self.velocity.x * 100, self.position.y + self.velocity.y * 100))


