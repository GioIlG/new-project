def on_button_pressed_a():
    global Seleccion
    if Seleccion > -3:
        Seleccion += -1
    else:
        Seleccion = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Change, a, b
    if a == 0:
        Change = 1
        if Seleccion == -1 or Seleccion == 1:
            a = 1
        elif Seleccion == -2 or Seleccion == 2:
            a = 2
        elif Seleccion == -3 or Seleccion == 3:
            a = 3
    elif a > 0 and b > 0:
        Change = 2
    else:
        if Seleccion == -1 or Seleccion == 1:
            b = 1
        elif Seleccion == -2 or Seleccion == 2:
            b = 2
        elif Seleccion == -3 or Seleccion == 3:
            b = 3
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Seleccion
    if Seleccion < 3:
        Seleccion += 1
    else:
        Seleccion = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

Change = 0
b = 0
a = 0
Seleccion = 0
Seleccion = 0
basic.show_number(1)
basic.pause(200)
basic.show_leds("""
    . # . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    """)

def on_forever():
    global Change, Seleccion, a, b
    if Change == 0:
        if Seleccion == 0:
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                """)
        elif Seleccion == 1:
            basic.show_icon(IconNames.SMALL_SQUARE)
        elif Seleccion == 2:
            basic.show_icon(IconNames.SCISSORS)
        elif Seleccion == 3:
            basic.show_icon(IconNames.SQUARE)
        elif Seleccion == -1:
            basic.show_icon(IconNames.SMALL_SQUARE)
        elif Seleccion == -2:
            basic.show_icon(IconNames.SCISSORS)
        elif Seleccion == -3:
            basic.show_icon(IconNames.SQUARE)
    if Change == 1:
        basic.show_number(2)
        basic.pause(100)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        Change = 0
        Seleccion = 0
    elif Change == 2:
        if a == 1 and b == 1 or (a == 2 and b == 2 or a == 3 and b == 3):
            basic.show_icon(IconNames.NO)
            basic.pause(100)
            Seleccion = 0
            Change = 0
            a = 0
            b = 0
        elif a == 1 and b == 2 or (a == 2 and b == 3 or a == 3 and b == 1):
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                """)
            basic.show_string("P1")
            basic.pause(100)
            Change = 0
            Seleccion = 0
            a = 0
            b = 0
        elif b == 1 and a == 2 or (b == 2 and a == 3 or b == 3 and a == 1):
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                """)
            basic.show_string("P2")
            basic.pause(100)
            Seleccion = 0
            Change = 0
            a = 0
            b = 0
basic.forever(on_forever)
