import numpy as np
from qam import Qam
from matplotlib import pyplot as plt

modulation = {
    '0000' : (1.4142, 135.0000),
    '0001' : (1.1180, 116.5650),
    '0010' : (1.4142,  45.0000),
    '0011' : (1.1180,  63.4350),
    '0100' : (1.4142, 225.0000),
    '0101' : (1.1180, 243.4350),
    '0110' : (1.4142, 315.0000),
    '0111' : (1.1180, 296.5650),
    '1000' : (1.1180, 153.4350),
    '1001' : (0.7071, 135.0000),
    '1010' : (1.1180,  26.5650),
    '1011' : (0.7071,  45.0000),
    '1100' : (1.1180, 206.5650),
    '1101' : (0.7071, 225.0000),
    '1110' : (1.1180, 333.4350),
    '1111' : (0.7071, 315.0000),
}

q1 = Qam(baud_rate = 10,
         bits_per_baud = 4,
         carrier_freq = 10e3,
         modulation = modulation)

q2 = Qam(baud_rate = 10,
         bits_per_baud = 4,
         carrier_freq = 9.9e3,
         modulation = modulation)

data = np.array([0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1])
array = ''.join([str(num) for num in data])

s = q1.generate_signal(array) + q2.generate_signal(array)

plt.figure(1)
#q.plot_constellation()
plt.figure(2)
s.plot(dB=False, phase=False, stem=False, frange=(0,12e3))
s.write_wav('result_16qam.wav')