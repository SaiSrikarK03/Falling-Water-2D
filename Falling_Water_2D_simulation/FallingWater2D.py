import pygame
import random
import numpy as np

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Water Simulation")
WHITE = (255, 255, 255)
WATER = (0, 0, 255)  # Blue color for water
T = 10  # Smaller tile size for smoother water flow

class Grid:
    def __init__(self):
        self.grid = np.zeros((WIDTH * 2, HEIGHT + T))
        self.position = []

    def addWater(self, pointX, pointY):
        if pointX >= 0 and pointX <= WIDTH and pointY >= 0 and pointY <= HEIGHT:
            if self.grid[pointX][pointY] == 0:
                self.grid[pointX][pointY] = 1
                self.position.append((pointX, pointY))

    def update_position(self):
        new_position = []
        random.shuffle(self.position)  # Shuffle to create more fluid movement
        for points in self.position:
            listpoints = list(points)

            if points[1] >= HEIGHT - T:
                new_position.append(points)
            elif self.grid[points[0]][points[1] + T] == 0:
                # Move down if the space below is empty
                self.grid[points[0]][points[1]] = 0
                self.grid[points[0]][points[1] + T] = 1
                listpoints[1] += T
                new_position.append(tuple(listpoints))
            else:
                # Check both sides for space to move
                left_available = points[0] - T >= 0 and self.grid[points[0] - T][points[1]] == 0
                right_available = points[0] + T < WIDTH and self.grid[points[0] + T][points[1]] == 0

                if left_available and right_available:
                    # 50:50 chance to move left or right if both sides are free
                    a = random.choice([-1, 1])
                elif left_available:
                    a = -1
                elif right_available:
                    a = 1
                else:
                    a = 0

                if a != 0:
                    self.grid[points[0]][points[1]] = 0
                    self.grid[points[0] + a * T][points[1]] = 1
                    listpoints[0] += a * T
                    new_position.append(tuple(listpoints))
                else:
                    new_position.append(points)

        self.position = new_position

    def draw(self, win):
        for points in self.position:
            pygame.draw.rect(win, WATER, (points[0], points[1], T, T), 0)

def main():
    run = True
    WATER_DROP_DELAY = 5  # Set the delay in milliseconds
    water_dropping = False  # Flag to track if left mouse button is held down
    drop_timer = 0  # Timer to keep track of water drop delay
    water_simulation = Grid()

    while run:
        pygame.time.delay(10)
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                water_dropping = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Left mouse button released
                water_dropping = False

        # Continuously add water while left mouse button is held down
        if water_dropping:
            drop_timer += 1
            if drop_timer >= WATER_DROP_DELAY:
                pos = pygame.mouse.get_pos()
                water_simulation.addWater(pos[0] - pos[0] % T, pos[1] - pos[1] % T)
                drop_timer = 0  # Reset drop timer

        water_simulation.update_position()
        water_simulation.draw(WIN)

        pygame.display.update()

    pygame.quit()

main()
