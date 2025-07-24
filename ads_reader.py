import time
import board
import busio
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_ads1x15.ads1115 as ADS


def read_channel(channel: int) -> None:
    """Continuously read voltage from the specified ADS1115 channel."""
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2c)

    channel_map = {
        0: ADS.P0,
        1: ADS.P1,
        2: ADS.P2,
        3: ADS.P3,
    }

    if channel not in channel_map:
        raise ValueError("channel must be 0-3")

    chan = AnalogIn(ads, channel_map[channel])

    while True:
        print(f"Voltage: {chan.voltage:.3f} V\tRaw: {chan.value}")
        time.sleep(1)
