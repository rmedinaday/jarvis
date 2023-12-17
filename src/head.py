import servo
import importlib
import dummyPwm
try:
    import Adafruit_PCA9685
except ImportError:
    pass

class head:
    def __init__(self, config):
        self.config = config[self.__class__.__name__]
        self.servos = {}
        self.validate_config()
        self.bus = self.config['bus']
        self.address = self.config['address']
        self.freq = self.config['freq']
        importlib.import_module('time')
        try:
            self.controller = Adafruit_PCA9685.PCA9685(
                    address=self.address, busnum=self.bus)
        except NameError:
            self.controller = dummyPwm.dummyPwm(
                address=self.address, busnum=self.bus)
        self.controller.set_pwm_freq(self.freq)
        for name in self.config['servos'].keys():
            self.servos[name] = servo.servo(self.controller, name, self.config['servos'][name])
    
    def validate_config(self):
        params = self.config.keys()
        if 'bus' not in params:
            raise KeyError(f"Missing parameter 'bus' for {self.name}")
        if 'address' not in params:
            raise KeyError(f"Missing parameter 'address' for {self.name}")
        if 'freq' not in params:
            raise KeyError(f"Missing parameter 'freq' for {self.name}")
        if 'servos' not in params:
            raise KeyError(f"Missing parameter 'servos' for {self.name}")

    def neutral_face(self):
        for i in self.servos.keys():
            self.servos[i].move(self.servos[i].get_center())

    def random_face(self):
        for i in self.servos.keys():
            self.servos[i].move_random()
    
    def get_face(self):
        state = {}
        for i in self.servos.keys():
            state[i] = self.servos[i].get_position()
        return state