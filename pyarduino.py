from pyfirmata import Arduino, util
import user_password
board = Arduino(user_password.port())#change the port

def ledOn():
    board.digital[13].write(1)

def ledOff():
    board.digital[13].write(0)