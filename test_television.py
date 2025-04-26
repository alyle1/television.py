# test_television.py

import pytest
from television import Television

def test_init():
    tv = Television()
    assert not tv._status
    assert not tv._muted
    assert tv._volume == Television.MIN_VOLUME
    assert tv._channel == Television.MIN_CHANNEL

def test_power():
    tv = Television()
    tv.power()
    assert tv._status
    tv.power()
    assert not tv._status

def test_mute():
    tv = Television()
    tv.power()
    tv.mute()
    assert tv._muted
    tv.mute()
    assert not tv._muted

def test_channel_up():
    tv = Television()
    tv.power()
    tv._channel = Television.MAX_CHANNEL
    tv.channel_up()
    assert tv._channel == Television.MIN_CHANNEL
    tv.channel_up()
    assert tv._channel == Television.MIN_CHANNEL + 1

def test_channel_down():
    tv = Television()
    tv.power()
    tv._channel = Television.MIN_CHANNEL
    tv.channel_down()
    assert tv._channel == Television.MAX_CHANNEL
    tv.channel_down()
    assert tv._channel == Television.MAX_CHANNEL - 1

def test_volume_up():
    tv = Television()
    tv.power()
    tv._volume = Television.MAX_VOLUME
    tv.volume_up()
    assert tv._volume == Television.MAX_VOLUME  # Should stay at MAX_VOLUME
    tv._muted = True
    tv.volume_up()
    assert not tv._muted
    assert tv._volume == Television.MAX_VOLUME  # After unmute, still at max

def test_volume_down():
    tv = Television()
    tv.power()
    tv._volume = Television.MIN_VOLUME
    tv.volume_down()
    assert tv._volume == Television.MIN_VOLUME  # Should stay at MIN_VOLUME
    tv._muted = True
    tv.volume_down()
    assert not tv._muted
    assert tv._volume == Television.MIN_VOLUME  # After unmute, still at min
