class car:
    def __init__(self, initx, inity, initdir, initserviceB, initserviceT, initserviceE, initserviceO):
        self.x = initx
        self.y = inity
        self.direction = initdir  #top: 0, right: 1, bottom: 2, left: 3
        self.serviceB = initserviceB  #topleft: 0, topright: 1, botleft: 2, botright: 3
        self.serviceT = initserviceT
        self.serviceE = initserviceE
        self.serviceO = initserviceO