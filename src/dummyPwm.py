class dummyPwm:
    def __init__(self, address=0x40, busnum=0):
        self.address = address
        self.busnum = busnum
        self.freq = 0

    def set_pwm_freq(self, freq):
        self.freq = freq

    def set_pwm(self, servo, start, stop):
        pass