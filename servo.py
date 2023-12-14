import random

class servo:
    def __init__(self, controller, name, config):
        self.controller = controller
        self.name = name
        self.config = config
        self.enabled = False
        self.position = 0
        self.validate_config()
        self.move(self.center)

    def validate_config(self):
        params = self.config.keys()
        if 'id' not in params:
            raise KeyError(f"Missing parameter 'id' for servo {self.name}")
        if 'min' not in params:
            raise KeyError(f"Missing parameter 'min' for servo {self.name}")
        if 'max' not in params:
            raise KeyError(f"Missing parameter 'max' for servo {self.name}")
        if 'center' not in params:
            self.config['center']  = round((min + max)/2)
        if ('enabled' in params and self.config['enabled'] == 1):
            self.enabled = True
        self.id = self.config['id']
        self.min = min(self.config['min'], self.config['max'])
        self.max = max(self.config['min'], self.config['max'])
        if (self.config['center'] > self.max or self.config['center'] < self.min):
            raise ValueError(f"Invalid parameter 'center' for servo {self.name}")
        else:
            self.center = self.config['center']

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def get_state(self):
        return self.enabled
    
    def get_min(self):
        return self.min
    
    def get_center(self):
        return self.center
    
    def get_max(self):
        return self.max
    
    def get_position(self):
        return self.position
    
    def move(self, position):
        if (position > self.max or position < self.min):
            raise ValueError(f"Invalid position {position} for servo {self.name}")
        elif self.enabled:
            self.controller.set_pwm(self.id, 0, position)
            self.position = position

    def move_random(self):
        position = random.randrange(self.min, self.max)
        self.move(position)
