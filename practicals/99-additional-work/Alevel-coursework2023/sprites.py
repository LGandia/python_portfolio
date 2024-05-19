
import pygame

import constants
import assets


SPACESHIP_HITBOX_X_OFFSET = 16
SPACESHIP_HITBOX_Y_OFFSET = 18


class SpaceshipSprite(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.x = None
        self.y = None

        self.X_CHANGE = 8
        self.Y_CHANGE = 8

        self.BASIC_SPEED = 8

        self.SPEED_CHANGE = 2

        self.current_speed = None

        self.pic_number = None

        self.hitbox_left = None
        self.hitbox_top = None

        self.HITBOX_WIDTH = 42
        self.HITBOX_HEIGHT = 44

        self.rect = None


    def control(self, keys):

        # movement

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= self.X_CHANGE

        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.X_CHANGE
        
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.y -= self.Y_CHANGE

        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.y += self.Y_CHANGE

        self.hitbox_left = self.x + SPACESHIP_HITBOX_X_OFFSET
        self.hitbox_top = self.y + SPACESHIP_HITBOX_Y_OFFSET
        self.rect = pygame.Rect(self.hitbox_left, self.hitbox_top, self.HITBOX_WIDTH, self.HITBOX_HEIGHT)

        if keys[pygame.K_RCTRL] or keys[pygame.K_LCTRL]:
            missiles_group.add(MissileSprite(self.hitbox_left, self.hitbox_top, "east"))


class AsteroidSprite(pygame.sprite.Sprite):

    def __init__(self, x, y, x_speed, y_speed):

        super().__init__()

        self.x = x
        self.y = y

        self.x_speed = x_speed
        self.y_speed = y_speed

        self.surface = assets.asteroid_surface

        self.rect = self.surface.get_rect()
        self.rect.topleft = (self.x, self.y)


    def move(self):

        # collision with top or bottom of screen
        if self.rect.top <= 0 or self.rect.bottom >= constants.SCREEN_HEIGHT - 1:
            self.y_speed *= -1

        self.x += self.x_speed
        self.y += self.y_speed

        self.rect.topleft = (self.x, self.y)


class EnemySprite(pygame.sprite.Sprite):

    def __init__(self, x, y, x_speed, y_speed):

        super().__init__()

        self.x = x
        self.y = y

        self.x_speed = x_speed
        self.y_speed = y_speed

        self.surface = assets.enemy_surface

        self.rect = self.surface.get_rect()
        self.rect.topleft = (self.x, self.y)


    def move(self):

        # collision with top or bottom of screen
        if self.rect.top <= 0 or self.rect.bottom >= constants.SCREEN_HEIGHT - 1:
            self.y_speed *= -1

        self.x += self.x_speed
        self.y += self.y_speed

        self.rect.topleft = (self.x, self.y)


class MissileSprite(pygame.sprite.Sprite):

    def __init__(self, x, y, direction):

        super().__init__()

        self.x = x
        self.y = y

        self.direction = direction

        if self.direction == "east":
            self.surface_to_draw = assets.missile_e_surface

        self.rect = self.surface_to_draw.get_rect()
        self.rect.topleft = (self.x, self.y)

    def move(self):

        if self.direction == "east":
            self.x += 20
            self.rect.topleft = (self.x, self.y)


spaceship_group = pygame.sprite.Group()
asteroid_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
missiles_group = pygame.sprite.Group()

