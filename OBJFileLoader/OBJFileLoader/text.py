def endGame():
                if game.player1.getBank() > game.player2.getBank():
                    return game.player1.name
                elif game.player2.getBank() > game.player1.getBank():
                    return game.player2.name
                elif game.player1.getBank() == game.player2.getBank():
                    return 'Draw'

            end_text = endGame()
            if end_text == "Draw":
                result_text = font_title.render("አቻ", True, BLACK, WHITE)
            else:
                result_text = font_title.render("አሸናፊ : " + end_text[0], True, BLACK, WHITE)
            text_data = pygame.image.tostring(result_text, "RGBA", True)
            glWindowPos2d(350, 300)
            glDrawPixels(result_text.get_width(), result_text.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)
            

            start_text = font_text.render("ድጋሚ ይጫወቱ", True, BLACK, WHITE)
            start_data = pygame.image.tostring(start_text, "RGBA", True)
            glWindowPos2d(350, 375)
            glDrawPixels(start_text.get_width(), start_text.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, start_data)
            

           
            pygame.display.flip()
            time.sleep(5)