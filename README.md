# tk-debounce
A simple utility class for debouncing key events in Python's
[Tkinter](https://wiki.python.org/moin/TkInter) GUI programming toolkit.

On my operating system, Ubuntu, a long press of a key is interpreted as a
sequence of press and release events. This is not useful if I want to perform
an action only at the start of the long press and/or only at the end of the
long press.

The script `debouncer.py` contains a class, `Debouncer`, which will implement
this behaviour. An example of the long-press behaviour with the `Debouncer` can
be found in the script `example_no_debounce.py`. An example of using the
`Debouncer` can be found in `example_debounce.py`.
