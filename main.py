import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display 
width, height = 500, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Calculator")

# Colors
pastel = (204, 229, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

#import font 
font = pygame.font.Font(None, 36)


expression = ""
result = ""

#main code loop KEYDOWN and MOUSEBUTTONDOWN are used to get the input from the user and when "=" is pressed the expression is evaluated and the result is displayed
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                try:
                    result = str(eval(expression))
                except:
                    result = "Error"
                expression = ""
            elif event.key == pygame.K_BACKSPACE:
                expression = expression[:-1]
            else:
                expression += event.unicode
                
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_x, mouse_y = event.pos
                for button in buttons:
                    button_x, button_y = button[1] + button_radius, button[2] + button_radius
                    distance = pygame.math.Vector2(button_x - mouse_x, button_y - mouse_y).length()
                    if distance <= button_radius:
                        if button[0] == "=":
                            try:
                                result = str(eval(expression))
                            except:
                                result = "Error"
                            expression = ""
                        else:
                            expression += button[0]


    #sreen color 
    screen.fill(pastel)

    
    expression_text = font.render(expression, True, black)
    result_text = font.render(result, True, black)

    screen.blit(expression_text, (20, 20))
    screen.blit(result_text, (20, 60))

    #buttons radius and margin 
    button_radius = 30
    button_margin = 10

    #buttons coordinates (x , y) and text
    buttons = [
        ("7", 70, 170), ("8", 170, 170), ("9", 270, 170), ("/", 370, 170),
        ("4", 70, 270), ("5", 170, 270), ("6", 270, 270), ("*", 370, 270),
        ("1", 70, 370), ("2", 170, 370), ("3", 270, 370), ("-", 370, 370),
        ("0", 70, 470), (".", 170, 470), ("=", 270, 470), ("+", 370, 470),
    ]

    #draw buttons
    for button in buttons:
        pygame.draw.circle(screen, gray, (button[1] + button_radius, button[2] + button_radius), button_radius)
        button_text = font.render(button[0], True, black)
        text_rect = button_text.get_rect(center=(button[1] + button_radius, button[2] + button_radius))
        screen.blit(button_text, text_rect)

    #update display
    pygame.display.flip()

    #set fps
    pygame.time.Clock().tick(30)
