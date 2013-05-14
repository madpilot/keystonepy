from keystone.interface import Interface
from keystone.invalid_device_error import InvalidDeviceError

class Radio:
  def __init__(self, device, usehardmute = True):
    self.keystone = Interface()
    self.device = device
    self.usehardmute = usehardmute

  def __enter__(self):
    if self.keystone.open_radio_port(self.device, self.usehardmute) != True:
      raise InvalidDeviceError(self.device)
    
    return self

  def __exit__(self, type, value, traceback):
    self.keystone.close_radio_port
  
  def comm_version(self):
    return self.keystone.comm_version()

  def reset(self):
    self.keystone.hard_reset_radio()

  def is_system_ready(self):
    return self.keystone.is_sys_ready() == 1
