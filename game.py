import pygame, sys
from player import Player
from bullet import Bullet


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1500, 800))
        pygame.display.set_caption('Runner!')
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.player = Player(self)
        self.bg = pygame.image.load('images/bg.png')
        self.bg = pygame.transform.scale(self.bg, (1500, 800))

        self.bullets = pygame.sprite.Group()

    def shoot(self):
        """Метод для стрельбы игрока вверх."""
        if self.player.moving_right:
            bullet = Bullet(self, self.player.rect.midright, self.player.rect.midright)
            self.bullets.add(bullet)
        elif self.player.moving_left:
            bullet = Bullet(self, self.player.rect.midleft, self.player.rect.midleft)
            self.bullets.add(bullet)

    def update_screen(self):
        self.player.jump()
        self.player.update()
        self.bullets.update()

        self.screen.blit(self.bg, (0, 0))
        self.player.blitme()
        self.bullets.draw(self.screen)

        pygame.display.flip()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    if event.key == pygame.K_d:
                        self.player.moving_right = True
                    if event.key == pygame.K_a:
                        self.player.moving_left = True
                    if event.key == pygame.K_KP_ENTER:
                        self.shoot()
                    if not self.player.is_jump:
                        if event.key == pygame.K_SPACE:
                            self.player.is_jump = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.player.moving_right = False
                    if event.key == pygame.K_a:
                        self.player.moving_left = False
            self.update_screen()
            self.clock.tick(self.fps)


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    game = Game()
    game.run_game()
