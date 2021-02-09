""" McD-Game """

import arcade
import sys
import time

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 780
SCREEN_HEIGHT = 780
SCREEN_TITLE = "McD-Game"

MOVEMENT_SPEED = 5

TILE_SCALING = 0.5

COIN_SCALING = 0.5

PLAYER_SCALING = 0.3

WORKER_SCALING = 0.5

TABLE_SCALING = 1

EXIT_SCALING = 0.4
#BRUH

class Player(arcade.Sprite):

    def update(self):
        """ Move the player """
        # Move player.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class MyGame(arcade.Window):
    """ Main application class """

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.player_list = None

        # Set up the player info
        self.player_sprite = None

        #set up coin info
        self.coin_list = None

        # Set up worker info
        self.worker_list = None

        # Set up table info
        self.table_list = None

        # Set up exit info
        self.exit_list = None

        # Keep track of the score
        self.score = 0

        #Exit text
        self.exit = ""

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Set the background color
        #arcade.set_background_color(arcade.color.AMAZON)
        #arcade.set_background_color(arcade.csscolor.DARK_KHAKI)


    def setup(self):
        """ Set up the game and initialize the variables """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.worker_list = arcade.SpriteList()
        self.table_list = arcade.SpriteList()
        self.exit_list = arcade.SpriteList()

        # Score
        self.score = 0

        #exit text
        self.exit = ""


        # Set up the player
        self.player_sprite = Player(":resources:images/alien/alienBlue_front.png", PLAYER_SCALING)
        self.player_sprite.center_x = 390
        self.player_sprite.center_y = 500
        self.player_list.append(self.player_sprite)


        # --- Load in a map from the tiled editor ---

        # Name of map file to load
        map_name = "map.tmx"
        # Name of the layer in the file that has our platforms/walls
        platforms_layer_name = 'Platforms'
        # Name of the layer that has items for pick-up
        #coins_layer_name = 'Coins'

        # Read in the tiled map
        my_map = arcade.tilemap.read_tmx(map_name)

        # -- Platforms
        self.board_list = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=platforms_layer_name,
                                                      scaling=TILE_SCALING,
                                                      use_spatial_hash=True)

        # -- Coins
        #self.coin_list = arcade.tilemap.process_layer(my_map, coins_layer_name, TILE_SCALING)

    
        #Environment setup

           # Use a loop to place some coins for our character to pick up
        for x in range(128, 1250, 256):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", COIN_SCALING)
            coin.center_x = 90
            coin.center_y = 590
            self.coin_list.append(coin)

           # Use a loop to place a worker
        for x in range(128, 1250, 256):
            worker = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_jump.png", WORKER_SCALING)
            worker.center_x = 70
            worker.center_y = 400
            self.worker_list.append(worker)

           # Use a loop to place some tables
        for x in range(128, 1250, 256):
            table = arcade.Sprite("tableShortChairs1.png", TABLE_SCALING)
            table.center_x = 200
            table.center_y = 200
            self.table_list.append(table)

           # Use a loop to place some tables
        for x in range(128, 1250, 256):
            table = arcade.Sprite("tableShortChairs2.png", TABLE_SCALING)
            table.center_x = 700
            table.center_y = 400
            self.table_list.append(table)

         # Use a loop to place some tables
        for x in range(128, 1250, 256):
            table = arcade.Sprite("tableShortChairs3.png", TABLE_SCALING)
            table.center_x = 700
            table.center_y = 200
            self.table_list.append(table)

        # Use a loop to place some tables
        for x in range(128, 1250, 256):
            table = arcade.Sprite("tableShortChairs4.png", TABLE_SCALING)
            table.center_x = 450
            table.center_y = 200
            self.table_list.append(table)

            # Use a loop to place an exit
        for x in range(128, 1250, 256):
            exit = arcade.Sprite(":resources:images/tiles/signExit.png", EXIT_SCALING)
            exit.center_x = 30
            exit.center_y = 700
            self.exit_list.append(exit)


    def on_draw(self):
        """ Render the screen """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.board_list.draw()
        self.coin_list.draw()
        self.player_list.draw()
        self.worker_list.draw()
        self.table_list.draw()
        self.exit_list.draw()

        # Draw our score on the screen
        score_text = f"Monetos: {self.score}"
        arcade.draw_text(score_text, 10, 10, arcade.csscolor.WHITE, 18)

        #See if we hit the Exit
        exit_hit_list = arcade.check_for_collision_with_list(self.player_sprite, 
                                                            self.exit_list)

        #Draw the Exit text
        exit_text = f"""Do you wish to give up? if so, press Y. {self.exit}"""

        #draw exit text
        for exit in exit_hit_list:
            arcade.draw_text(exit_text, 100, 400, arcade.csscolor.DARK_RED, 18)



    def on_update(self, delta_time):
        """ Movement and game logic """

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED

        # Call update to move the sprite
        self.player_list.update()

        # See if we hit any coins
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.coin_list)

        # Loop through each coin we hit (if any) and remove it
        for coin in coin_hit_list:
            # Remove the coin
            coin.remove_from_sprite_lists()
            self.score=+1

        # See if we hit worker
        worker_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.worker_list)

        # Loop through each worker we hit (if any) and talk to them
        for worker in worker_hit_list:
            # Remove the coin
            pass

    def on_key_press(self, key, modifiers):
        """ Called whenever a key is pressed """
        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

        if key == arcade.key.Y:
            if len(arcade.check_for_collision_with_list(self.player_sprite, self.exit_list)) > 0:
                sys.exit()
            


    def on_key_release(self, key, modifiers):
        """ Called when the user releases a key """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()