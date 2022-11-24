import matplotlib.pyplot as plt
import numpy as np

mapping_table = {
    (0,0,0,0) : -3-3j,
    (0,0,0,1) : -3-1j,
    (0,0,1,0) : -3+3j,
    (0,0,1,1) : -3+1j,
    (0,1,0,0) : -1-3j,
    (0,1,0,1) : -1-1j,
    (0,1,1,0) : -1+3j,
    (0,1,1,1) : -1+1j,
    (1,0,0,0) :  3-3j,
    (1,0,0,1) :  3-1j,
    (1,0,1,0) :  3+3j,
    (1,0,1,1) :  3+1j,
    (1,1,0,0) :  1-3j,
    (1,1,0,1) :  1-1j,
    (1,1,1,0) :  1+3j,
    (1,1,1,1) :  1+1j
}

comparision_table = {
    (0,0,0,0) : 0,
    (0,0,0,1) : 1,
    (0,0,1,0) : 2,
    (0,0,1,1) : 3,
    (0,1,0,0) : 4,
    (0,1,0,1) : 5,
    (0,1,1,0) : 6,
    (0,1,1,1) : 7,
    (1,0,0,0) : 8,
    (1,0,0,1) : 9,
    (1,0,1,0) : 10,
    (1,0,1,1) : 11,
    (1,1,0,0) : 12,
    (1,1,0,1) : 13,
    (1,1,1,0) : 14,
    (1,1,1,1) : 15
}

M=16
Bits_per_symbol=np.log2(M)
Order=pow(2,Bits_per_symbol)

if M != Order:
   print("the value of M is only acceptable if log2(M)is an integer")

bit_arr = np.array([0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1])


lx= len(bit_arr)
m=int(np.log2(M))
nt= (lx + m - 1)//m
b= -lx + nt*m
input_bit_arr= np.pad(bit_arr,(0,b),'constant')
no_bits = np.size(input_bit_arr)

bit_period = pow(10,-6)
symbol_period = bit_period * Bits_per_symbol
symbol_rate = 1/symbol_period
FreqC = 2 * symbol_rate
t = np.arange(symbol_period/100, symbol_period + symbol_period/100, symbol_period/100)

data_reshape = np.reshape(input_bit_arr, (int(no_bits/np.log2(M)),int(np.log2(M))))

Real_part = [0] * int(no_bits/np.log2(M))
Imaginary_part = [0] * int(no_bits/np.log2(M))

for i in range(0,len(bit_arr),int(no_bits/np.log2(M))):
    x = tuple(bit_arr[i:i+int(np.log2(M))])
    V = mapping_table[x]
    Real_part[int(i/np.log2(M))] = V.real
    Imaginary_part[int(i/np.log2(M))] = V.imag


QAM_signal = np.empty(0)

for i in range(int(no_bits/np.log2(M))):
    out_real = Real_part[i] *  np.sin(2 * np.pi * FreqC * t) # PSK Modulada
    out_img = Imaginary_part[i] * np.cos(2 * np.pi * FreqC * t) # ASK Modulada
    out = out_img + out_real
    QAM_signal = np.append(QAM_signal,out)

tt = np.arange(symbol_period/100, symbol_period*len(Real_part) + symbol_period/100, symbol_period/100)
plt.figure(3)
plt.plot(tt,QAM_signal)


def calc_fft(y):
    n = len(y)  # length of the signal
    k = np.arange(n)
    t2 = symbol_period
    frq = k / t2  # two sides frequency range
    frq = frq[range(n // 2)]  # one side frequency range
    Y = np.fft.fft(y) / n  # fft computing and normalization
    Y = Y[range(n // 2)]
    return Y, frq

Z, frq = calc_fft(QAM_signal)
plt.figure(4)
plt.plot(Z)

plt.show()
