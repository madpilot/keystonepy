from keystone.radio import Radio
from keystone.interface import Interface

if __name__ == "__main__":
  import sys

  def do_scan(self):
    radiostatus = 0
    freq = 0
    total_programs = 0

    if k.dab_auto_search(0, 40) == True:
      radiostatus = 1

      while radiostatus == 1:
        freq = k.get_frequency()
        total_programs = k.get_total_programs()
        print "Scanning index " + str(freq) + ", found " + str(total_programs) + " prgrams"
        radiostatus = k.get_play_status()

  scan = False
  k = Interface()
  if k.open_radio_port("/dev/ttyACM0"):
    if scan:
      do_scan()

    total_programs = k.get_total_programs()
    k.set_volume(10)
    k.set_stereo_mode(1)
    
    if total_programs > 0:
      k.play_stream(0, 4)
    else:
      k.play_stream(1, 95400)

    if total_programs > 0:
      print "Found " + str(total_programs) + " programs"

      for i in range(0, total_programs):
        name = k.get_program_name(0, i, 1)
        print "DAB Index=" + str(i) + ", Program Name=" + str(name)
        print k.get_ensemble_name(i, 1)

    playmode = k.get_play_mode()
    playindex = k.get_play_index()
    datarate = k.get_data_rate()

    print "Currently Playing " + k.get_program_name(playmode, playindex, 1) + " at " + str(datarate) + " kbps"

    while 1:
      k.get_play_status()
      text = k.get_program_text()
      if text != None:
        print text

  else:
    print "no"

  k.close_radio_port()
