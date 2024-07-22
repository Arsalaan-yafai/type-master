def new_word():
    global word_x, word_y, text, chosen_word, press_word, speed
    word_x = random.randint(200, 500)
    word_y = 0
    chosen_word = random.choice(l1)
    text = font.render(chosen_word, True, blue)
    press_word = ''
    speed += 0.01


import pygame
import random
import sys
import time

pygame.init()
global word_x, word_y, text, chosen_word, press_word, speed

def ScreenText(text,colour,x,y,size,style, bold=False,itallic= False):
    font1= pygame.font.SysFont(style,size,bold=bold,italic=itallic)
    screen_text = font.render(text,True,colour)
    screen.blit(screen_text,(x,y))

"""
def highestscore():
    with open("highscore.txt","r") as f:
        return f.read()
"""

# colour
red = (192, 192, 192)
green = (196, 78, 58)
new = (78,54,10)
blue = (0, 0, 0)
speed = 0.05
point = 0
score = point
# screen size
x = 900
y = 600
"""
try :
      highscore= int(highestscore())
except:
       highscore=0
"""

screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("TYPE MASTER VIA CLOUDS")
# images
logo = pygame.image.load("coding.png")
background1 = pygame.image.load("background1.jpg")
background2 = pygame.image.load("background2.jpg")
cloud = pygame.image.load("file (1).png")
explosion = pygame.image.load("explosion1.gif")
pygame.display.set_icon(logo)
# music
pygame.mixer.init()
channel0 = pygame.mixer.Channel(0)
channel1 = pygame.mixer.Channel(1)
blastmusic = pygame.mixer.Sound("boom.wav")
loss_music = pygame.mixer.Sound("loss1.wav")
channel0.set_volume(0.2)
channel1.set_volume(0.5)
pygame.mixer.music.load('Allan-Walker-Faded-Instrumental.wav')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()

# list

l1 = ['arsalaan', 'yafai', 'coder', 'coding', 'gym', 'bullet', 'owl', 'rehan', 'faizan', 'physics',
      'mango', 'maths', 'red', 'blue', 'bike', 'barbell', 'deadlift', 'benchpress', 'bench', 'bus', 'squat', 'lats',
      'abs', 'bicep', 'tricep', 'shoulder', 'back', 'laptop', 'india', 'orange', 'red', 'green', 'black', 'white',
      'car', 'cloud', 'saudi']
font = pygame.font.SysFont('ComicSansMs', 45)
text1 = font.render('Hit Enter to restart the game', True, blue)
# score1 =  font.render('Score: ',True,blue)
# highscoretext =font.render('highscore: ',True,blue)
# high_score1= font.render(high_score,True,blue)
new_word()
while True:

    # screen.blit(text,(word_x,word_y))
    screen.blit(background1, (0, 0))
    screen.blit(cloud, (word_x - 20, word_y - 10))
    screen.blit(text, (word_x, word_y))
    word_y += speed
    word_caption = font.render(chosen_word, True, new)
    screen.blit(word_caption, (650, 0))
    # screen.blit(score1, (0, 0))
    # screen.blit(highscoretext,(0,50))
    # screen.blit(high_score1,(50,50))
    point_caption = font.render(str(point), True, green)
    ScreenText(f"score: {score} ", red, 0, 0, size=20, style="calibri")
    # ScreenText(f"High_Score: {highscore} ", red, 20, 40, size=20, style="calibri")

    # screen.blit(point_caption, (150, 0))
    """
    if highscore < score:
        with open(f"highscore.txt", "w") as f:
            f.write(str(highscore))
   """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif (event.type == pygame.KEYDOWN):
            press_word += pygame.key.name(event.key)
            if chosen_word.startswith(press_word):
                text = font.render(press_word, True, green)
                if chosen_word == press_word:
                    point += len(chosen_word)
                    score = point
                    pygame.display.update()

                    channel0.play((blastmusic), maxtime=600)
                    screen.blit(explosion, (word_x, word_y))
                    pygame.display.update()
                    time.sleep(0.07)
                    new_word()


            else:
                text = font.render(press_word, True, red)
                press_word = ''
        if (word_y <= y - 10):
            pass
        else:
            a = pygame.mixer.Channel(1).get_busy()
            if a == 1:
                pass
            else:
                channel1.play(loss_music, maxtime=6000)
            screen.blit(text1, (100, 260))

            pygame.display.update()
            event = pygame.event.wait()

            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                point = 0
                speed = 0.1
                new_word()

        pygame.display.update()
