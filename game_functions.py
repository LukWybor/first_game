import sys

import pygame

def check_keydown_events(event, ship):
    """Respond to keypresses"""
    
    #Move the ship to the right
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        
    #Move the ship to the left
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        
def check_keyup_events(event, ship):
    """Respond to key releases"""
    
    #Stops moving the ship to the right
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
        
    #Stops moving the ship to the left
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    
    
def check_events(ship):
    """Reaction to events generated by pressing a key 
    or a mouse button"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(game_settings, screen, ship):
    """Update images on the screen and flip to the new screen"""
    #Refresh the screen during each iteration of the loop
    screen.fill(game_settings.bg_color)
    ship.blitme()

    #Display the last modified screen
    pygame.display.flip()
