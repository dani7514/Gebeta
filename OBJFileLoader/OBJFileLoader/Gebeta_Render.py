import sys
import pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
import time
from Gebeta_Loader import *
import logic

import pygame
from pygame.locals import *
import sys


def render(angle, zpos, board):
    glTranslate(0, 0, - zpos)
    glRotate(90, 0, 0, 1)
    glRotate(angle, 0, 1, 0)
    board.render()
    glTranslate(0, 0, zpos)

# def renderText(value, pos, i):
#     font = pygame.font.SysFont('freesansbold.ttf', 40)
#     player_name  = font.render("Player" + str(i) + value, True, brown, blue)
#     text_data = pygame.image.tostring(player_name, "RGBA", True)
#     x, y = pos
#     glWindowPos2d(x, y)
#     glDrawPixels(player_name.get_width(), player_name.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)
#     pygame.display.flip()


def main():
    geez_number = {
        0: "0",
        1: '፩',
        2: '፪',
        3: '፫',
        4: '፬',
        5: '፭',
        6: '፮',
        7: '፯',
        8: '፰',
        9: '፱',
        10: '፲',
        11: '፲፩',
        12: '፲፪',
        13: '፲፫',
        14: '፲፬',
        15: '፲፭',
        16: '፲፮',
        17: '፲፯',
        18: '፲፰',
        19: '፲፱',
        20: '፳',
        21: '፳፩',
        22: '፳፪',
        23: '፳፫',
        24: '፳፬',
        25: '፳፭',
        26: '፳፮',
        27: '፳፯',
        28: '፳፰',
        29: '፳፱',
        30: '፴',
        31: '፴፩',
        32: '፴፪',
        33: '፴፫',
        34: '፴፬',
        35: '፴፭',
        36: '፴፮',
        37: '፴፯',
        38: '፴፰',
        39: '፴፱',
        40: '፵',
        41: '፵፩',
        42: '፵፪',
        43: '፵፫',
        44: '፵፬',
        45: '፵፭',
        46: '፵፮',
        47: '፵፯',
        48: '፵፰',
        49: '፵፱',
        50: '፶',
        51: '፶፩',
        52: '፶፪',
        53: '፶፫',
        54: '፶፬',
        55: '፶፭',
        56: '፶፮',
        57: '፶፯',
        58: '፶፰',
        59: '፶፱',
        60: '፷',
        61: '፷፩',
        62: '፷፪',
        63: '፷፫',
        64: '፷፬',
        65: '፷፭',
        66: '፷፮',
        67: '፷፯',
        68: '፷፰',
        69: '፷፱',
        70: '፸',
        71: '፸፩',
        72: '፸፪',
        73: '፸፫',
        74: '፸፬',
        75: '፸፭',
        76: '፸፮',
        77: '፸፯',
        78: '፸፰',
        79: '፸፱',
        80: '፹',
        81: '፹፩',
        82: '፹፪',
        83: '፹፫',
        84: '፹፬',
        85: '፹፭',
        86: '፹፮',
        87: '፹፯',
        88: '፹፰',
        89: '፹፱',
        90: '፺',
        91: '፺፩',
        92: '፺፪',
        93: '፺፫',
        94: '፺፬',
        95: '፺፭',
        96: '፺፮',
        97: '፺፯',
        98: '፺፰',
        99: '፺፱',
        100: '፻'
    }


    # Initialize Pygame
    pygame.init()

    # Set up the window
    viewport = (900,600)
    window_width, window_height = viewport
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Gebeta Game")

    # Set up fonts
    font_title1 = pygame.font.Font("AbyssinicaSIL-Regular.ttf", 50)
    font_title = pygame.font.Font("AbyssinicaSIL-Regular.ttf", 40)
    font_text = pygame.font.Font("AbyssinicaSIL-Regular.ttf", 30)

    # Set up colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Set up input fields
    player1_text = ""
    player2_text = ""
    player1_active = True
    player2_active = False
    PLAYER1 = (255, 255, 240, 255)
    PLAYER2 =  (70, 56, 51, 255)

    # Load background image
    background_image = pygame.image.load("Texture_Images/timber_light.jpg").convert()

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if player1_active:
                        player1_active = False
                        player2_active = True
                    elif player2_active:
                        if player1_text != "" and player2_text != "":
                            running = False
                elif event.key == K_BACKSPACE:
                    if player1_active:
                        player1_text = player1_text[:-1]
                    elif player2_active:
                        player2_text = player2_text[:-1]
                else:
                    if player1_active:
                        player1_text += event.unicode
                    elif player2_active:
                        player2_text += event.unicode

        # Clear the window
        window.blit(background_image, (0, 0))

        # Render the welcome text
        title_text = font_title.render("እንኳን ወደ ገበጣ ጨዋታ በደህና መጡ!", True, WHITE)
        title_text_rect = title_text.get_rect(center=(window_width // 2, 100))
        window.blit(title_text, title_text_rect)

        # Render the player name inputs
        player1_label = font_text.render("ተጨዋች ፩:", True, WHITE)
        player1_label_rect = player1_label.get_rect(midright=(window_width // 2 - 100, 200))
        window.blit(player1_label, player1_label_rect)
        pygame.draw.rect(window, WHITE, (player1_label_rect.right + 10, 180, 280, 50), 2)
        player1_input = font_text.render(player1_text, True, WHITE)
        player1_input_rect = player1_input.get_rect(midleft=(player1_label_rect.right + 15, 205))
        window.blit(player1_input, player1_input_rect)

        player2_label = font_text.render("ተጨዋች ፪:", True, WHITE)
        player2_label_rect = player2_label.get_rect(midright=(window_width // 2 - 100, 260))
        window.blit(player2_label, player2_label_rect)
        pygame.draw.rect(window, WHITE, (player2_label_rect.right + 10, 240, 280, 50), 2)
        player2_input = font_text.render(player2_text, True, WHITE)
        player2_input_rect = player2_input.get_rect(midleft=(player2_label_rect.right + 15, 265))
        window.blit(player2_input, player2_input_rect)

        # Render the start button
        start_button = pygame.draw.rect(window, WHITE, (window_width // 2 - 100, 320, 200, 50))
        start_text = font_text.render("ጨዋታ ጀምር", True, BLACK)
        start_text_rect = start_text.get_rect(center=start_button.center)
        window.blit(start_text, start_text_rect)

        # Check if the start button is clicked
        mouse_pos = pygame.mouse.get_pos()
        if start_button.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            if player1_text != "" and player2_text != "":
                running = False

        # Update the display
        pygame.display.update()

    # Retrieve player names and proceed to the main game
    player1_name = player1_text
    player2_name = player2_text
    print("Player 1:", player1_name)
    print("Player 2:", player2_name)



    game = logic.Game(player1_name, player2_name)
    brown = (210, 105, 30, 0)
    blue = (0, 0, 128, 0)
    
    angle = 0
    srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)
    # 194, 178, 128, 25
    BACKGROUND_COLOR = (146, 120, 110, 255)
    glClearColor(0.573, 0.471, 0.431, 1)
    glViewport(0, 0, 900, 600)

    glLightfv(GL_LIGHT0, GL_POSITION,  (-20, 200, 100, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    # LOAD OBJECT AFTER PYGAME INIT
    board = OBJ('GebetaData/gebeta_board.obj', swapyz=True)
    board.loadTexture('Texture_Images/timber_light3.jpg')
    board.generate()

    # LOAD BEAD IN PYGAME WINDOW
    bead = OBJ('BeadData/bead.obj', swapyz=True)
    bead.generate()

    clock = pygame.time.Clock()

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    width, height = viewport
    gluPerspective(90.0, width/float(height), 1, 100.0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_MODELVIEW)

    zpos = 10
    rotate = False
    move = False
    data = logic.Data()
    beadPositionDict = data.getBeads()

    is_starting = True
    while True:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        clock.tick(30)
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            elif e.type == KEYDOWN and e.key == K_ESCAPE:
                sys.exit()
            elif e.type == MOUSEBUTTONDOWN:
                # if e.button == 4: zpos = max(1, zpos-1)
                # elif e.button == 5: zpos += 1
                if e.button == 1:
                    rotate = True
                    pos = pygame.mouse.get_pos()
                    game.isValidMove(pos)
                    beadPositionDict = game.dataObj.getBeads()

                elif e.button == 3:
                    move = True
            elif e.type == MOUSEBUTTONUP:
                if e.button == 1:
                    rotate = False
                elif e.button == 3:
                    move = False

        if is_starting:
            render(angle, zpos, board)
            if angle == 380:
                is_starting = False
            angle += 5
            pass
        elif game.isEndGame == True:
            break
            
        else:
            font = pygame.font.SysFont('freesansbold.ttf', 40)
            # glRotate(180, 0, 0, 1)
           

            
            turn = (100, 475)

            if game.currentPlayer == game.player2:
                turn = (550, 475)
            result_text = font_text.render("ተረኛ፡ ", True, PLAYER1, BACKGROUND_COLOR)
            text_data = pygame.image.tostring(result_text, "RGBA", True)
            glWindowPos2d(turn[0], turn[1])
            glDrawPixels(result_text.get_width(), result_text.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

            result_text = font_title1.render("ገበጣ", True, PLAYER2, BACKGROUND_COLOR)
            text_data = pygame.image.tostring(result_text, "RGBA", True)
            glWindowPos2d(400, 475)
            glDrawPixels(result_text.get_width(), result_text.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)
            
            result_text = font.render(game.player1.name.upper(), True, PLAYER1, BACKGROUND_COLOR)
            text_data = pygame.image.tostring(result_text, "RGBA", True)
            glWindowPos2d(200, 500)
            glDrawPixels(result_text.get_width(), result_text.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

            result_text = font_text.render("{:^{padding}}".format(geez_number.get(game.player1.bank), padding=(len(game.player1.name)) // 2), True, PLAYER1, BACKGROUND_COLOR)
            text_data = pygame.image.tostring(result_text, "RGBA", True)
            glWindowPos2d(250, 450)
            glDrawPixels(result_text.get_width(), result_text.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

            result_text = font.render(game.player2.name.upper(), True, PLAYER2, BACKGROUND_COLOR)
            text_data = pygame.image.tostring(result_text, "RGBA", True)
            glWindowPos2d(650, 500)
            glDrawPixels(result_text.get_width(), result_text.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)
            result_text = font_text.render("{:^{padding}}".format(geez_number.get(game.player2.bank), padding=len(game.player2.name)), True, PLAYER2, BACKGROUND_COLOR)
            text_data = pygame.image.tostring(result_text, "RGBA", True)
            glWindowPos2d(650, 450)
            glDrawPixels(result_text.get_width(), result_text.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)
            
            start_pos = (50, 200)
            for val in game.board[:6]:
                glDrawPixels(result_text.get_width(), result_text.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)
                result_text = font_text.render("{:}".format(geez_number.get(val)), True, PLAYER2, BACKGROUND_COLOR)
                text_data = pygame.image.tostring(result_text, "RGBA", True)

                start_pos = (start_pos[0] + 105, start_pos[1])
                glWindowPos2d(start_pos[0], start_pos[1])
            
            start_pos = (50, 100)
            for val in game.board[6:]:
                glDrawPixels(result_text.get_width(), result_text.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)
                result_text = font_text.render("{:}".format(geez_number.get(val)), True, PLAYER2, BACKGROUND_COLOR)
                text_data = pygame.image.tostring(result_text, "RGBA", True)

                start_pos = (start_pos[0] + 105, start_pos[1])
                glWindowPos2d(start_pos[0], start_pos[1])

            glDrawPixels(result_text.get_width(), result_text.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)
            result_text = font_text.render("{:}".format(geez_number.get(game.board[-1])), True, PLAYER2, BACKGROUND_COLOR)
            text_data = pygame.image.tostring(result_text, "RGBA", True)

            start_pos = (start_pos[0] + 10, start_pos[1])
            glWindowPos2d(start_pos[0], start_pos[1])

            render(angle, zpos, board)


        for location in beadPositionDict.values():
           
            glTranslate(location[0], location[1], - zpos + location[2])
            bead.render()
            glTranslate(-location[0], -location[1], zpos - location[2])


        pygame.display.flip()
        
    screen = pygame.display.set_mode(viewport)
    pygame.display.set_caption("Game Over")

    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    GRAY = (128, 128, 128)

    # Set up fonts
    font_large = pygame.font.SysFont('freesansbold.ttf', 36)
    font_medium = pygame.font.SysFont('freesansbold.ttf', 24)

    # Set up buttons
    button_width, button_height = 180, 60
    button_padding = 20
    replay_button = pygame.Rect(
        (viewport[0] - button_width) // 2,
        viewport[1] // 2 - button_height // 2 - button_padding,
        button_width,
        button_height,
    )
    exit_button = pygame.Rect(
        (viewport[0] - button_width) // 2,
        viewport[1] // 2 + button_padding,
        button_width,
        button_height,
    )

    def endGame():
        if game.player1.getBank() > game.player2.getBank():
            return game.player1.name, game.player1.getBank()
        elif game.player2.getBank() > game.player1.getBank():
            return game.player2.name, game.player2.getBank()
        elif game.player1.getBank() == game.player2.getBank():
            return 'Draw'

    end_text, score = endGame()


    # Load background image
    background_image = pygame.image.load("Texture_Images/timber_light.jpg")
    background_image = pygame.transform.scale(background_image, (viewport[0], viewport[1]))

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if replay_button.collidepoint(mouse_pos):
                        print("Replay button clicked")
                        main()
                    elif exit_button.collidepoint(mouse_pos):
                        print("Exit button clicked")
                        running = False

        # Draw background image
        screen.blit(background_image, (0, 0))

        # Render game over text
        if (end_text == 'Draw'):
            winner_text = font_title.render("አቻ", True, WHITE)
        else:
            winner_text = font_title.render("አሸናፊ:  ", True, WHITE)
            winner_name_text = font_title.render(end_text.upper(), True, PLAYER1)

        score_text = font_text.render("ውጤት:  ", True, WHITE)
        score_value_text = font_text.render(geez_number.get(score), True, WHITE)
        replay_text = font_text.render("ድጋሚ", True, BLACK)
        exit_text = font_text.render("ውጣ", True, BLACK)

        # Draw game over text
        screen.blit(winner_text, (viewport[0] // 2 - winner_text.get_width() // 2 - winner_name_text.get_width() // 2, 100))
        if end_text != 'Draw':
            screen.blit(winner_name_text, (viewport[0] // 2 , 100))
        screen.blit(score_text, (viewport[0] // 2 - score_text.get_width() // 2 - score_value_text.get_width() // 2, 160))
        screen.blit(score_value_text, (viewport[0] // 2 + score_value_text.get_width(), 160))

        # Draw buttons
        pygame.draw.rect(screen, GRAY, replay_button)
        pygame.draw.rect(screen, GRAY, exit_button)
        pygame.draw.rect(screen, BLACK, replay_button, 5)
        pygame.draw.rect(screen, BLACK, exit_button, 5)
        screen.blit(replay_text, (replay_button.x + button_width // 2 - replay_text.get_width() // 2, replay_button.y + button_height // 2 - replay_text.get_height() // 2))
        screen.blit(exit_text, (exit_button.x + button_width // 2 - exit_text.get_width() // 2, exit_button.y + button_height // 2 - exit_text.get_height() // 2))

        # Update the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
