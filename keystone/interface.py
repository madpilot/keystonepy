from ctypes import *
from ctypes.util import *

# TODO Confirm the DLL names are correct. The documentation says they shouldn't be mangled
# (they are externed in the source) but they seem to be...
# Update: This *might* be to do with debug symbols? 
# http://stackoverflow.com/questions/2804893/c-dll-export-decorated-mangled-names

class Interface:
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
    return self.keystone._Z10NextStreamv()

  def prev_stream(self):
    return self.keystone._Z10PrevStreamv()

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

  def get_preset(self, mode, index):
    return self.keystone._Z9GetPresetcc(c_char_p(mode), c_char_p(index))

  def set_preset(self, mode, index, channel):
    return self.keystone._Z9SetPresetccm(c_char_p(mode), c_char_p(index), c_long(channel))

  def dab_auto_search(self, start_index, end_index):
    return self.keystone._Z13DABAutoSearchhh(c_char_p(start_index), c_char_p(end_index))

  def dab_auto_search_no_clear(self, start_index, end_index):
    return self.keystone._Z20DABAutoSearchNoClearhh(c_char_p(start_index), c_char_p(end_index))

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
    return self.keystone._Z13GetStereoModev()

  def clear_database(self):
    return self.keystone._Z13ClearDatabasev()

  def set_bbeeq(self):
    return False

  def get_bbeeq(self):
    return False

  def set_headroom(self, headroom):
    return self.keystone._Z11SetHeadroomc(c_char_p(headroom))

  def get_headroom(self):
    return self.keystone._Z11GetHeadroomv()

  def get_application_type(self, index):
    return self.keystone._Z18GetApplicationTypel(c_long(index))

  def get_program_info(self):
    return False

  def mot_query(self):
    return self.keystone._Z8MotQueryv()

  def get_image(self):
    return False

  def mot_reset(self):
    return False

  def get_dab_signal_quality(self):
    return self.keystone._Z19GetDABSignalQualityv()
