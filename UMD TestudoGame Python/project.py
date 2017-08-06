import pygame
import random

#provides animation
class Game(object):
    def main(self, screen):
        clock = pygame.time.Clock()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        game_over = False



        while True:
            # initialize the score, the position and the speed of everything
            score = 0
            background = pygame.image.load('background.jpg')
            testudo = pygame.image.load('testudo_edit.png')
            testudo_x = 0
            testudo_y = 0
            testudo_speed_y = random.randrange(1, 5)
            testudo_speed_x = random.randrange(4, 8)
            testudo_say = pygame.image.load('testudo_hit_me.png')

            rabbit = pygame.image.load('bunny.png')
            rabbit_x = 300
            rabbit_y = 550
            egg1 = pygame.image.load('esteregg.png')
            egg1_x = 50
            egg1_y = 0
            egg2 = pygame.image.load('easteregg2.png')
            egg2_x = 550
            egg2_y = 0
            egg3 = pygame.image.load('easteregg3.png')
            egg3_x = 950
            egg3_y = 0
            egg4 = pygame.image.load('easteregg4.png')
            egg4_x = 750
            egg4_y = 0
            egg5 = pygame.image.load('easteregg5.png')
            egg5_x = 650
            egg5_y = 0
            egg_speed_1 = random.randrange(2, 7)
            egg_speed_2 = random.randrange(2, 7)
            egg_speed_3 = random.randrange(2, 7)   	 
            egg_speed_4 = random.randrange(2, 7)   	 
            egg_speed_5 = random.randrange(2, 7) 


            # display beginning screen
            clock.tick(30)
            screen.blit(background, (0,0))
            welcome_text = myfont.render('Welcome to UMD Bunny Hop Game!', False, (0, 0, 0))
            screen.blit(welcome_text,(300,100))
            space_text = myfont.render('press SPACE to begin', False, (0, 0, 0))
            screen.blit(space_text,(350,170))
            pygame.display.flip()

            # begin the game by press space
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
	 


                    # Coordinate system for the game, clock is used to slow down cpu
                    while not game_over:
                        clock.tick(30)
                        
                        # initialize the rare case when the Testudo appears or say "Hit me"
                        rare = random.randrange(1000)
                        say_case = random.randrange(100)
                        

                        # display score
                        screen.blit(background, (0,0))
                        score_text = myfont.render('Score: ' + str(score), False, (0, 0, 0))
                        screen.blit(score_text,(0,0))
            
                        # display image
                        screen.blit(rabbit, (rabbit_x, rabbit_y))
                        screen.blit(egg1, (egg1_x, egg1_y))
                        screen.blit(egg1, (egg1_x, egg1_y))
                        screen.blit(egg2, (egg2_x, egg2_y))
                        screen.blit(egg3, (egg3_x, egg3_y))
                        screen.blit(egg4, (egg4_x, egg4_y))
                        screen.blit(egg5, (egg5_x, egg5_y))
                        pygame.display.flip()

                        # everything goes down
                        rabbit_y += 7
                        testudo_y += testudo_speed_y
                        testudo_x += testudo_speed_x
                        egg1_y += egg_speed_1
                        egg2_y += egg_speed_2
                        egg3_y += egg_speed_3
                        egg4_y += egg_speed_4
                        egg5_y += egg_speed_5
       	 
                        # eggs appear again after touch the ground
                        if egg1_y > 600:
                            egg1_x = random.randrange(0, 600)
                            egg1_y = -25
                        if egg2_y > 600:
                            egg2_x = random.randrange(0, 600)
                            egg2_y = -25
                        if egg3_y > 600:
                            egg3_x = random.randrange(0, 600)
                            egg3_y = -25    
                        if egg4_y > 600:
                            egg4_x = random.randrange(0, 600)
                            egg4_y = -25   
                        if egg5_y > 600:
                            egg5_x = random.randrange(0, 600)
                            egg5_y = -25   
       	 
                        # the first jump of the rabbit
                        if rabbit_y >= 550:
                            rabbit_y = 550
                            mouse = pygame.mouse.get_pressed()
                            if mouse[0]:
                                rabbit_y -= 300

                        # bunny cannot jump out of the upper screen
                        if rabbit_y <= 0:
                            rabbit_y = 0

                        # moving the bunny while hovering the mouse
                        (mouse_x,mouse_y) = pygame.mouse.get_pos()
                        rabbit_x = mouse_x
       	 
                        #user input from the mouse, exit game 
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                                return pygame.display.quit()


                        # bunny jumps when hitting the eggs or Testudo
                        if rabbit_x in range (egg1_x-50,egg1_x+50) and rabbit_y + 100 in range (egg1_y,egg1_y+20):
                            rabbit_y -= 300
                            score +=10
                            egg1_x = random.randrange(0, 600)
                            egg1_y = -25

                        if rabbit_x in range (egg2_x-50,egg2_x+50) and rabbit_y + 100 in range (egg2_y,egg2_y+20):
                            rabbit_y -= 300
                            score +=10
                            egg2_x = random.randrange(0, 600)
                            egg2_y = -25

                        if rabbit_x in range (egg3_x-50,egg3_x+50) and rabbit_y + 100 in range (egg3_y,egg3_y+20):
                            rabbit_y -= 300
                            score +=10
                            egg3_x = random.randrange(0, 600)
                            egg3_y = -25

                        if rabbit_x in range (egg4_x-50,egg4_x+50) and rabbit_y + 100 in range (egg4_y,egg4_y+20):
                            rabbit_y -= 300
                            score +=10
                            egg4_x = random.randrange(0, 600)
                            egg4_y = -25

                        if rabbit_x in range (egg5_x-50,egg5_x+50) and rabbit_y + 100 in range (egg5_y,egg5_y+20):
                            rabbit_y -= 300
                            score +=10
                            egg5_x = random.randrange(0, 600)
                            egg5_y = -25


                        if rabbit_x in range (testudo_x-50,testudo_x+50) and rabbit_y + 100 in range (testudo_y,testudo_y+20):
                            rabbit_y -= 300
                            score *=2
                            testudo_x = 1300
                            testudo_y = 650


                        # Testudo random appear
                        if testudo_x >= 1000:
                            testudo_x = 1300
                            testudo_y = 650

                        if rare == 1:
                            testudo_x = 0
                            testudo_y = 0
                            testudo_speed_y = random.randrange(1, 5)
                            testudo_speed_x = random.randrange(4, 8)

                
                        # display Testudo saying "Hit me"
                        if say_case in range (70):
                            screen.blit(testudo_say, (testudo_x, testudo_y))
                            pygame.display.flip()
                        else:
                            screen.blit(testudo, (testudo_x, testudo_y))
                            pygame.display.flip()

                        # game over if the bunny hit the ground
                        if rabbit_y in range (540, 550):
                            game_over = True
                
                    # display when game over
                    while game_over:
                        screen.blit(background, (0,0))
                        score_text = myfont.render('Score: ' + str(score), False, (0, 0, 0))
                        screen.blit(score_text,(0,0))
                        game_over_text = myfont.render('Great Job! You get ' + str(score) + ' score!!!', False, (0, 0, 0))
                        screen.blit(game_over_text,(300,100))
                        enter_text = myfont.render('Press Excape to quit.', False, (0, 0, 0))
                        screen.blit(enter_text,(350,170))
                        space_text = myfont.render('Or press SPACE to begin AGAIN', False, (0, 0, 0))
                        screen.blit(space_text,(350,200))
                        pygame.display.flip()
                        
                        #user input from the mouse, exit game or play it again
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                                return pygame.display.quit()
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                                game_over = False
                                break



#displays screen size 
if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((1000, 600))
	Game().main(screen)

