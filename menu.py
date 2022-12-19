import subprocess
#subprocess.run(["C:/Users/Сергей/AppData/Local/Microsoft/WindowsApps/python3.10.exe", "main.py"])
import pygame
from pygame.locals import*

pygame.init()
screen = pygame.display.set_mode((700, 500))
img = pygame.image.load("images/menu.png")
img = pygame.transform.scale(img, (700, 500))
screen.blit(img, (0, 0))
running = True
x = 340
x1 = 340
y = 200
y1 = 300
width = 300
heith = 60
img1 = pygame.image.load("images/play.bmp")
img1 = pygame.transform.smoothscale(img1, (width, heith))
img2 = pygame.image.load("images/create.bmp")
img2 = pygame.transform.smoothscale(img2, (width, heith))
screen.blit(img1, (x, y))
screen.blit(img2, (x1, y1))
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    if pygame.mouse.get_pressed()[0]:
        if pygame.mouse.get_pos()[0] >= x and pygame.mouse.get_pos()[0] <= x + width and pygame.mouse.get_pos()[1] >= y and pygame.mouse.get_pos()[1] <= y + heith:
            subprocess.run(["C:/Users/Сергей/AppData/Local/Microsoft/WindowsApps/python3.10.exe", "main.py"])
            running = False
        if pygame.mouse.get_pos()[0] >= x1 and pygame.mouse.get_pos()[0] <= x1 + width and pygame.mouse.get_pos()[1] >= y1 and pygame.mouse.get_pos()[1] <= y1 + heith:
            subprocess.run(["C:/Users/Сергей/AppData/Local/Microsoft/WindowsApps/python3.10.exe", "creator.py"])
            running = False
pygame.quit()