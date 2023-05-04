import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the dimensions of the screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

# Define the size of the paddles
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 60

# Define the size of the ball
BALL_WIDTH = 15
BALL_HEIGHT = 15

class Paddle(pygame.sprite.Sprite):
    """A class to represent a paddle in the game"""
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([PADDLE_WIDTH, PADDLE_HEIGHT])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def move_up(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0
    
    def move_down(self, pixels):
        self.rect.y += pixels
        if self.rect.y > SCREEN_HEIGHT - PADDLE_HEIGHT:
            self.rect.y = SCREEN_HEIGHT - PADDLE_HEIGHT

class Ball(pygame.sprite.Sprite):
    """A class to represent the ball in the game"""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([BALL_WIDTH, BALL_HEIGHT])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.speed_x = 5
        self.speed_y = 5
        
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        if self.rect.y > SCREEN_HEIGHT - BALL_HEIGHT or self.rect.y < 0:
            self.speed_y = -self.speed_y
            
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = SCREEN_WIDTH // 2
            self.rect.y = SCREEN_HEIGHT // 2
            self.speed_x = 5
            self.speed_y = 5
            
        if self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH // 2
            self.rect.y = SCREEN_HEIGHT // 2
            self.speed_x = -5
            self.speed_y = -5
            
    def collide(self, sprite):
        if self.rect.colliderect(sprite.rect):
            self.speed_x = -self.speed_x
            self.speed_y = random.randint(-5, 5)
            
class Game:
    """A class to represent the game"""
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.font = pygame.font.Font(None, 36)
        self.player1 = Paddle(50, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.player2 = Paddle(SCREEN_WIDTH - 50 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.ball = Ball()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player1, self.player2, self.ball)
        self.player1_score = 0
        self.player2_score = 0
        
    def run(self):
        """Runs the game"""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                    elif event.key == pygame.K_UP:
                        self.player2.move_up(5)
                    elif event.key == pygame.K_DOWN:
                        self.player2.move_down(5)
                    elif event.key == pygame.K_w:
                        self.player1.move_up(5)
                    elif event.key == pygame.K_s:
                        self.player1.move_down(5)
                        
            self.ball.update()
            self.ball.collide(self.player1)
            self.ball.collide(self.player2)
            
            if self.ball.rect.x < 0:
                self.player2_score += 1
                self.ball.rect.x = SCREEN_WIDTH // 2
                self.ball.rect.y = SCREEN_HEIGHT // 2
                self.ball.speed_x = -5
                self.ball.speed_y = -5
                
            if self.ball.rect.x > SCREEN_WIDTH:
                self.player1_score += 1
                self.ball.rect.x = SCREEN_WIDTH // 2
                self.ball.rect.y = SCREEN_HEIGHT // 2
                self.ball.speed_x = 5
                self.ball.speed_y = 5
                
            self.screen.fill(BLACK)
            pygame.draw.line(self.screen, WHITE, [SCREEN_WIDTH // 2, 0], [SCREEN_WIDTH // 2, SCREEN_HEIGHT], 5)
            self.all_sprites.draw(self.screen)
            player1_text = self.font.render(str(self.player1_score), True, WHITE)
            player2_text = self.font.render(str(self.player2_score), True, WHITE)
            self.screen.blit(player1_text, (SCREEN_WIDTH // 4, 10))
            self.screen.blit(player2_text, (SCREEN_WIDTH * 3 // 4, 10))
            pygame.display.flip()
            
            self.clock.tick(60)
            
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()