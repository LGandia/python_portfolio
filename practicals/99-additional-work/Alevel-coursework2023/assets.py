
import pygame

import constants


SPACESHIP_RESIZE = 2

spaceship_sprite_width = 40 * SPACESHIP_RESIZE
spaceship_sprite_height = 40 * SPACESHIP_RESIZE

spaceship_spritesheet_width = 8 * spaceship_sprite_width
spaceship_spritesheet_height = 1 * spaceship_sprite_height

spaceship_1_surface = pygame.Surface((40 * SPACESHIP_RESIZE, 40 * SPACESHIP_RESIZE))
spaceship_2_surface = pygame.Surface((40 * SPACESHIP_RESIZE, 40 * SPACESHIP_RESIZE))
spaceship_exploding_0_surface = pygame.Surface((40 * SPACESHIP_RESIZE, 40 * SPACESHIP_RESIZE))
spaceship_exploding_1_surface = pygame.Surface((40 * SPACESHIP_RESIZE, 40 * SPACESHIP_RESIZE))
spaceship_exploding_2_surface = pygame.Surface((40 * SPACESHIP_RESIZE, 40 * SPACESHIP_RESIZE))
spaceship_exploding_3_surface = pygame.Surface((40 * SPACESHIP_RESIZE, 40 * SPACESHIP_RESIZE))
spaceship_exploding_4_surface = pygame.Surface((40 * SPACESHIP_RESIZE, 40 * SPACESHIP_RESIZE))
spaceship_exploding_5_surface = pygame.Surface((40 * SPACESHIP_RESIZE, 40 * SPACESHIP_RESIZE))

missile_sprite_width = 32
missile_sprite_height = 32

missile_e_surface = pygame.Surface((missile_sprite_width, missile_sprite_height))

missile_se_surface = pygame.Surface((missile_sprite_width, missile_sprite_height))
missile_s_surface = pygame.Surface((missile_sprite_width, missile_sprite_height))
missile_sw_surface = pygame.Surface((missile_sprite_width, missile_sprite_height))
missile_w_surface = pygame.Surface((missile_sprite_width, missile_sprite_height))
missile_nw_surface = pygame.Surface((missile_sprite_width, missile_sprite_height))
missile_n_surface = pygame.Surface((missile_sprite_width, missile_sprite_height))
missile_ne_surface = pygame.Surface((missile_sprite_width, missile_sprite_height))

enemy_sprite_width = 60
enemy_sprite_height = 48

enemy_surface = pygame.Surface((enemy_sprite_width, enemy_sprite_height))

asteroid_sprite_width = 60
asteroid_sprite_height = 48

asteroid_surface = pygame.Surface((enemy_sprite_width, enemy_sprite_height))

start_menu_surface = pygame.Surface((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
game_over_surface = pygame.Surface((426, 220), pygame.SRCALPHA)
pause_icon_surface = pygame.Surface((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

def set_up_graphics():

    # load and resize the spaceship spritesheet

    spaceship_spritesheet = pygame.image.load("assets/graphics/spaceship_spritesheet.png").convert()

    spaceship_spritesheet = pygame.transform.scale(spaceship_spritesheet, (spaceship_spritesheet_width, spaceship_spritesheet_height))

    # draw the images from george's spritesheet onto the surfaces

    spaceship_1_surface.blit(spaceship_spritesheet, (0, 0), (0 * spaceship_sprite_width, 0, spaceship_sprite_width, spaceship_sprite_height))
    spaceship_2_surface.blit(spaceship_spritesheet, (0, 0), (1 * spaceship_sprite_width, 0, spaceship_sprite_width, spaceship_sprite_height))
    spaceship_exploding_0_surface.blit(spaceship_spritesheet, (0, 0), (2 * spaceship_sprite_width, 0, spaceship_sprite_width, spaceship_sprite_height))
    spaceship_exploding_1_surface.blit(spaceship_spritesheet, (0, 0), (3 * spaceship_sprite_width, 0, spaceship_sprite_width, spaceship_sprite_height))
    spaceship_exploding_2_surface.blit(spaceship_spritesheet, (0, 0), (4 * spaceship_sprite_width, 0, spaceship_sprite_width, spaceship_sprite_height))
    spaceship_exploding_3_surface.blit(spaceship_spritesheet, (0, 0), (5 * spaceship_sprite_width, 0, spaceship_sprite_width, spaceship_sprite_height))
    spaceship_exploding_4_surface.blit(spaceship_spritesheet, (0, 0), (6 * spaceship_sprite_width, 0, spaceship_sprite_width, spaceship_sprite_height))
    spaceship_exploding_5_surface.blit(spaceship_spritesheet, (0, 0), (7 * spaceship_sprite_width, 0, spaceship_sprite_width, spaceship_sprite_height))

    # set the colorkeys to black

    spaceship_1_surface.set_colorkey((0, 0, 0,))
    spaceship_2_surface.set_colorkey((0, 0, 0,))
    spaceship_exploding_0_surface.set_colorkey((0, 0, 0,))
    spaceship_exploding_1_surface.set_colorkey((0, 0, 0,))
    spaceship_exploding_2_surface.set_colorkey((0, 0, 0,))
    spaceship_exploding_3_surface.set_colorkey((0, 0, 0,))
    spaceship_exploding_4_surface.set_colorkey((0, 0, 0,))
    spaceship_exploding_5_surface.set_colorkey((0, 0, 0,))

    # load the missile spritesheet

    missile_spritesheet = pygame.image.load("assets/graphics/missile_spritesheet.png").convert()

    # draw the images from the missile spritesheet onto the surfaces

    missile_e_surface.blit(missile_spritesheet, (0, 0), (0 * missile_sprite_width, 0, missile_sprite_width, missile_sprite_height))
    
    missile_se_surface.blit(missile_spritesheet, (0, 0), (1 * missile_sprite_width, 0, missile_sprite_width, missile_sprite_height))
    missile_s_surface.blit(missile_spritesheet, (0, 0), (2 * missile_sprite_width, 0, missile_sprite_width, missile_sprite_height))
    missile_sw_surface.blit(missile_spritesheet, (0, 0), (3 * missile_sprite_width, 0, missile_sprite_width, missile_sprite_height))
    missile_w_surface.blit(missile_spritesheet, (0, 0), (4 * missile_sprite_width, 0, missile_sprite_width, missile_sprite_height))
    missile_nw_surface.blit(missile_spritesheet, (0, 0), (5 * missile_sprite_width, 0, missile_sprite_width, missile_sprite_height))
    missile_n_surface.blit(missile_spritesheet, (0, 0), (6 * missile_sprite_width, 0, missile_sprite_width, missile_sprite_height))
    missile_ne_surface.blit(missile_spritesheet, (0, 0), (7 * missile_sprite_width, 0, missile_sprite_width, missile_sprite_height))

    # set the colorkeys to black

    missile_e_surface.set_colorkey((0, 0, 0,))
    
    missile_se_surface.set_colorkey((0, 0, 0,))
    missile_s_surface.set_colorkey((0, 0, 0,))
    missile_sw_surface.set_colorkey((0, 0, 0,))
    missile_w_surface.set_colorkey((0, 0, 0,))
    missile_nw_surface.set_colorkey((0, 0, 0,))
    missile_n_surface.set_colorkey((0, 0, 0,))
    missile_ne_surface.set_colorkey((0, 0, 0,))


    # load and resize the enemy graphic
    enemy_graphic = pygame.image.load("assets/graphics/enemy.png").convert()
    enemy_graphic = pygame.transform.scale(enemy_graphic, (enemy_sprite_width, enemy_sprite_height))

    # draw the images from the enemy graphic onto the surface
    enemy_surface.blit(enemy_graphic, (0, 0), (0, 0, enemy_sprite_width, enemy_sprite_height))

    # set the colorkey to black
    enemy_surface.set_colorkey((0, 0, 0,))


    # load and resize the asteroid graphic
    asteroid_graphic = pygame.image.load("assets/graphics/asteroid.png").convert()
    asteroid_graphic = pygame.transform.scale(asteroid_graphic, (asteroid_sprite_width, asteroid_sprite_height))

    # draw the images from the asteroid graphic onto the surface
    asteroid_surface.blit(asteroid_graphic, (0, 0), (0, 0, asteroid_sprite_width, asteroid_sprite_height))

    # set the colorkey to black
    asteroid_surface.set_colorkey((0, 0, 0,))


    # load and resize the start menu graphic
    start_menu_graphic = pygame.image.load("assets/graphics/start_menu.png").convert()
    start_menu_graphic = pygame.transform.scale(start_menu_graphic, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    # draw the image from the start menu graphic onto the surface
    start_menu_surface.blit(start_menu_graphic, (0, 0), (0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))


    # load the game over graphic
    game_over_graphic = pygame.image.load("assets/graphics/game_over.png").convert_alpha()

    # draw the image from the game graphic onto the surface
    game_over_surface.blit(game_over_graphic, (0, 0), (0, 0, 426, 220))


    # load and resize the pause menu graphic

    pause_icon_graphic = pygame.image.load("assets/graphics/pause_icon.png").convert()

    pause_icon_graphic = pygame.transform.scale(pause_icon_graphic, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    # draw the image from the pause menu graphic onto the surface

    pause_icon_surface.blit(pause_icon_graphic, (0, 0), (0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    #set colourkey to black
    pause_icon_surface.set_colorkey((0, 0, 0,))