from keystone import radio

with radio.Radio("/dev/ttyACM0") as r:
  print r.comm_version()
  print r.is_system_ready()
