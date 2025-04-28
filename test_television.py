import unittest
from television import Television

class TestTelevisionFunctions(unittest.TestCase):

    def test_init(self):
        tv = Television()
        tv_str = str(tv)
        self.assertIn("Power = False", tv_str)
        self.assertIn("Channel = 0", tv_str)
        self.assertIn("Volume = 0", tv_str)

    def test_power(self):
        tv = Television()
        tv.power()
        self.assertIn("Power = True", str(tv))
        tv.power()
        self.assertIn("Power = False", str(tv))

    def test_mute(self):
        tv = Television()
        # Try muting when TV is off
        tv.mute()
        self.assertIn("Volume = 0", str(tv))  # Should remain volume = 0

        # Turn on TV
        tv.power()
        tv.volume_up()  # Increase volume so not zero

        # Mute
        tv.mute()
        self.assertIn("Volume = 0", str(tv))  # Should mute volume to 0

        # Un-mute
        tv.mute()
        self.assertIn("Volume = 1", str(tv))  # Should restore actual volume

    def test_channel_up(self):
        tv = Television()
        current = str(tv)

        # Channel up when TV is off (should not change)
        tv.channel_up()
        self.assertEqual(str(tv), current)

        # Turn on TV
        tv.power()

        # Channel up normally
        tv.channel_up()
        self.assertIn("Channel = 1", str(tv))

        # Set to max channel and wrap around
        for _ in range(3):  # Go to MAX_CHANNEL
            tv.channel_up()
        self.assertIn("Channel = 0", str(tv))

    def test_channel_down(self):
        tv = Television()
        str(tv)

        # Channel down when TV is off (should not change)
        tv.channel_down()
