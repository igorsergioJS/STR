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

# Função para centralizar e mostrar texto
def draw_text(message, y, color=white, final=False):
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(screen_width // 2, y))
    screen.blit(text, text_rect)

# Função para desenhar as letras
def draw_letters(letter_colors, random_positions, random_letters):
    for i, letter in enumerate(random_letters):
        text = font.render(letter, True, letter_colors[i])
        screen.blit(text, random_positions[i])

# Função para mostrar o tempo de cada etapa e o tempo médio final
def show_time(time_seconds, final=False):
    screen.fill(black)
    if final:
        draw_text(f"Tempo médio total: {time_seconds:.2f} segundos", 250, white, final=True)
        draw_text("Fim do jogo. Pressione qualquer tecla", 350, white)

    else:
        draw_text(f"Tempo desta etapa: {time_seconds:.2f} segundos", 250)
    pygame.display.flip()
    if final:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    return

# Função para a tela inicial
def show_start_screen():
    screen.fill(black)
    draw_text("Pressione qualquer tecla para iniciar", 250)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

# Main loop do jogo
def main():
    show_start_screen()

    times = []
    counter = 0

    for _ in range(10):  # 10 etapas
        running = True
        random_letters = random.sample(letters, 4)
        #random_positions = [(random.randint(100, screen_width - 100), random.randint(100, screen_height - 100)) for _ in range(4)]
        random_positions = [(screen_width // 2 - 150 + 100 * i, screen_height // 2) for i in range(4)]

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
    show_time(average_time, final=True)

    pygame.quit()

main()
