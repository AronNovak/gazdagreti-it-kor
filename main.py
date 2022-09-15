# Snake game.

import time
import keyboard as keyboard

x = 0
y = 0

# I would like a cycle that never ends.
while True:

    # Listen to keypress "down".
    if keyboard.is_pressed('down'):
        y += 1

    # I would like to print enter character, as many times as the value of y.
    enters = "\n" * y
    print(enters)

    # I would like to increase the value of x by 1.
    x = x + 1

    # Let's wait one second before printing the next line.
    time.sleep(1)

    # Let's have a variable with spaces, as much as declared in i variable.
    spaces = " " * x

    # I would like to clear the screen.
    print("\033c")

    # Let"s print X with spaces variable in front of it.
    print(spaces + "X")

