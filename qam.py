import numpy as np
from matplotlib import pyplot as plt
from sigproc import Signal


#################################
class Qam:
    #################################
    def __init__(self, m=8, baud_rate=10, carrier_freq=100):
        '''
        Create a modulator using OOK by default
        '''
        self.Nbits = m
        self.baud_rate = baud_rate
        self.carrier_freq = carrier_freq

        self.m = [i for i in range(self.Nbits)]
        self.s = self.__qam_symbols()
        self.code_book = self.__create_constellation(self.m, self.s)

    #################################
    def generate_signal(self, data):
        '''
        Generate signal corresponding to the current modulation scheme to
        represent given binary string, data.
        '''

        def create_func(data):
            n = int(np.log2(self.Nbits))
            data = [str(bit) for bit in data]
            splited = ["".join(data[i:i + n])
                       for i in range(0, len(data), n)]  # subsequences of bits
            amplitude = [self.code_book[s] for s in splited]

            def timefunc(t):
                slot = int(t * self.baud_rate)
                start = float(slot) / self.baud_rate
                offset = t - start

                return amplitude[slot].real * np.cos(
                    2 * np.pi * self.carrier_freq *
                    offset) + amplitude[slot].imag * np.sin(
                        2 * np.pi * self.carrier_freq * offset)

            return timefunc

        func = create_func(data)
        duration = float(len(data)) / (self.baud_rate * self.Nbits)
        s = Signal(duration=duration, func=func)
        return s

    def __gray_encoding(self, dec_in):
        '''
            Gray encoding
        '''
        bin_seq = [np.binary_repr(d, width=self.Nbits) for d in dec_in]
        gray_out = []
        for bin_i in bin_seq:
            gray_vals = [
                str(int(bin_i[idx])
                    ^ int(bin_i[idx - 1])) if idx != 0 else bin_i[0]
                for idx in range(0, len(bin_i))
            ]
            gray_i = "".join(gray_vals)
            gray_out.append(int(gray_i, 2))
        return gray_out

    def __create_constellation(self, m, s):
        '''
            Create constellation
        '''
        n = int(np.log2(self.Nbits))
        mg = self.__gray_encoding(m)
        mgb = [np.binary_repr(d, width=n) for d in mg]
        dict_out = {k: v for k, v in zip(mgb, s)}
        return dict_out

    def __qam_symbols(self):
        '''
            QAM symbols
        '''
        c = np.sqrt(self.Nbits)
        b = -2 * (np.array(self.m) % c) + c - 1
        a = 2 * np.floor(np.array(self.m) / c) - c + 1
        s = list((a + 1j * b))
        return s
