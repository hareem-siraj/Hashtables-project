# import pygame

# WIDTH,HEIGHT = 900,500
# WIN = pygame.display.set_mode((WIDTH,HEIGHT))

# def main ():
#     run = True
#     while run:
#         for event in pygame.event.get():
#             if event.type==pygame.QUIT:
#                 run=False
#         WIN.fill((100,0,100))
#                   #  R   G  B
#         pygame.display.update()
#     pygame.quit()
        
# if __name__ == "__main__":
#     main()

import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 800
screen_height = 600

# Set the colors we'll be using
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
pink = (255, 192, 203)
light_pink = (250,218, 221)

# Create the Pygame screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the font and size for the text
font = pygame.font.Font(None, 36)

# Create the text surfaces
welcome_surface = font.render("WELCOME TO HASHSKIP", True, white)
welcome_rect = welcome_surface.get_rect(center=(screen_width/2, screen_height/3))

next_surface = font.render("Next", True, white)
next_rect = next_surface.get_rect(center=(screen_width/2, screen_height/2))

# Create the background surface
background = pygame.Surface(screen.get_size())
background.fill(pink)

# Add the text surfaces to the background
background.blit(welcome_surface, welcome_rect)
background.blit(next_surface, next_rect)

# Display the background
screen.blit(background, (0, 0))
pygame.display.flip()

# Set up variables for the second screen
second_screen = False

# Set up the text and buttons for the second screen
text_surface = font.render("WHAT OPERATION DO YOU WANT TO PERFORM?", True, white)
text_rect = text_surface.get_rect(center=(screen_width/2, screen_height/3))

insert_surface = font.render("INSERT", True, white)
insert_rect = insert_surface.get_rect(center=(screen_width/2, screen_height/2 - 50))

delete_surface = font.render("DELETE", True, white)
delete_rect = delete_surface.get_rect(center=(screen_width/2, screen_height/2))

search_surface = font.render("SEARCH", True, white)
search_rect = search_surface.get_rect(center=(screen_width/2, screen_height/2 + 50))

erase_surface = font.render("ERASE", True, white)
erase_rect = erase_surface.get_rect(center=(screen_width/2, screen_height/2 + 100))

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and next_rect.collidepoint(event.pos):
            # Show the second screen
            background.fill(pink)
            background.blit(text_surface, text_rect)
            background.blit(insert_surface, insert_rect)
            background.blit(delete_surface, delete_rect)
            background.blit(search_surface, search_rect)
            background.blit(erase_surface, erase_rect)
            screen.blit(background, (0, 0))
            pygame.display.flip()
            second_screen = True
        elif event.type == pygame.MOUSEBUTTONDOWN and second_screen:
            # Check which button was clicked
            if insert_rect.collidepoint(event.pos):
                print("INSERT button clicked")
            elif delete_rect.collidepoint(event.pos):
                print("DELETE button clicked")
            elif search_rect.collidepoint(event.pos):
                print("SEARCH button clicked")
            elif erase_rect.collidepoint(event.pos):
                print("ERASE button clicked")

        # elif event.type == pygame.MOUSEBUTTONDOWN and second_screen:
        #     # Check which button was clicked
        #     if insert_rect.collidepoint(event.pos):
        #         insert_surface.fill(light_pink)
        #         print("INSERT button clicked")
        #     elif delete_rect.collidepoint(event.pos):
        #         delete_surface.fill(light_pink)
        #         print("DELETE button clicked")
        #     elif search_rect.collidepoint(event.pos):
        #         search_surface.fill(light_pink)
        #         print("SEARCH button clicked")
        #     elif erase_rect.collidepoint(event.pos):
        #         erase_surface.fill(light_pink)
        #         print("ERASE button clicked")
        # elif event.type == pygame.MOUSEBUTTONUP and second_screen:
        #     # Change button color back to white on release
        #     insert_surface.fill(white)
        #     delete_surface.fill(white)
        #     search_surface.fill(white)
        #     erase_surface.fill(white)






# Quit Pygame
pygame.quit()

