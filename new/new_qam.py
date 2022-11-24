import numpy as np
import matplotlib.pyplot as plt

'''
    This class is used to generate a QAM signal.
'''
class NewQam:
    QAM_signal = np.empty(0)
    modulate = np.empty(0)
    data = np.empty(0)

    def __init__(self, Nbits = 8, fCarrier=50, fs=12000, baud=120):
        '''
            Constructor para QAM
            Nbits: number of bits
            fCarrier: carrier frequency
            fs: sampling frequency
            baud: baud rate
        '''
        self.Nbits = int(Nbits)
        self.fCarrier = fCarrier
        self.fs = fs
        self.baud = baud
        self.Ns = fs / baud
        self.N = Nbits * self.Ns
        self.t = np.r_[0.0:self.N] / fs

        self.m = [i for i in range(self.Nbits)]
        self.s = self.__qam_symbols()
        self.code_book = self.__create_constellation(self.m, self.s)

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

    def generate_signal(self, data):
        '''
            Generate QAM signal
            data: data to be transmitted on binary format
        '''
        self.data = data
        msg = data
        n = int(np.log2(self.Nbits))

        msg = [str(bit) for bit in msg]
        splited = ["".join(msg[i:i + n])
                   for i in range(0, len(msg), n)]  # subsequences of bits
        self.modulate = [self.code_book[s] for s in splited]

        for i in range(len(self.modulate)):
            QAM = (self.modulate[i].real.ravel() *
                   np.cos(2 * np.pi * self.fCarrier * self.t) +
                   self.modulate[i].imag.ravel() *
                   np.sin(2 * np.pi * self.fCarrier * self.t))
            self.QAM_signal = np.append(self.QAM_signal, QAM)

        return self.QAM_signal

    def plot_signal(self, figName='QAM signal'):
        '''
            Plot QAM signal
        '''
        tt = np.arange(0, len(self.t) * len(self.modulate))
        fig = plt.figure(figsize=(16, 4))
        plt.plot(tt, self.QAM_signal.real)
        plt.title(f'{self.Nbits}-QAM of {figName}')
        plt.xlabel('time [s]')
        plt.savefig(f'{self.Nbits}-QAM-{figName}.png')
        plt.show()
