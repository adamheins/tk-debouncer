from threading import Timer


# How long a single key press lasts (as opposed to a press-and-hold).
SINGLE_PRESS_MAX_SECONDS = 0.05


class Debouncer(object):
    ''' Debounces key events for Tkinter apps, so that press-and-hold works. '''
    def __init__(self, pressed_cb, released_cb):
        self.key_pressed = False
        self.key_released_timer = None

        self.pressed_cb = pressed_cb
        self.released_cb = released_cb


    def _key_released_timer_cb(self, event):
        ''' Called when the timer expires for a key up event, signifying that a
            key press has actually ended. '''
        self.key_pressed = False
        self.released_cb(event)


    def pressed(self, event):
        ''' Callback for a key being pressed. '''
        # If timer set by up is active, cancel it, because the press is still
        # active.
        if self.key_released_timer:
            self.key_released_timer.cancel()
            self.key_released_timer = None

        # If the key is not currently pressed, mark it so and call the callback.
        if not self.key_pressed:
            self.key_pressed = True
            self.pressed_cb(event)


    def released(self, event):
        ''' Callback for a key being released. '''
        # Set a timer. If it is allowed to expire (not reset by another down
        # event), then we know the key has been released for good.
        self.key_released_timer = Timer(SINGLE_PRESS_MAX_SECONDS,
                                        self._key_released_timer_cb, [event])
        self.key_released_timer.start()
