# Python Library for the Monkeyboard DAB/DAB+ FM Digital Radio Board

This library is a Python interface to the C++ library for the [Monkeyboard DAB/DAB+ FM Digital Radio Board](http://www.monkeyboard.org/products/85-developmentboard/85-dab-dab-fm-digital-radio-development-board-pro)

The library is made of two parts: an unpythonic-style interface, that is a basic wrapper around the C++ library, and a more pythonisque OOP interface.

## Setup

*Please note* This library requires the latest libkeystonecomm.so file, which has correctly exported library functions. We'll tell you how to check after the new version is released :)

1. Download and Install the libkeystonecomm.so as per these [instructions](http://www.monkeyboard.org/tutorials/78-interfacing/87-raspberry-pi-linux-dab-fm-digital-radio)
2. Download this library
  ```
  git clone git@github.com:madpilot/keystonepy.git
  ```
3. Run
  ```
  sudo python setup.py install
  ```

## Using the library

```python
from keystone.radio import Radio

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

## Documentation

It's ugly, but it's here:

http://htmlpreview.github.io/?https://github.com/madpilot/keystonepy/blob/master/docs/radio.html

http://htmlpreview.github.io/?https://github.com/madpilot/keystonepy/blob/master/docs/program.html

## Notes

1. I've only tested this on Linux, as I don't have access to a Windows machine with Python on it at the moment. It *should* work on Windows, and if it doesn't, it should be a minor fix. If you are a Windows user and know Python, feel free to fork and fix.
2. Not all of the methods have been tested fully. I'm working on this. Again, if you feel adventurous fork, test and patch away.
3. This is literally the second piece of Python I've ever written. If I've done something wrong, let me know.

## Contributing to keystonepy
 
* Check out the latest master to make sure the feature hasn't been implemented or the bug hasn't been fixed yet.
* Check out the issue tracker to make sure someone already hasn't requested it and/or contributed it.
* Fork the project.
* Start a feature/bugfix branch.
* Commit and push until you are happy with your contribution.
* Please try not to mess with the VERSION file. If you want to have your own version, or is otherwise necessary, that is fine, but please isolate to its own commit so I can cherry-pick around it.

## Copyright

Copyright (c) 2013 [MadPilot Productions](http://www.madpilot.com.au/). See LICENSE.txt for further details.
