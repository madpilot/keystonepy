from keystone import radio

with radio.Radio("/dev/ttyACM0") as r:
    program = r.programs[4]
    r.volume = 6
    r.stereo = True

    program.play()
    
    print "Now playing: " + program.name
    while True:
        if r.status != -1:
            text = program.text

            if text != None:
                print text
