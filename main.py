import pygame as pg
from SpaceShip import SpaceShip

windowWidth, windowHeight = 1000, 800

pg.init()
window = pg.display.set_mode((windowWidth, windowHeight))
pg.display.set_caption('Asteroid Destroyer')
clock = pg.time.Clock()
dt = 0

spaceship = SpaceShip('white', [windowWidth / 2, windowHeight / 2]) 

running = True
# Game Loop
while running:
    # Event Handling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Controls
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        spaceship.moveBy(0, -5)
    if keys[pg.K_s]:
        spaceship.moveBy(0, 5)
    if keys[pg.K_a]:
        spaceship.moveBy(-5, 0)
    if keys[pg.K_d]:
        spaceship.moveBy(5, 0)
    if keys[pg.K_w] and keys[pg.K_LSHIFT]:
        spaceship.moveBy(0, -8)
    if keys[pg.K_s] and keys[pg.K_LSHIFT]:
        spaceship.moveBy(0, 8)
    if keys[pg.K_a] and keys[pg.K_LSHIFT]:
        spaceship.moveBy(-8, 0)
    if keys[pg.K_d] and keys[pg.K_LSHIFT]:
        spaceship.moveBy(8, 0)
    
    # Game Rendering
    window.fill('black')
    
    pg.draw.polygon(window, spaceship.colour, spaceship.verteces, spaceship.width)

    # Update frame
    pg.display.flip()
    # fps = 60
    clock.tick(60)

pg.quit()