from ctypes import *
from ctypes.util import *
from keystone import library_not_installed_error

class Interface:
  def __init__(self):
    libraries = find_library('keystonecomm') 
    if len(libraries) > 0:
      cdll.LoadLibrary(libraries)
      self.keystone = CDLL(libraries)
    else:
      raise LibaryNotInstalledError("Couldn't locate libkeystonecomm. Please check it is installed")


  def comm_version(self):
    return self.keystone.CommVersion()

  def open_radio_port(self, device, usehardmute = True):
    return self.keystone.OpenRadioPort(c_char_p(device), usehardmute)

  def hard_reset_radio(self):
    return self.keystone.HardResetRadio()

  def is_sys_ready(self):
    return self.keystone.IsSysReady()

  def close_radio_port(self):
    return self.keystone.CloseRadioPort()

  def set_volume(self, level):
    return self.keystone.SetVolume(c_char_p(level))

  def play_stream(self, mode, channel):
    return self.keystone.PlayStream(c_char_p(mode), c_long(channel))

  def stop_stream(self):
    return self.keystone.StopStream()

  def volume_plus(self):
    return self.keystone.VolumnPlus()

  def volume_minus(self):
    return self.keystone.VolumeMinus()

  def volume_mute(self):
    self.keystone.VolumeMute()

  def get_volume(self):
    return self.keystone.GetVolume()

  def get_play_mode(self):
    return self.keystone.GetPlayMode()

  def get_play_status(self):
    return self.keystone.GetPlayStatus()
  
  def get_total_program(self):
    return self.keystone.GetTotalProgram()
  
  def next_stream(self):
    return self.keystone.NextStream()

  def prev_stream(self):
    return self.keystone.PrevStream()

  def get_play_index(self):
    return self.keystone.GetPlayIndex()

  def get_signal_strength(self):
    return False

  def get_program_type(self):
    return False

  def get_program_text(self):
    buf = create_unicode_buffer(300)
    if self.keystone.GetProgramText(buf) == 0:
      return buf.value.strip()
    else:
      return None

  def get_program_name(self, mode, index, namemode):
    buf = create_unicode_buffer(300)
    if self.keystone.GetProgramName(c_char_p(mode), c_long(index), c_char_p(namemode), buf):
      return buf.value.strip()
    else:
      return ""

  def get_preset(self, mode, index):
    return self.keystone.GetPresetcc(c_char_p(mode), c_char_p(index))

  def set_preset(self, mode, index, channel):
    return self.keystone.SetPresetccm(c_char_p(mode), c_char_p(index), c_long(channel))

  def dab_auto_search(self, start_index, end_index):
    return self.keystone.DABAutoSearchhh(c_char_p(start_index), c_char_p(end_index))

  def dab_auto_search_no_clear(self, start_index, end_index):
    return self.keystone.DABAutoSearchNoClear(c_char_p(start_index), c_char_p(end_index))

  def get_ensemble_name(self, index, namemode):
    buf = create_unicode_buffer(300)
    if self.keystone.GetEnsembleName(c_long(index), c_char_p(namemode), buf):
      return buf.value.strip()
    else:
      return ""

  def get_data_rate(self):
    return self.keystone.GetDataRate()

  def set_stereo_mode(self, mode):
    return self.keystone.SetStereoMode(c_char_p(mode))

  def get_frequency(self):
    return self.keystone.GetFrequency()

  def get_stereo_mode(self):
    return self.keystone.GetStereoMode()

  def clear_database(self):
    return self.keystone.ClearDatabase()

  def set_bbeeq(self):
    return False

  def get_bbeeq(self):
    return False

  def set_headroom(self, headroom):
    return self.keystone.SetHeadroom(c_char_p(headroom))

  def get_headroom(self):
    return self.keystone.GetHeadroom()

  def get_application_type(self, index):
    return self.keystone.GetApplicationType(c_long(index))

  def get_program_info(self):
    return False

  def mot_query(self):
    return self.keystone.MotQuery()

  def get_image(self):
    return False

  def mot_reset(self):
    return False

  def get_dab_signal_quality(self):
    return self.keystone.GetDABSignalQuality()
