# uwr25_remote/config.py

class GamepadConfig:
    def __init__(self):
        self.axis = ["LX", "LY", "RX", "RY"]
        self.button = ["X", "A", "B", "Y", "LB", "RB", "LT", "RT", "BACK", "START", "LS", "RS"]
        self.joystickmin = 40   
        self.checkdelay = 10

class SerialConfig:
    def __init__(self):
        self.speed = 115200
        self.timeout = 0.1
        self.skip_ports = ["COM3", "COM4"] 

class camera_setting:
    def __init__(self):
        self.camid = 0
        self.save_dir = './img'