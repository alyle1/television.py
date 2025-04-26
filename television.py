class Television:
    # Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        # Initialize the Television with default settings.
        self._status: bool = False
        self._muted: bool = False
        self._volume: int = self.MIN_VOLUME
        self._channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        # Toggle the TV power status.
        self._status = not self._status

    def mute(self) -> None:
        # Mute or unmute the TV.
        if self._status:
            self._muted = not self._muted

    def channel_up(self) -> None:
        # Increase the channel number, wrapping as required.
        if self._status:
            if self._channel == self.MAX_CHANNEL:
                self._channel = self.MIN_CHANNEL
            else:
                self._channel += 1

    def channel_down(self) -> None:
        # Decrease the channel number, wrapping as required.
        if self._status:
            if self._channel == self.MIN_CHANNEL:
                self._channel = self.MAX_CHANNEL
            else:
                self._channel -= 1

    def volume_up(self) -> None:
        # Increase the volume, unmuting as required.
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume < self.MAX_VOLUME:
                self._volume += 1

    def volume_down(self) -> None:
        # Decrease the volume, unmuting as required.
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume > self.MIN_VOLUME:
                self._volume -= 1

    def __str__(self) -> str:
        # Return the TV's current status.
        current_volume = 0 if self._muted else self._volume
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {current_volume}"
