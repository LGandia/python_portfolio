
import pygame
import random

import constants
import assets
import sprites

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

#background
bg = pygame.image.load("assets/graphics/spaceground.png")
bg = pygame.transform.scale(bg,(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

assets.set_up_graphics()

spaceship = sprites.SpaceshipSprite()

sprites.spaceship_group.add(spaceship)


# program_loop

program_running = True
while program_running:

    pygame.event.clear()

    # check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_running = False

    # draw the start menu
    screen.blit(assets.start_menu_surface, (0, 0))
    pygame.display.flip()

    # start menu loop
    start_menu = True
    while start_menu:

        # check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_menu = False
                program_running = False
            elif event.type == pygame.KEYDOWN:
                start_menu = False

    # initialise a new game

    bg_x=0
    bg_y=0
    speed = 0

    spaceship.x = (constants.SCREEN_WIDTH // 2) - (assets.spaceship_sprite_width // 2)
    spaceship.y = (constants.SCREEN_HEIGHT // 2) - (assets.spaceship_sprite_height // 2)

    spaceship.current_speed = spaceship.BASIC_SPEED

    spaceship.hitbox_left = spaceship.x + sprites.SPACESHIP_HITBOX_X_OFFSET
    spaceship.hitbox_top = spaceship.y + sprites.SPACESHIP_HITBOX_Y_OFFSET
    spaceship.rect = pygame.Rect(spaceship.hitbox_left, spaceship.hitbox_top, spaceship.HITBOX_WIDTH, spaceship.HITBOX_HEIGHT)

    spaceship_alive = True
    spaceship_explosion_count = 0

    asteroid_count_reset = constants.ASTEROID_COUNT_RESET
    asteroid_count = asteroid_count_reset

    enemy_count_reset = constants.ENEMY_COUNT_RESET
    enemy_count = enemy_count_reset


    # game loop

    game_running = True
    pause = False
    while program_running and game_running:

        # check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                program_running = False

        # spaceship control
        keys = pygame.key.get_pressed()
        spaceship.control(keys)

        # press ctrl for shooting

        if keys[pygame.K_p] and pause == False:
            pause = True 
            screen.blit(assets.pause_icon_surface, (0, 0))
            print ('pause')
        
        elif keys[pygame.K_p] and pause == True:
            pause = False
            print ('unpause')


        elif pause == False:
            
            # screen background

            speed = speed + 0.05 
            bg_x -= speed/2

            bg_x1 = -constants.SCREEN_WIDTH + bg_x
            screen.blit(bg, (bg_x1, bg_y))

            bg_x2 = bg_x1 + constants.SCREEN_WIDTH
            screen.blit(bg, (bg_x2, bg_y))

            bg_x += 0
            if bg_x < 0:
                bg_x += constants.SCREEN_WIDTH
            elif bg_x >= constants.SCREEN_WIDTH:
                bg_x -= constants.SCREEN_WIDTH


            # asteroids

            asteroid_count -= 1
            if asteroid_count == 0:

                # spawn a new asteroid
                x = constants.SCREEN_WIDTH
                y = random.randint(32, constants.SCREEN_HEIGHT - 32)
                x_speed = -10
                y_speed = 0
                sprites.asteroid_group.add(sprites.AsteroidSprite(x, y, x_speed, y_speed))

                asteroid_count = asteroid_count_reset
                if asteroid_count > 0:
                    asteroid_count_reset -= 1

            for i in sprites.asteroid_group:

                i.move()

                #pygame.draw.rect(screen, "blue", i.rect)
                screen.blit(i.surface, (i.x, i.y))

                if i.x < -32 or i.x > constants.SCREEN_WIDTH + 32:
                    i.kill()


            # enemies

            enemy_count -= 1
            if enemy_count == 0:

                # spawn a new enemy
                x = constants.SCREEN_WIDTH
                y = random.randint(64, constants.SCREEN_HEIGHT - 64)
                x_speed = -20
                y_speed = random.randint(0, 20)
                sprites.enemy_group.add(sprites.EnemySprite(x, y, x_speed, y_speed))

                enemy_count = enemy_count_reset
                if enemy_count > 0:
                    enemy_count_reset -= 1

            for i in sprites.enemy_group:

                i.move()

                #pygame.draw.rect(screen, "blue", i.rect)
                screen.blit(i.surface, (i.x, i.y))

                if i.x < -32:
                    i.kill()


            # collisions between enemies and asteroids

            for enm in sprites.enemy_group:

                for ast in sprites.asteroid_group:

                    if enm.rect.colliderect(ast.rect):

                        if enm.rect.centerx >= ast.rect.centerx:
                            ast.x_speed += 10
                            enm.x_speed -= 10

                        ast.y_speed += enm.y_speed
                        enm.y_speed *= -1
            
            if spaceship_alive:

                #pygame.draw.rect(screen, "blue", spaceship.rect)
                
                # missiles
                for i in sprites.missiles_group:
                    if len(sprites.missiles_group) == 1:
                        i.move()
                        screen.blit(i.surface_to_draw, (i.x, i.y + 8))
                    
                    elif len(sprites.missiles_group) >1:
                        i.kill()
                        
                    elif i.x > constants.SCREEN_WIDTH + 32:
                        i.kill()
                        

                # missiles hit asteroid

                for i in sprites.asteroid_group:
                    for x in sprites.missiles_group:

                        if pygame.sprite.spritecollideany(i, sprites.missiles_group):

                            i.kill()
                            x.kill()

                # missiles hit enemy

                for i in sprites.enemy_group:
                    for x in sprites.missiles_group:
                        if pygame.sprite.spritecollideany(i, sprites.missiles_group):
                        
                            i.kill()
                            x.kill()
                # arrows
                if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_RIGHT]:
                    screen.blit(assets.spaceship_2_surface, (spaceship.x, spaceship.y))
                else:
                    screen.blit(assets.spaceship_1_surface, (spaceship.x, spaceship.y))

                # awsd
                if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_d]:
                    screen.blit(assets.spaceship_2_surface, (spaceship.x, spaceship.y))
                else:
                    screen.blit(assets.spaceship_1_surface, (spaceship.x, spaceship.y))

                # collision with asteroid or enemy

                if pygame.sprite.spritecollideany(spaceship, sprites.asteroid_group) \
                        or pygame.sprite.spritecollideany(spaceship, sprites.enemy_group):
                    spaceship_explosion_count = 24

                if spaceship_explosion_count > 20:
                    screen.blit(assets.spaceship_exploding_0_surface, (spaceship.x, spaceship.y))
                    spaceship_explosion_count -= 1

                elif spaceship_explosion_count > 16:
                    screen.blit(assets.spaceship_exploding_1_surface, (spaceship.x, spaceship.y))
                    spaceship_explosion_count -= 1

                elif spaceship_explosion_count > 12:
                    screen.blit(assets.spaceship_exploding_2_surface, (spaceship.x, spaceship.y))
                    spaceship_explosion_count -= 1

                elif spaceship_explosion_count > 8:
                    screen.blit(assets.spaceship_exploding_3_surface, (spaceship.x, spaceship.y))
                    spaceship_explosion_count -= 1

                elif spaceship_explosion_count > 4:
                    screen.blit(assets.spaceship_exploding_4_surface, (spaceship.x, spaceship.y))
                    spaceship_explosion_count -= 1

                elif spaceship_explosion_count > 0:
                    screen.blit(assets.spaceship_exploding_5_surface, (spaceship.x, spaceship.y))
                    spaceship_explosion_count -= 1
                    if spaceship_explosion_count == 0:
                        spaceship_alive = False


            if not spaceship_alive and spaceship_explosion_count == 0:

                screen.blit(assets.game_over_surface, (160, 160))

                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE] or keys[pygame.K_SPACE]:
                    game_over_menu = False
                    game_running = False


        pygame.display.flip()
        clock.tick(15)

print("goodbye")

