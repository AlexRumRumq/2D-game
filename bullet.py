import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, my_game, x, y):
        Sprite.__init__(self)
        self.moving_right = my_game.player.moving_right
        self.moving_left = my_game.player.moving_left

        self.screen = my_game.screen
        self.screen_rect = my_game.screen.get_rect()

        self.image = pygame.Surface((67, 45))
        self.image.fill((254, 189, 255))
        self.rect = self.image.get_rect()

        self.bullet_speed = 15

        if self.moving_right:
            self.rect.midleft = x
            self.rect.midleft = y

        elif self.moving_left:
            self.rect.midright = x
            self.rect.midright = y

    def update(self):
        if self.moving_right:
            self.rect.x += self.bullet_speed
        elif self.moving_left:
            self.rect.x -= self.bullet_speed
        # Убить, если он заходит за верхнюю часть экрана
        if self.rect.right < 0:
            self.kill()
        if self.rect.left > self.screen_rect.right:
            self.kill()