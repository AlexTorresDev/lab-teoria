import numpy as np
from qam import Qam
from matplotlib import pyplot as plt

q = Qam(16, baud_rate=10, carrier_freq=150)

data = np.array([0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1])
s = q.generate_signal(data)
plt.figure(1)
s.plot(dB=False, phase=False, stem=False, frange=(0, 12e3))
