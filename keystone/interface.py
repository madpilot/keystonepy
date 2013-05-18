from ctypes import *
from ctypes.util import *
from keystone.library_not_installed_error import LibraryNotInstalledError
from keystone.program_info import ProgramInfo
from keystone.signal_strength import SignalStrength

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
        error = pointer(c_int(0))
        strength = self.keystone.GetSignalStrength(error)
        return SignalStrength(strength, error)

    def get_program_type(self, mode, index):
        return self.keystone.GetProgramType(c_char_p(mode), c_long_p(index))

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

    def set_bbeeq(self, bbe):
        return self.keystone.SetBBEEQ(
            c_char_p(bbe.on),
            c_char_p(bbe.eq_mode),
            c_char_p(bbe.lo),
            c_char_p(bbe.hi),
            c_char_p(bbe.freq),
            c_char_p(bbe.mach_freq),
            c_char_p(bbe.mach_gain),
            c_char_p(bbe.mach_q),
            c_char_p(bbe.surr),
            c_char_p(bbp.mp),
            c_char_p(bbe.hpf),
            c_char_p(bbe.hi_ode))

    def get_bbeeq(self):
        on = create_unicode_buffer(1) 
        eq_mode = create_unicode_buffer(1) 
        lo = create_unicode_buffer(1) 
        hi = create_unicode_buffer(1) 
        freq = create_unicode_buffer(1) 
        mach_freq = create_unicode_buffer(1) 
        mach_gain = create_unicode_buffer(1) 
        mach_q = create_unicode_buffer(1) 
        surr = create_unicode_buffer(1) 
        mp = create_unicode_buffer(1) 
        hpf = create_unicode_buffer(1) 
        hi_ode = create_unicode_buffer(1) 

        if self.keystone.getBBEEQ(on, eq_mode, lo, hi, freq, mach_freq, mach_gain, mach_q, surr, mp, hpf, hi_ode):
            return BBEEQ(on.value(), eq_mode.value(), lo.value(), hi.value(), freq.value(), mach_freq.value(), mach_gain.value(), mach_q.value(), surr.value(), mp.value(), hpf.value(), hi_ode.value())

        return False

    def set_headroom(self, headroom):
        return self.keystone.SetHeadroom(c_char_p(headroom))

    def get_headroom(self):
        return self.keystone.GetHeadroom()

    def get_application_type(self, index):
        return self.keystone.GetApplicationType(c_long(index))

    def get_program_info(self, index):
        service_component_id = create_unicode_buffer(300)
        service_id = pointer(c_int(0))
        ensemble_id = pointer(c_int(0))
        
        if self.keystone.GetProgramInfo(index, service_component_id, service_id, ensemble_id):
            return ProgramInfo(service_component_id.value.strip(), service_id[0], ensemble_id[0])
        else:
            return False

    def mot_query(self):
        return self.keystone.MotQuery()

    def get_image(self):
        buf = create_unicode_buffer(300)
        self.keystone.GetImage(buf)
        return buf.value.strip()

    def mot_reset(self, mode):
        self.keystone.MotReset(c_int(mode))

    def get_dab_signal_quality(self):
        return self.keystone.GetDABSignalQuality()
