from __future__ import print_function

import Tkinter as tk


class MyApp(object):
    def __init__(self):
        self.app = tk.Tk()
        self.app.bind('<KeyPress-Right>', self._pressed_cb)
        self.app.bind('<KeyRelease-Right>', self._released_cb)


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
