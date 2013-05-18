from keystone.constants import *
from keystone.interface import Interface
from keystone.program import Program
from keystone.invalid_device_error import InvalidDeviceError
from keystone.operation_failed_error import OperationFailedError

class Radio(object):
    def __init__(self, device, mode = DAB, usehardmute = True):
        self.interface = Interface()
        self.device = device
        self.mode = mode
        self.usehardmute = usehardmute
        self.currently_playing = None

    def __enter__(self):
        self.open() 
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    # Initialization functions
    def open(self):
        if self.interface.open_radio_port(self.device, self.usehardmute) != True:
            raise InvalidDeviceError(self.device)
        
    def close(self):
        self.interface.close_radio_port

    def comm_version(self):
        return self.interface.comm_version()

    def reset(self):
        if self.interface.hard_reset_radio() != True:
            raise OperationFailedError("Reset failed")

    def is_system_ready(self):
        return self.interface.is_sys_ready() == 1

    # Volume functions
    def mute(self):
        self.interface.volume_mute()

    @property
    def volume(self):
        return self.interface.get_volume()

    @volume.setter
    def volume(self, value):
        if value >= 0 and value <= 16:
            if self.interface.set_volume(value) == -1: 
                raise OperationFailedError("Set volume failed")

    # Control functions
    def prev_stream(self):
        if self.interface.prev_stream != True:
            raise OperationFailedError("Could not select the previous stream")
    
    def next_stream(self):
        if self.interface.next_stream != True:
            raise OperationFailedError("Could not select the next stream")

    def dab_auto_search(self, start_index, end_index, clear = True):
      if clear:
        if self.interface.dab_auto_search(start_index, end_index) == False:
          raise OperationFailedError("Auto-search failed")
      else:
        if self.interface.dab_auto_search_no_clear(start_index, end_index) == False:
          raise OperationFailedError("Auto-search failed")

    def ensemble_name(self, index, namemode):
      return self.interface.get_ensemble_name(index, namemode)

    def clear_database(self):
      if self.interface.clear_database() == False:
        raise OperationFailedError("Clear database failed")

    @property
    def bbeeq(self):
      return self.interface.get_bbeeq()

    @bbeeq.setter
    def bbeeq(self, bbe):
      self.interface.set_bbeeq(bbe)

    @property
    def headroom(self):
      return self.interface.get_headroom()

    @headroom.setter
    def headroom(self, headroom):
      self.interface.set_headroom(headroom)

    @property
    def status(self):
        return self.interface.get_play_status()

    @property
    def data_rate(self):
        return self.interface.get_data_rate()

    @property
    def stereo(self):
        return self.interface.get_stereo_mode() == 1

    @stereo.setter
    def stereo(self, value):
        if value == True:
            self.interface.set_stereo_mode(1)
        else:
            self.interface.set_stereo_mode(0)

    @property
    def signal_strength(self):
        return self.interface.get_signal_strength()

    @property
    def dab_signal_quality(self):
        return self.interface.get_dab_signal_quality()

    @property
    def programs(self):
        programs = self.interface.get_total_program()
        objs = []
        for i in range(0, programs):
            objs.append(Program(self, self.mode, i))

        return objs
