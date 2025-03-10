from pygame.sprite import Sprite

from dino_runner.utils.constants import HEART

class Heart(Sprite):
    def __init__(self, x_position):
        self.image = HEART
        self.rect = self.image.get_rect() #(pos_x, pos_y)
        self.rect.x = x_position
        self.rect.y = 20

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)