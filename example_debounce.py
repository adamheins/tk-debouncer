from __future__ import print_function

import Tkinter as tk

from debouncer import Debouncer


class MyApp(object):
    def __init__(self):
        self.app = tk.Tk()
        self.debouncer = Debouncer(self._pressed_cb, self._released_cb)
        self.app.bind('<KeyPress-Right>', self.debouncer.pressed)
        self.app.bind('<KeyRelease-Right>', self.debouncer.released)


    def _pressed_cb(self, event):
        print('Pressed!')


    def _released_cb(self, event):
        print('Released!')


    def loop(self):
        self.app.mainloop()


def main():
    app = MyApp()
    app.loop()


if __name__ == '__main__':
    main()
