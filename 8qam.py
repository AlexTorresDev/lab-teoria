import numpy as np
from qam import Qam
from matplotlib import pyplot as plt

modulation = { 
    '000' : (0.5,   0),
    '001' : (0.5,  90),
    '010' : (0.5, 180),
    '011' : (0.5, 270),
    '100' : (1.0,   0),
    '101' : (1.0,  90),
    '110' : (1.0, 180),
    '111' : (1.0, 270),
}

q = Qam(
        baud_rate = 10,
        bits_per_baud = 3,
        carrier_freq = 50,
        modulation = modulation
    )

data = np.array([0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1])
array = ''.join([str(num) for num in data])

s = q.generate_signal(array)

plt.figure(1)
q.plot_constellation()
plt.figure(2)
s.plot(dB=False, phase=False, stem=False, frange=(0,500))
s.write_wav('result_8qam.wav')