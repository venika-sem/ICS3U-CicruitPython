#!/usr/bin/env python3

# Created by: Venika Sem
# Created on: Nov 2022
# This program is the "Space Aliens" program  on the PyBadge

import constants
import stage
import ugame


def game_scene():
    # This function is the main game game_scene

    # image banks for Cicruit Python
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    
    # buttons that you want to keep state information on
    a_button = constans.button_state["button_up"]
    b_button = constans.button_state["button_up"]
    start_button = constans.button_state["button_up"]
    select_button = constans.button_state["button_up"]

    # get sound ready
    pew_sound = open("pew.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # set background to image 0 in the image bank
    # and the size (10X8 tiles of size 16X16)
    backgrounf = stage,Grid(image_bank_background, 10, 8)

    # a sprite that will be updated every frame
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    alien = stage,Sprite(
        image_bank_sprites,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )

    # create a stage for the backgrounf to show up on
    # and set the frame rate 60fps
    game = stage.Stage(ugame.display, 60)

    # set layers of all sprites, items show up in  order
    game.layers = [ship] + [alien] [background]

    # render all sprites
    # most likely you will only render the backgrounf once per gaem scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

    # A button to fire
        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        if keys & ugame.K_RIGHT != 0:
            if ship.x > (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move((ship.x + constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move((constants.SCREEN_X - constants.SPRITE_SIZE), ship.y)

        if keys & ugame.K_LEFT != 0:
            if ship.x > 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(0, ship.y)

        # update game logic
        # play sound if A was just buttpm_just_pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)
        
        #redraw Sprite
        game.render_sprites([ship] + [alien])
        game.tick() #wait until refesh rate finishes


if __name__ == "__main__":
    game_scene()
