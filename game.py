import pygame
import random
import math
from pygame import mixer

pygame.init()

#Screen Create
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Mango Catcher")
# icon = pygame.image.load('mango (1).png')
icon = pygame.image.load('mangoes.png')
pygame.display.set_icon(icon)

#Background Image
bgImage = pygame.image.load('background.png')

#Background Music
mixer.music.load('background.wav')
mixer.music.play(-1)
#Score:
score = 0
font = pygame.font.Font('freesansbold.ttf',32)
fontX= 20
fontY= 15

MangoFallCount = 0
#GameOverText
over_font=pygame.font.Font('freesansbold.ttf',64)

def game_over():
    ovet_text = font.render("Game Over",True,(255,255,255))
    screen.blit(ovet_text,(350,250))

def fontShow(x,y):
    scoreValue = font.render("Score : "+str(score),True,(255,123,255))
    screen.blit(scoreValue,(x,y))

#Bucket
bucketImg = pygame.image.load('bucket.png')
bucketX = 390
bucketY = 536
bucketMoveX=0
falling = False

def bucketRun(x,y):
    screen.blit(bucketImg,(x,y))
    global falling
    falling=True


mangoImg = pygame.image.load('mango (1).png')
mangoX = random.randint(18,750)
mangoY = random.randint(20,98)
mangoChangeY = 6

def mangoFall(x,y):
    screen.blit(mangoImg,(x,y))


def is_cought(enX,enY,buX,buY):
    distance = math.sqrt( math.pow(enX-buX,2)+math.pow(enY-buY,2) )
    if distance <=40 :
        return True
    return False


running = True
while running:
    screen.fill((127,127,127))
    screen.blit(bgImage,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bucketMoveX = -11
            if event.key == pygame.K_RIGHT:
                bucketMoveX = 11
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT:
                bucketMoveX = 0

    if MangoFallCount >= 5:
        mangoX = 2000
        game_over()
        
    if score >= 5:
        mangoChangeY = 7
    bucketX+=bucketMoveX
    if bucketX <= 0:
        bucketX = 0
    if bucketX >= 736:
        bucketX = 736

    if falling:
        mangoY+=mangoChangeY
    if mangoY >=600:
        MangoFallCount+=1
        mangoX = random.randint(10,768)
        mangoY = random.randint(0,100)
    
    
    if is_cought(mangoX,mangoY,bucketX,bucketY):
        score+=1
        mangoX = random.randint(10,768)
        mangoY = random.randint(0,100)
    
    mangoFall(mangoX,mangoY)
    bucketRun(bucketX,bucketY)
    fontShow(fontX,fontY)
    pygame.display.update()

