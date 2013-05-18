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
        """
        Returns the name of the program
        """
        return self.interface.get_program_name(self.mode, self.index, 1)

    @property
    def type(self):
        """
        Returns the type of the program
        """
        return self.interface.get_program_type(self.mode, self.index)

    @property
    def text(self):
        """
        Returns the current DAB text. Often used for current song information
        """
        return self.interface.get_program_text()

    @property
    def application_type(self):
        """
        Returns the programs application type
        """
        return self.interface.get_application_type(self.index)

    @property
    def info(self):
        """
        Returns information about the program
        """
        return self.interface.get_program_info(self.index)

    def mot_query(self):
        """
        Query Mot to get images and other interesting files
        Returns True if successful, False if not
        """
        return self.interface.mot_query()

    def mot_reset(self, mode):
        """
        Resets the Mot state

        Keyword arguments: 
        mode: MOT_HEADER_MODE or MOT_DIRECTORY_MODE
        """
        self.interface.mot_reset(mode)


    @property
    def image(self):
        """
        Returns the DAB image. This is an image blob that can be decoded using an appropriate library
        """
        filename = self.interface.get_image()
        img = None
        f = open(filename, 'r')
        img = f.read()
        f.close()
        os.unlink(filename)
        return img

    @property
    def image_filename(self):
        """
        Returns a filename pointing at the current DAB image.
        The contents of this file will have an image that can be opened
        """
        return self.interface.get_image()
