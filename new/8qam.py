import numpy as np
from new_qam import NewQam

data = np.array([0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1])

qam = NewQam(16, fCarrier=50, fs=12000, baud=120)
qam.generate_signal(data)
#qam.plot_constellation()
qam.plot_signal()