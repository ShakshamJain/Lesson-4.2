import pygame
def main():
    pygame.init()
    screen_width, screen_height = 500,500
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Color Changing Sprite")
    colors = {
        'red':pygame.Color('red'),
        'blue':pygame.Color('blue'),
        'green':pygame.Color('green'),
        'yellow':pygame.Color('yellow'),
        'white':pygame.Color('white')
    }
    current_color = colors['white']
    