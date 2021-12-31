# Source at: https://www.youtube.com/watch?v=cFlk9kyFtS0
import pygame
import random
import math
import time

pygame.init()

display = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
FPS = 90
pygame.display.set_caption('Firework!!!')
Icon = pygame.image.load('Anh/heart.png')
pygame.display.set_icon(Icon)


def choose_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


class Streak():
    def __init__(self, x, y, color):
        self.color = color
        self.x = x
        self.y = y
        angle = random.uniform(-60, 240)
        velocity_mag = random.uniform(.3, 2.5)
        self.vx = velocity_mag * math.cos(math.radians(angle))
        self.vy = -velocity_mag * math.sin(math.radians(angle))
        self.timer = 0
        self.ended = False

    def get_angle(self):
        return math.atan2(-self.vy, self.vx)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.timer += 1
        if self.timer >= 90:
            self.ended = True

    def draw(self):
        angle = self.get_angle()
        length = 1
        dx = length * math.cos(angle)
        dy = length * math.sin(angle)
        a = [int(self.x + dx), int(self.y - dy)]
        b = [int(self.x - dx), int(self.y + dy)]
        pygame.draw.line(display, self.color, a, b, 1)


class Firework():
    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = 500
        self.velocity = random.uniform(3.5, 7)
        self.end_y = random.uniform(10, 250)
        self.ended = False

    def move(self):
        self.y -= self.velocity
        if self.y <= self.end_y:
            self.ended = True

    def draw(self):
        a = [self.x, int(self.y + 8)]
        b = [self.x, int(self.y - 8)]
        pygame.draw.line(display, (128, 128, 128), a, b, 2)


game_font = pygame.font.Font('font/Coastine Font.ttf', 100)


def draw_text(text):
    text_surface = game_font.render(text, True, (255, 255, 255))
    text_x = 400
    text_y = 250
    text_rect = text_surface.get_rect(center=(text_x, text_y))
    display.blit(text_surface, text_rect)


def update_time():
    curr_time = time.time()
    start = curr_time + 20
    end = start + 5
    return start, end


def game():
    start_time, end_time = update_time()
    fireworks = [Firework()]
    streaks = []
    pos = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if random.uniform(0, 1) <= 1 / 60:
            fireworks.append(Firework())

        display.fill((0, 0, 0))

        for firework in fireworks:
            firework.move()
            firework.draw()
            if firework.ended:
                colors = choose_random_color()
                streaks += [Streak(firework.x, firework.y, colors) for i in range(random.randint(20, 40))]
                fireworks.remove(firework)
        for streak in streaks:
            streak.move()
            streak.draw()
            if streak.ended:
                streaks.remove(streak)
        texts = ['HAPPY NEW YEAR', '2022', 'LOVE YOU']
        if start_time <= time.time() <= end_time:
            draw_text(texts[pos])
        elif time.time() >= end_time:
            start_time, end_time = update_time()
            pos = pos + 1 if pos + 1 <= len(texts) - 1 else 0

        pygame.display.update()
        clock.tick(FPS)


pygame.mixer.init()
bmg = pygame.mixer.Sound("sound/HappyNewYear.mp3")
sound = pygame.mixer.Sound("sound/firework_sound.mp3")
bmg.play(loops=0)
sound.play(loops=1000)
sound.set_volume(0.15)
game()
pygame.quit()
