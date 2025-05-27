import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FONT = pygame.font.SysFont("consolas", 24)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text RPG Adventure")

# Story data
scenes = {
    "start": {
        "text": "You wake up in a dark forest. You see two paths.\n\n1. Take the left path\n2. Take the right path",
        "choices": {"1": "left_path", "2": "right_path"}
    },
    "left_path": {
        "text": "You encounter a sleeping dragon!\n\n1. Sneak past it\n2. Attack it",
        "choices": {"1": "sneak", "2": "attack"}
    },
    "right_path": {
        "text": "You find a treasure chest!\n\n1. Open it\n2. Leave it",
        "choices": {"1": "treasure", "2": "leave_chest"}
    },
    "sneak": {
        "text": "You successfully sneak past and escape the forest. You win!",
        "choices": {}
    },
    "attack": {
        "text": "The dragon wakes up and burns you. Game over.",
        "choices": {}
    },
    "treasure": {
        "text": "You found gold and a magic sword. You win!",
        "choices": {}
    },
    "leave_chest": {
        "text": "You walk away and fall into a trap. Game over.",
        "choices": {}
    }
}

# Game state
current_scene = "start"
user_input = ""

def draw_text(surface, text, y_offset=0):
    lines = text.split('\n')
    y = 50 + y_offset
    for line in lines:
        rendered = FONT.render(line, True, WHITE)
        surface.blit(rendered, (50, y))
        y += 30

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Draw current scene text
    scene = scenes[current_scene]
    draw_text(screen, scene["text"])
    draw_text(screen, f"> {user_input}", y_offset=300)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.key == pygame.K_RETURN:
                choice = user_input.strip()
                if choice in scene["choices"]:
                    current_scene = scene["choices"][choice]
                    user_input = ""
                else:
                    user_input = ""
            else:
                user_input += event.unicode

pygame.quit()
sys.exit()

