input.onButtonPressed(Button.A, function () {
    if (Seleccion > -3) {
        Seleccion += -1
    } else {
        Seleccion = 0
    }
})
input.onButtonPressed(Button.AB, function () {
    if (a == 0) {
        Change = 1
        if (Seleccion == -1 || Seleccion == 1) {
            a = 1
        } else if (Seleccion == -2 || Seleccion == 2) {
            a = 2
        } else if (Seleccion == -3 || Seleccion == 3) {
            a = 3
        }
    } else if (a > 0 && b > 0) {
        Change = 2
    } else {
        if (Seleccion == -1 || Seleccion == 1) {
            b = 1
        } else if (Seleccion == -2 || Seleccion == 2) {
            b = 2
        } else if (Seleccion == -3 || Seleccion == 3) {
            b = 3
        }
    }
})
input.onButtonPressed(Button.B, function () {
    if (Seleccion < 3) {
        Seleccion += 1
    } else {
        Seleccion = 0
    }
})
let Change = 0
let b = 0
let a = 0
let Seleccion = 0
Seleccion = 0
basic.showNumber(1)
basic.pause(200)
basic.showLeds(`
    . # . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    `)
basic.forever(function () {
    if (Change == 0) {
        if (Seleccion == 0) {
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                `)
        } else if (Seleccion == 1) {
            basic.showIcon(IconNames.SmallSquare)
        } else if (Seleccion == 2) {
            basic.showIcon(IconNames.Scissors)
        } else if (Seleccion == 3) {
            basic.showIcon(IconNames.Square)
        } else if (Seleccion == -1) {
            basic.showIcon(IconNames.SmallSquare)
        } else if (Seleccion == -2) {
            basic.showIcon(IconNames.Scissors)
        } else if (Seleccion == -3) {
            basic.showIcon(IconNames.Square)
        }
    }
    if (Change == 1) {
        basic.showNumber(2)
        basic.pause(100)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        Change = 0
        Seleccion = 0
    } else if (Change == 2) {
        if (a == 1 && b == 1 || (a == 2 && b == 2 || a == 3 && b == 3)) {
            basic.showIcon(IconNames.No)
            basic.pause(100)
            Seleccion = 0
            Change = 0
            a = 0
            b = 0
        } else if (a == 1 && b == 2 || (a == 2 && b == 3 || a == 3 && b == 1)) {
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                `)
            basic.showString("P1")
            basic.pause(100)
            Change = 0
            Seleccion = 0
            a = 0
            b = 0
        } else if (b == 1 && a == 2 || (b == 2 && a == 3 || b == 3 && a == 1)) {
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                `)
            basic.showString("P2")
            basic.pause(100)
            Seleccion = 0
            Change = 0
            a = 0
            b = 0
        }
    }
})
