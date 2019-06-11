from time import sleep

# Install the adafruit ADC library using pip3
# pip3 install adafruit-ads1x15

import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)
GAIN = 2/3

while 1:
    value = [0]
    value[0]=adc.read_adc(0,gain=GAIN)
    volts = value[0]/32767.0 * 6.144