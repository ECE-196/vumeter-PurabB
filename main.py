import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48, 
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39,
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

def volume_to_leds(volume, max_volume):
    num_leds = len(leds)
    led_count = int((volume / max_volume) * num_leds)
    return led_count

# main loop
while True:
    volume = microphone.value
    max_volume = 60000
    # max_volume = 6553
    print(volume)
    led_count = volume_to_leds(volume, max_volume)
    for i in range(len(leds)):
        if i < led_count:
            leds[i].value = True  # Turn LED on
        else:
            leds[i].value = False  # Turn LED off

    sleep(1)
