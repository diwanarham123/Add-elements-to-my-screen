import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My first game screen")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

rect_width, rect_height = 100, 50
rect_x = (WIDTH - rect_width) // 2
rect_y = (HEIGHT - rect_height) // 2
rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

font = pygame.font.Font(None, 36)
text_surface = font.render("Hello Pygame!", True, BLACK)
text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, rectangle)
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

pygame.quit()