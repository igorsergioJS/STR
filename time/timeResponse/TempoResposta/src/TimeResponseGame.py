import pygame
import random
import time

# Inicialização do Pygame
pygame.init()

# Configurações da tela
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Jogo de Digitação')

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# Fonte
font = pygame.font.Font(None, 74)

# Alfabeto
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def read_best_time(difficulty):
    try:
        with open(f'best_time_{difficulty}.txt', 'r') as file:
            return float(file.read())
    except FileNotFoundError:
        return None

def write_best_time(difficulty, time_seconds):
    with open(f'best_time_{difficulty}.txt', 'w') as file:
        file.write(str(time_seconds))

def draw_text(message, y, color=white, final=False):
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(screen_width // 2, y))
    screen.blit(text, text_rect)

def draw_letters(letter_colors, random_positions, random_letters):
    for i, letter in enumerate(random_letters):
        text = font.render(letter, True, letter_colors[i])
        screen.blit(text, random_positions[i])

def show_time(time_seconds, best_time=0, final=False):
    screen.fill(black)
    if final:
        draw_text("Fim do jogo", 250, white)
        draw_text(f" Tempo médio: {time_seconds:.2f} segundos", 350, white, final)
        draw_text("Pressione qualquer tecla para sair", 400, white)
        draw_text(f'Recorde: {best_time:.2f} segundos', 500, white)
    else:
        draw_text(f" Tempo: {time_seconds:.2f} segundos", 250, white, final)

    pygame.display.flip()

    if final:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    return

def show_start_screen():
    screen.fill(black)
    draw_text("Jogo da Digitação", 100)
    draw_text("Pressione:", 200)
    draw_text("1. Fácil - Sequencial", 260)
    draw_text("2. Difícil - Aleatório", 320)
    pygame.display.flip()

    difficulty = 1  # Modo fácil por padrão
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = 1  # Modo fácil
                    waiting = False
                elif event.key == pygame.K_2:
                    difficulty = 2  # Modo difícil
                    waiting = False

    return difficulty

def main():
    difficulty = show_start_screen()

    times = []
    counter = 0

    for _ in range(10):  # 10 etapas
        running = True
        random_letters = random.sample(letters, 4)

        if difficulty == 1:
            random_positions = [(screen_width // 2 - 150 + 100 * i, screen_height // 2) for i in range(4)]
        else:
            random_positions = [(random.randint(100, screen_width - 100), random.randint(100, screen_height - 100)) for _ in range(4)]

        letter_colors = [white] * 4
        start_time = time.time()

        while running:
            screen.fill(black)
            draw_text(f" {counter + 1} /10", 50)
            draw_letters(letter_colors, random_positions, random_letters)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    for i, letter in enumerate(random_letters):
                        if chr(event.key).upper() == letter:
                            letter_colors[i] = green
                            break

                    if all(color == green for color in letter_colors):
                        end_time = time.time()
                        stage_time = end_time - start_time
                        times.append(stage_time)
                        show_time(stage_time)
                        time.sleep(random.randint(2, 5))  # Delay entre as etapas
                        running = False

        counter += 1

    average_time = sum(times) / len(times)

    best_time = read_best_time(difficulty)
    if best_time is None or average_time < best_time:
        write_best_time(difficulty, average_time)
        best_time = average_time

    show_time(average_time, best_time,final=True)

    pygame.quit()

main()
