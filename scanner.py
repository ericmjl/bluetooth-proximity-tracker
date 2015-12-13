import bluetooth
import time
from sense_hat import SenseHat

exit = False

sense = SenseHat()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
X = [255, 0, 0]  # Red
O = [0, 0, 0]  # Black
G = [0, 255, 0] # Green
success = [
    G, G, G, O, G, G, G, O,
    G, O, O, G, O, G, O, O,
    G, O, O, G, O, G, O, O,
    G, G, G, O, O, G, O, O,
    G, O, O, G, O, G, O, O,
    G, O, O, G, O, G, O, O,
    G, G, G, O, O, G, O, O,
    O, O, O, O, O, O, O, O
    ]

no_devices = [
    X, O, O, X, O, X, X, O,
    X, X, O, X, X, O, O, X,
    X, O, X, X, X, O, O, X,
    X, O, O, X, O, X, X, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O 
]

while not exit:
    nearby_devices = bluetooth.discover_devices(lookup_names=True, duration=2)
    
    if nearby_devices:
        # for i in range(10):
            # time.sleep(0.5)
        for device in nearby_devices:
            if "Eric's iPhone 6+" in device[1]:
                # sense.show_message(device[1])
                sense.set_pixels(success)
                # sense.show_message('In range')
    else:
        # for i in range(10):
        #    time.sleep(0.5)
        sense.set_pixels(no_devices)
        # sense.show_message('Out of range')
