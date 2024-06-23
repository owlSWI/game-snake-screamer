import pygame
from random import randrange

RES = 800
SIZE = 50

x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 60
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
score = 0
speed_count, snake_speed = 0, 10

pygame.init()
surface = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
img = pygame.image.load('m_m_1644009690_59-phonoteka-org-p-fon-dlya-prezentatsii-televizor-60 (1).png').convert()
img2 = pygame.image.load('2TBh7m1jvvM.jpg').convert()


def close_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


game_over_sound_played = False


def game_over():
    global game_over_sound_played
    render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
    surface.blit(render_end, (RES // 2 - 200, RES // 3))
    surface.blit(pygame.transform.scale(img2, (RES, RES)), (0, 0))
    if not game_over_sound_played:
        pygame.mixer.init()
        game_over_sound = pygame.mixer.Sound('5.mp3')
        game_over_sound.play()
        game_over_sound_played = True
        pygame.display.flip()
        pygame.time.wait(int(game_over_sound.get_length() * 1000))  # Wait for the sound to finish
    pygame.quit()
    exit()


while True:
    surface.blit(img, (0, 0))

    [pygame.draw.rect(surface, pygame.Color('green'), (i, j, SIZE - 1, SIZE - 1)) for i, j in snake]
    pygame.draw.rect(surface, pygame.Color('red'), (*apple, SIZE, SIZE))

    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    surface.blit(render_score, (5, 5))

    speed_count += 1
    if not speed_count % snake_speed:
        x += dx * SIZE
        y += dy * SIZE
        snake.append((x, y))
        snake = snake[-length:]

    if snake[-1] == apple:
        apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        length += 1
        score += 1
        snake_speed -= 1
        snake_speed = max(snake_speed, 4)

    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        game_over()
        break

    pygame.display.flip()
    clock.tick(fps)
    close_game()

    key = pygame.key.get_pressed()

    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    elif key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    elif key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    elif key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}
