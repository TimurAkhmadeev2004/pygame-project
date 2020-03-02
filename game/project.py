import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption("MyGame")

walkRight = [pygame.image.load('r0.png'),
             pygame.image.load('r1.png'),
             pygame.image.load('r2.png'),
             pygame.image.load('r3.png'),
             pygame.image.load('r4.png'),
             pygame.image.load('r5.png'),
             pygame.image.load('r6.png'),
             pygame.image.load('r7.png')]

walkLeft = [pygame.image.load('l0.png'),
            pygame.image.load('l1.png'),
            pygame.image.load('l2.png'),
            pygame.image.load('l3.png'),
            pygame.image.load('l4.png'),
            pygame.image.load('l5.png'),
            pygame.image.load('l6.png'),
            pygame.image.load('l7.png')]

playerStand = pygame.image.load('idle.png')

bg = pygame.image.load('bg.png')

zombie = pygame.image.load('z.png')

clock = pygame.time.Clock()

x = 50
a = False
x1 = 500 - 96
x2 = 5
y = 500 - 128 - 15 
width = 96
height = 128
speed = 7

z = False

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0
lastMove = "right"

class bul():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 20 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y),
                           self.radius)

def zom():
    global x1, x2, y
    if a:
        screen.blit(zombie, (x1, y))
        z = True
    else:
        screen.blit(zombie, (x2, y))
        z = True

def drawWin():
    global animCount
    
    screen.blit(bg, (0, 0))
    

    if animCount + 1 >= 40:
        animCount = 0

    if left:
        screen.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        screen.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        screen.blit(playerStand, (x, y)) 

    for bullet in bullets:
        bullet.draw(screen)
    pygame.display.update()

run = True
bullets = []
while run:
    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if lastMove == "right":
                    facing = 1
                else:
                    facing = -1
        
                if len(bullets) < 5:
                    bullets.append(bul(round(x + width // 2), round(y +
                    height // 2), 8, (0, 0, 0), facing))

    for bullet in bullets:
        if 0 < bullet.x < 500:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
        if a:
            if bullet.y in range(y, 500) and bullet.x in range(x1, x1 + 128):
                a = False
                bullets.pop(bullets.index(bullet))
                z = False
            else:
                screen.blit(zombie, (x1, y))
        else:
            if bullet.y in range(y, 500) and bullet.x in range(x2, x2 + 128):
                a = True
                bullets.pop(bullets.index(bullet))
                z = False

    keys = pygame.key.get_pressed()
    
    
    
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        lastMove = "left"
    elif keys[pygame.K_RIGHT] and (x < 500 - width - 5):
        x += speed
        left = False
        right = True
        lastMove = "right"
    else:
        left = False
        right = False
        animCount = 0
    if not isJump:
        if keys[pygame.K_UP]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10


    drawWin()
    
pygame.quit()
