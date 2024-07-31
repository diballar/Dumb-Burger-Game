import sys
import pygame
import os
import playsound
import random
from threading import Thread

rl_path = os.path.realpath(__file__)

path = rl_path.replace('main.py', '')
print(f"{path}")
os.chdir(path)
print(os.getcwd())

# Initialize Pygame
pygame.init()

# Set up display
width, height = 300, 250
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Burger")
icon = pygame.image.load('burg_icon.png')
pygame.display.set_icon(icon)

# Define colors
white = (255, 255, 255)

brown = (205, 127, 50)

font = pygame.font.Font(None, 60)

score = 0
burg = pygame.image.load("burg.png")
burger = burg.get_rect(center = (width // 2, 150))
text_render = font.render(f"{score}", True, (0, 0, 0))
scor = text_render.get_rect(center = (width // 2, 40))

rand_sound = ['nom1.mp3', 'nom2.mp3', 'nom3.mp3']
music_p = ['music1.mp3', 'music2.mp3', 'music3.mp3', 'music4.mp3']

def music_thread():
    while True:
        for x in music_p:
            playsound.playsound(x)

def music():
    thread2 = Thread(target= music_thread)
    thread2.daemon = True
    thread2.start()

def bite_sound():
    rand = random.choice(rand_sound)
    playsound.playsound(rand)

def bite():
    thread = Thread(target= bite_sound)
    thread.start()

music()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            score += 1

            bite()

    # Update game logic here
    text_render = font.render(f"{score}", True, (0, 0, 0))
    scor = text_render.get_rect(center = (width // 2, 40))

    screen.fill(brown)

    screen.blit(burg, burger)
    screen.blit(text_render, scor)

    pygame.display.flip()

    # Set the frames per second
    pygame.time.Clock().tick(60)
