import pygame

class ChickenJump:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Chicken jump")

        self.screen = pygame.display.set_mode((1000, 200))
        self.clock = pygame.time.Clock()

    def paint(self):
        self.screen.fill("white")

        for x in range(11):
            pygame.draw.line(self.screen, "black", (x * 100, 0), (x * 100, 200), 2)

        for y in range(3):
            pygame.draw.line(self.screen, "black", (0, y * 100), (1000, y * 100), 2)

        pygame.draw.circle(self.screen, "blue", (self.ball_x * 100 + 50, (1 - self.ball_y) * 100 + 50), 40)
        pygame.draw.rect(self.screen, "black", pygame.Rect(500, 100, 100, 100))
        pygame.display.flip()
    
    def reset(self):
        self.ball_x = 0
        self.ball_y = 0
        self.terminated = False

        self.paint()
        return 0

    def action(self, action):
        self.clock.tick(10)

        if self.ball_x < 9:
            self.ball_x += 1
        else:
            self.terminated = True
        
        self.ball_y = action

        # Collision means death
        if self.ball_x == 5 and self.ball_y == 0:
            reward = -10
            self.terminated = True
        
        # Flying takes energy
        elif self.ball_y == 1:
            reward = -0.1
        
        # Walking is easier
        else:
            reward = 0

        state = self.ball_y * 10 + self.ball_x

        self.paint()
        return state, reward      
    
    def close(self):
        pygame.quit()
