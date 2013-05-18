# Python Library for the Monkeyboard DAB/DAB+ FM Digital Radio Board

This library is a Python interface to the C++ library for the [Monkeyboard DAB/DAB+ FM Digital Radio Board](http://www.monkeyboard.org/products/85-developmentboard/85-dab-dab-fm-digital-radio-development-board-pro)

The library is made of two parts: an unpythonic-style interface, that is a basic wrapper around the C++ library, and a more pythonisque OOP interface.

## Setup

*Please note* This library requires the latest libkeystonecomm.so file, which has correctly exported library functions. We'll tell you how to check after the new version is released :)

1. Install the libkeystonecomm.so as per the instructions (TODO: Point to download)
2. Download this library
  ```
  git clone git@github.com:madpilot/keystonepy.git
  ```
3. Run
  ```bash
  sudo python setup.py install
  ```

## Including the library

```python
from keystone import *

with radio.Radio("/dev/ttyACM0") as r:
    # Select the fourth program from the ensemble
    program = r.programs[4]

    # Set the volume to 6 (Max is 16)
    r.volume = 6

    # Request stereo sound
    r.stereo = True

    # Play the selected program
    program.play()

    # Print the name of the program
    print "Now playing: " + program.name

    # Wait for text from the program
    while True:
      if r.status != -1:
        text = program.text

        if text != None:
          print text
```
