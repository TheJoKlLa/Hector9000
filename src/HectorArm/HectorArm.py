class HectorArm(object):
    """docstring for HectorArm"""
    def __init__(self, PIN_Enable, PIN_Reset, PIN_Sleep, PIN_Step, PIN_Direction, PIN_Endstop, Steps, devEnv = False):
        
        print("HectorArm: Init HectorArm")
        self.PIN_Enable = PIN_Enable
        self.PIN_Reset = PIN_Reset
        self.PIN_Sleep = PIN_Sleep
        self.PIN_Step = PIN_Step
        self.PIN_Direction = PIN_Direction
        self.PIN_Endstop = PIN_Endstop # Pin of the Optical Endstop

        # Steps between IN and OUT Position
        if devEnv and not isinstance(Steps, int):
            raise ValueError("Steps must be type of int")
        self.Steps = Steps

        # SetUp GPIO
        if not self.devEnv:
            print("HectorArm: SetUp GPIO PINs")

            GPIO.setup(self.PIN_Enable, GPIO.OUT)
            GPIO.setup(self.PIN_Reset, GPIO.OUT)
            GPIO.setup(self.PIN_Sleep, GPIO.OUT)
            GPIO.setup(self.PIN_Enable, GPIO.OUT)
            GPIO.setup(self.PIN_Direction, GPIO.OUT)

            GPIO.output(self.PIN_Enable, True)
            GPIO.output(self.PIN_Sleep, True)
            GPIO.output(self.PIN_Reset, True)

            GPIO.setup(self.arm, GPIO.IN)

    # Moves the Arm to OUT Position
    def move_out(self):

        print("HectorArm: Move Arm to OUT")

         # Enable Arm and Move Direction
        if not self.devEnv:
            GPIO.output(self.PIN_Enable, False)
            GPIO.output(self.PIN_Direction, True)

        # Move Arm
        while not self.arm_pos():
            if not self.devEnv:
                GPIO.output(self.PIN_Step, False)
                time.sleep(.001)
                GPIO.output(self.PIN_Step, True)
                time.sleep(.001)
        
        # Disable Arm
        if not self.devEnv:
            GPIO.output(self.PIN_Enable, True)

        print("HectorArm: Arm is moved to OUT Position")

    # Move the Arm to IN Position
    def move_in(self):

        print("HectorArm: Move Arm to IN")
        
        # Moves Arm first to OUT to go in by Steps
        self.arm_out()

        # Enable Arm
        if not self.devEnv:
            GPIO.output(self.PIN_Enable, False)
            GPIO.output(self.PIN_Direction, False)

        # Move Arm
        if not self.devEnv:
            for i in range(self.Steps):
                GPIO.output(self.PIN_Step, False)
                time.sleep(.001)
                GPIO.output(self.PIN_Step, True)
                time.sleep(.001)
        
        # Disable Arm
        if not self.devEnv:
            GPIO.output(self.PIN_Enable, True)
        
        print("HectorArm: Arm is moved to OUT Position")

    # Move the Arm to OUT Position with specifc Steps
    # Negativ Values are allowed
    def move_out_BySteps(self, steps):

        if not isinstance(steps, int):
            raise ValueError("steps must be type of int")

        print("HectorArm: Move Arm out by %d Steps" % (steps))

        # Enable Arm
        if not self.devEnv:
            GPIO.output(self.PIN_Enable, False)

            if steps > 0:
                GPIO.output(self.PIN_Direction, True)
            else:
                GPIO.output(self.PIN_Direction, False)

        # Move Arm
        if not self.devEnv:
            for i in range(steps):
                GPIO.output(self.PIN_Step, False)
                time.sleep(.001)
                GPIO.output(self.PIN_Step, True)
                time.sleep(.001)
        
        # Disable Arm
        if not self.devEnv:
            GPIO.output(self.PIN_Enable, True)
        
        print("HectorArm: Arm is moved out by %d Steps" % (steps))

    # Returns True if Endstop is reached
    def arm_pos(self):

        if not self.devEnv:
            pos = GPIO.input(self.arm)
        else:
            pos = 100

        pos = (pos != 0)

        if pos:
            print("HectorArm: Arm Position is OUT: True")
        else:
            print("HectorArm: Arm Position is OUT: False")
        
        return pos