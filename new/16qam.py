import numpy as np
from new_qam import NewQam

data = np.array([1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0,
                 0])  #20 bits
qam = NewQam(16, fCarrier=50, fs=12000, baud=120)
qam.generate_signal(data)
qam.plot_signal('Primera señal')

data2 = np.array(
    [0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1])
qam2 = NewQam(16, fCarrier=50, fs=12000, baud=120)
qam2.generate_signal(data2)
qam2.plot_signal('Segunda señal')
