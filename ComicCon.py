#imports
import pygame, sys, time
from pygame.locals import *
#setting up the pygame window
pygame.init()
display_surface = pygame.display.set_mode((900, 700))
size = (900, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
#import background
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
#loding images
BackGround = Background('yeet.jpeg', [0,0])
image = pygame.image.load('Plzwork.png')
land=Background('landed.jpeg', [0,0])
fail=Background('Fail.jpeg', [0,0])
start=Background('start.jpeg', [0,0])
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
#setting the varibles
rock_x=300
rock_y=200
something=True
back_image=start.image
back_rect=start.rect
Place_hold=False
done = False
space_was_pressed = False
side_was_pressed =True
# -------- Main Program Loop -----------
while not done:
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    # --- Main event loop
    if keys[K_q]:
            done = True
            print('yeet')    #settup for game
    if keys[K_s]:
        back_image=BackGround.image
        back_rect=BackGround.rect
        Place_hold=True


            
    screen.blit(back_image, back_rect)
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and side_was_pressed: 
        display_surface.blit(image, (rock_x, rock_y))
        rock_x+=-2
        rock_y+=2
    if keys[K_RIGHT] and side_was_pressed:
        display_surface.blit(image, (rock_x, rock_y))
        rock_x+=2
        rock_y+=-2
    if Place_hold:
        display_surface.blit(image, (rock_x, rock_y))    
    bet= pygame.key.get_focused()
    #launch
    if keys[K_SPACE] or space_was_pressed:
            #side_was_pressed=False
            #space_was_pressed = True
            if rock_y>=-400:
                rock_x-=5
                rock_y-=5
    #land/miss
            print("areuhere")
            if rock_y==200 and rock_x>-360 and rock_x<-330:
                space_was_pressed=False
                time.sleep(.5)
                back_image=land.image
                back_rect=land.rect
                Place_hold=False
                print("tester")
                if keys[K_SPACE]:
                    rock_x=300
                    rock_y=200
                    something=True
                    back_image=start.image
                    back_rect=start.rect
                    Place_hold=False
                    done = False
                    space_was_pressed = False
                    side_was_pressed =True
            elif rock_y<-400:                
                keys = pygame.key.get_pressed()
                space_was_pressed=False
                time.sleep(.5)
                back_image=fail.image
                back_rect=fail.rect
                Place_hold=False
                #restart
                if keys[K_SPACE]:
                    rock_x=300
                    rock_y=200
                    something=True
                    back_image=start.image
                    back_rect=start.rect
                    Place_hold=False
                    done = False
                    space_was_pressed = False
                    side_was_pressed =True
    # --- Go ahead and update the screen with what we've drawn.
    #print(rock_y)
    print(rock_x)
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(100000)
# Close the window and quit.
pygame.quit()
