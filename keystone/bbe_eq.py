class BBEEQ(object):
    def __init__(self, on, eq_mode, lo, hi, freq, mach_freq, mach_gain, mach_q, surr, mp, hpf, hi_ode):
        self.on = on
        self.eq_mode = eq_mode
        self.lo = lo
        self.hi = hi
        self.freq = freq
        self.mach_freq = mach_freq
        self.mach_gain = mach_gain
        self.mach_q = mach_q
        self.surr = surr
        self.mp = mp
        self.hpf = hpf
        self.hi_ode = hi_ode
