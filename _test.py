from keystone import radio

with radio.Radio("/dev/ttyACM0") as r:
  program = r.programs[4]
  r.volume = 5
  r.stereo = True

  program.play()
  
  print "Now playing: " + program.name + " at " + str(r.data_rate) + " kbs"
  print "Signal Quality: " + str(r.dab_signal_quality)
  while True:
    if r.status != -1:
      text = program.text
      if text != None:
        print text
