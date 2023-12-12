import Adafruit_PCA9685
import time
import random

class head:
    def __init__(self, config):
        self.config = config[self.__class__.__name__]
        self.eye_h_range = [self.config['eye_h']['left'], self.config['eye_h']['right']].sort()
        self.eye_v_range = [self.config['eye_v']['up'], self.config['eye_v']['down']].sort()
        self.jaw_range = [self.config['jaw']['open'], self.config['jaw']['closed']].sort()
        self.pwm = Adafruit_PCA9685.PCA9685(
                address=self.config['address'], busnum=self.config['bus'])
        self.pwm.set_pwm_freq(self.config['freq'])

    def neutral_face(self):
        self.pwm.set_pwm(self.config['jaw']['id'], 0, self.config['jaw']['closed'])
        self.pwm.set_pwm(self.config['eye_h']['id'], 0, self.config['eye_h']['center'])
        self.pwm.set_pwm(self.config['eye_v']['id'], 0, self.config['eye_v']['center'])
        self.pwm.set_pwm(self.config['turn']['id'], 0, self.config['turn']['center'])

    def random_face(self):
        eye_h_pulse = random.randrange(self.eye_h_range[0], self.eye_h_range[1])
        eye_v_pulse = random.randrange(self.eye_v_range[0], self.eye_v_range[1])
        jaw_pulse = random.randrange(self.jaw_range[0], self.jaw_range[1])
        self.pwm.set_pwm(self.config['eye_h']['id'], 0, eye_h_pulse)
        self.pwm.set_pwm(self.config['eye_v']['id'], 0, eye_v_pulse)
        self.pwm.set_pwm(self.config['jaw']['id'], 0, jaw_pulse)
