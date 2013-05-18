from keystone.operation_failed_error import OperationFailedError
import os

class Program(object):
    def __init__(self, radio, mode, index):
        self.radio = radio
        self.interface = radio.interface
        self.mode = mode
        self.index = index

    def play(self):
        if self.interface.play_stream(self.mode, self.index) != True:
            raise OperationFailedError("Could not play stream: " + str(self.index))
        
        self.radio.currently_playing = self

    def stop(self):
        if self.interface.stop_stream() != True:
            raise OperationFailedError("Could not stop stream: " + str(self.index))
      
        self.radio.currently_playing = None

    @property
    def name(self):
        return self.interface.get_program_name(self.mode, self.index, 1)

    @property
    def type(self):
        return self.interface.get_program_type(self.mode, self.index)

    @property
    def text(self):
        return self.interface.get_program_text()

    @property
    def application_type(self):
        return self.interface.get_application_type(self.index)

    @property
    def info(self):
        return self.interface.get_program_info(self.index)

    def mot_query(self):
      if self.mot_query() == False:
        raise OperationFailedError("Mot Query failed")

    @property
    def image(self):
        filename = self.interface.get_image()
        img = None
        f = open(filename, 'r')
        img = f.read()
        f.close()
        os.unlink(filename)
        return img

    @property
    def image_filename(self):
        return self.interface.get_image()
