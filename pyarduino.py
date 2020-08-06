from pyfirmata import Arduino, util
board = Arduino("YOUR PORT")#change the port

def ledOn():
    board.digital[13].write(1)

def ledOff():
    board.digital[13].write(0)