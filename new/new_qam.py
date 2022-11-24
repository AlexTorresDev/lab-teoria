import numpy as np
import matplotlib.pyplot as plt
from ModulationPy import QAMModem


class NewQam:

    QAM_signal = np.empty(0)
    modulate = np.empty(0)
    data = np.empty(0)
    modem: QAMModem

    def __init__(self, Nbits, fCarrier=50, fs=12000, baud=120):
        self.Nbits = Nbits
        self.fCarrier = fCarrier
        self.fs = fs
        self.baud = baud
        self.Ns = fs / baud
        self.N = Nbits * self.Ns
        self.t = np.r_[0.0:self.N] / fs

        self.modem = QAMModem(self.Nbits,
                              soft_decision=False,
                              bin_output=False)

    def generate_signal(self, data):
        self.data = data
        self.modulate = self.modem.modulate(data)

        for i in range(len(self.modulate)):
            QAM = (self.modulate[i].real.ravel() *
                   np.cos(2 * np.pi * self.fCarrier * self.t) +
                   self.modulate[i].imag.ravel() *
                   np.sin(2 * np.pi * self.fCarrier * self.t))
            self.QAM_signal = np.append(self.QAM_signal, QAM)

        return self.QAM_signal

    def plot_constellation(self):
        self.data = np.arange(2**self.Nbits)
        self.data = self.data.reshape(-1, 1)
        self.data = self.data.astype(complex)
        self.data = self.data * np.exp(1j * 2 * np.pi * self.fCarrier * self.t)
        plt.scatter(self.data.real, self.data.imag)
        plt.show()

    def plot_signal(self):
        tt = np.arange(0, len(self.t) * len(self.modulate))

        demodulate = self.modem.demodulate(self.modulate)
        bits = self.modem.de2bin(demodulate)
        x = [list(map(int, b)) for b in bits]
        x = np.concatenate(x, axis=0)

        fig = plt.figure(figsize=(16, 4))
        plt.plot(tt, self.QAM_signal.real)
        plt.xlabel('time [s]')
        plt.title(f'QAM={self.Nbits} of the sequence:' +
                  np.array2string(np.transpose(x)))
        plt.show()