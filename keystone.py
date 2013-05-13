from ctypes import *
from ctypes.util import *

# TODO Confirm the DLL names are correct. The documentation says they shouldn't be mangled
# (they are externed in the source) but they seem to be...
# Update: This *might* be to do with debug symbols? 
# http://stackoverflow.com/questions/2804893/c-dll-export-decorated-mangled-names

class Keystone:
  def __init__(self):
    libraries = find_library('keystonecomm') 
    if len(libraries) > 0:
      cdll.LoadLibrary(libraries)
      self.keystone = CDLL(libraries)
    else:
      print "Nope"
      # TODO: Raise exception


  def comm_version(self):
    return self.keystone._Z11CommVersionv()

  def open_radio_port(self, device, usehardmute = True):
    return self.keystone._Z13OpenRadioPortPcb(c_char_p(device), usehardmute)

  def hard_reset_radio(self):
    return self.keystone._Z14HardResetRadiov()

  def is_sys_ready(self):
    return self.keystone._Z10IsSysReadyv()

  def close_radio_port(self):
    return self.keystone._Z14CloseRadioPortv()

  def set_volume(self, level):
    return self.keystone._Z9SetVolumec(c_char_p(level))

  def play_stream(self, mode, channel):
    return self.keystone._Z10PlayStreamcm(c_char_p(mode), c_long(channel))

  def stop_stream(self):
    return self.keystone._Z10StopStreamv()

  def volumne_plus(self):
    return self.keystone._Z10VolumnPlusv()

  def volume_minus(self):
    return self.keystone._Z11VolumeMinusv()

  def volume_mute(self):
    self.keystone._Z10VolumeMutev()

  def get_volume(self):
    return self.keystone._Z9GetVolumev()

  def get_play_mode(self):
    return self.keystone._Z11GetPlayModev()

  def get_play_status(self):
    return self.keystone._Z13GetPlayStatusv()
  
  def get_total_programs(self):
    return self.keystone._Z15GetTotalProgramv()
  
  def next_stream(self):
    return False

  def prev_stream(self):
    return False

  def get_play_index(self):
    return self.keystone._Z12GetPlayIndexv()

  def get_signal_strength(self):
    return False

  def get_program_type(self):
    return False

  def get_program_text(self):
    buf = create_unicode_buffer(300)
    if self.keystone._Z14GetProgramTextPw(buf) == 0:
      return buf.value.strip()
    else:
      return None

  def get_program_name(self, mode, index, namemode):
    buf = create_unicode_buffer(300)
    if self.keystone._Z14GetProgramNameclcPw(c_char_p(mode), c_long(index), c_char_p(namemode), buf):
      return buf.value.strip()
    else:
      return ""

  def get_present(self):
    return False

  def set_preset(self):
    return False

  def dab_auto_search(self, start_index, end_index):
    return self.keystone._Z13DABAutoSearchhh(c_char_p(start_index), c_char_p(end_index))

  def dab_auto_search_no_clear(self, start_index, end_index):
    return False

  def get_ensemble_name(self, index, namemode):
    buf = create_unicode_buffer(300)
    if self.keystone._Z15GetEnsembleNamelcPw(c_long(index), c_char_p(namemode), buf):
      return buf.value.strip()
    else:
      return ""

  def get_data_rate(self):
    return self.keystone._Z11GetDataRatev()

  def set_stereo_mode(self, mode):
    return self.keystone._Z13SetStereoModec(c_char_p(mode))

  def get_frequency(self):
    return self.keystone._Z12GetFrequencyv()

  def get_stereo_mode(self):
    return False

  def clear_database(self):
    return False

  def set_bbeeq(self):
    return False

  def get_bbeeq(self):
    return False

  def set_bbeeq(self):
    return False

  def set_headroom(self):
    return False

  def get_headroom(self):
    return False

  def get_application_type(self):
    return False

  def get_program_info(self):
    return False

  def mot_query(self):
    return False

  def get_image(self):
    return False

  def mot_reset(self):
    return False

  def get_dab_signal_quality(self):
    return False

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
k = Keystone()
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
