import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))

class Circle():
    def __init__(self, color, position, radius):
        self.c = color
        self.pos = position
        self.rad = radius
        self.scr = screen
    def draw_circle(self):
        pygame.draw.circle(self.scr, self.c, self.pos, self.rad)
    def grow(self):
        self.rad += 10
        pygame.draw.circle(self.scr, self.c, self.pos, self.rad)

round = Circle("purple", (250,250), 40)
round.draw_circle()

while True:
    for i in pygame.event.get():
        screen.fill("white")
        if i.type == pygame.QUIT:
            pygame.quit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            round.draw_circle()
            pygame.display.update()
        elif i.type == pygame.MOUSEBUTTONUP:
            round.grow()
            pygame.display.update()
