# hardware configuration
config = {
    "hx711": {
        "CLK": 29,
        "DAT": 31,
        "ref": 862  # calibration yields 100 g <-> readout 214500
    },
    "pca9685": {
        "freq": 60,
        "valvechannels": range(12),  # 0..11
        "valvepositions": [  # (open, closed)
            (375, 620),  # ch 0
            (375, 610),  # ch 1
            (375, 625),  # ch 2
            (350, 600),  # ch 3
            (365, 625),  # ch 4
            (370, 620),  # ch 5
            (400, 150),  # ch 6
            (360, 610),  # ch 7
            (380, 130),  # ch 8
            (400, 140),  # ch 9
            (380, 620),  # ch 10
            (370, 620)  # ch 11
        ],
        "fingerchannel": 12,
        "fingerpositions": (340, 515, 540),  # retracted, above bell, bell
        "lightpin": 22,
        "lightpwmchannel": 13,
        "lightpositions": (0, 500)
    },
    "a4988": {
        "ENABLE": 11,
        "MS1": 13,
        "MS2": 15,
        "MS3": 19,
        "RESET": 21,
        "SLEEP": 23,
        "STEP": 37,
        "DIR": 33,
        "numSteps": 350
    },
    "arm": {
        "SENSE": 16
    },
    "pump": {
        "MOTOR": 18
    },
    "ws2812": {
        "DIN": 12
    }
}
