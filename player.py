import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self, my_game):
        Sprite.__init__(self)

        self.screen = my_game.screen
        self.screen_rect = my_game.screen.get_rect()

        # Создаем поверхность зеленого цвета и получаем прямоугольник
        self.image = pygame.image.load('images/1.PNG')
        self.image = pygame.transform.scale(self.image, (200, 250))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom[0], self.screen_rect.midbottom[0] - 40

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.player_speed = 8

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

        self.is_jump = False
        self.jump_count = 12

        self.animCount = 0

        self.walkRight = [pygame.image.load('images/right_1.jpg'), pygame.image.load('images/right_2.jpg'),
                          pygame.image.load('images/right_3.jpg'), pygame.image.load('images/right_4.jpg'),
                          pygame.image.load('images/right_5.jpg'), pygame.image.load('images/right_6.jpg'),
                          pygame.image.load('images/right_7.jpg'), pygame.image.load('images/right_8.jpg'),
                          pygame.image.load('images/right_9.jpg'), pygame.image.load('images/right_10.jpg'),
                          pygame.image.load('images/right_11.jpg'), pygame.image.load('images/right_12.jpg')]

        self.walkLeft = [pygame.image.load('images/left_1.jpg'), pygame.image.load('images/left_2.jpg'),
                         pygame.image.load('images/left_3.jpg'), pygame.image.load('images/left_4.jpg'),
                         pygame.image.load('images/left_5.jpg'), pygame.image.load('images/left_6.jpg'),
                         pygame.image.load('images/left_7.jpg'), pygame.image.load('images/left_8.jpg'),
                         pygame.image.load('images/left_9.jpg'), pygame.image.load('images/left_10.jpg'),
                         pygame.image.load('images/left_11.jpg'), pygame.image.load('images/left_12.jpg')]

    def update(self):
        """Обновляет позицию игрока с учетом флага."""
        # Обновление атрибута x, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.player_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.player_speed
        elif not self.moving_left and not self.moving_right:
            self.animCount = 0
        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def jump(self):
        if self.is_jump:
            if self.jump_count >= -12:
                if self.jump_count < 0:
                    self.y += (self.jump_count ** 2) / 2
                else:
                    self.y -= (self.jump_count ** 2) / 2
                self.jump_count -= 1
            else:
                self.is_jump = False
                self.jump_count = 12

    def blitme(self):
        if self.animCount + 1 >= 60:
            self.animCount = 0
        if self.moving_left:
            self.image = self.walkLeft[self.animCount // 5]
            self.image = pygame.transform.scale(self.image, (200, 250))
            self.image.set_colorkey((255, 255, 255))
            self.screen.blit(self.image, self.rect)
            self.animCount += 1
        elif self.moving_right:
            self.image = self.walkRight[self.animCount // 5]
            self.image = pygame.transform.scale(self.image, (200, 250))
            self.image.set_colorkey((255, 255, 255))
            self.screen.blit(self.image, self.rect)
            self.animCount += 1
        else:
            self.image = pygame.image.load('images/1.PNG')
            self.image = pygame.transform.scale(self.image, (200, 250))
            self.image.set_colorkey((255, 255, 255))
            self.screen.blit(self.image, self.rect)
