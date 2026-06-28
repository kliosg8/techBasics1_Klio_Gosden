# Code Reading Exercise

## 1. Where did you find the code and why did you choose it? (Provide the link) 
https://github.com/msaad1999/GREY--Python3-2D-Game/blob/master/GREY.py

## 2. What does the program do? What's the general structure of the program?
This is a classic 2D arcade shooter built with Pygame, its the only code i found closest to my idea (2D Platformer Game). The player controls a jet and shoots enemy aircrafts while avoiding collisions and enemies, as the game goes on it gets harder and harder as long as you don't die.<br>

**The general structure contains:**

**1. Initialization**
- Importing modules
- Loading images
- Creating the game window
- loads timers, fonts etc

**2. Classes for:**
- Player
- Enemies
- Animations<br>
(which is something i am also doing for my game.)

**3. Game Functions**
- like game() and innergame() initialize the game and contain the main gameplay loop.


## 3. Function analysis: pick one function and analyze it in detail:

### 3.1 What does this function do?
Innergame() runs the actual game. It updates the player, enemies, bullets, animations, collisions, score, health bar, upgrades, and drawing every frame until the player dies or pauses the game.

### 3.2 What are the inputs and outputs?
**Inputs**<br>
It uses global variables:
- player
- score
- blockspeed1
- blockspeed2
- gametrack
- sprite groups (all_sprites, all_blocks, etc.)

**Outputs**<br>
It does not return a value.
Instead, it updates the game's state continuously and eventually calls gameover() when the player loses.

### 3.3 How does it work (step by step)?

- Hides the mouse cursor.
- Initializes variables such as health bar colour, upgrade flags and game state flags.
- Starts or changes the background music.
- Enters the main game loop (while not crash:).
- Handles player upgrades when certain scores are reached.
- Processes events:
    - keyboard input
    - mouse clicks
    - enemy spawning
    - pause menu
- Updates every sprite.
    - Checks all collisions:
    - bullets hitting enemies
    - enemy bullets hitting the player
    - bullets colliding with bullets
    - enemies colliding with the player
- Creates explosion animations and sound effects when collisions occur.
- Updates the score and health.
- Draws the scrolling background, clouds, sprites, health bar, score, and upgrade notifications.
- Updates the display and limits the frame rate to 60 FPS.
- When the player's health reaches zero, it plays the death  animation and opens the game over screen.

### 4. Takeaways: are there anything you can learn from the code? (How to structure your code, a clean solution for some function you might also need...)
- Since i haven't thought about main menus and UI yet this was insightful in the sense that now i have an idea of what the code could look like for that.
- Seeing all the different classes and functions made me more confident that what i'm doing for my game is going in the right direction.
- The Animation classes (Explosion and Upgrade_anim classes) show a clean way of creating frame-by-frame animations using a frame counter and update timer. This is useful to me because I also use sprite sheet animations for my player and enemies, and it took me a while to figure out how to use a sprite sheet for animation.
- I also haven't thought about the music in my game yet so seeing their handling of it definetly helps and gives me a base on it.

### 5. What parts of the code were confusing or difficult at the beginning to understand?
- The collision handling was kinda difficult to follow i think because its a huge bloch full of nested loops.
- The many variables in the beginning were also a lot, and i wasn't sure what all of them were

#### 5.1 Were you able to understand what it is doing after your own research?

Yes but i mostly understood stuff easier because of everything we have already worked on and because of what i've done for my own game.
