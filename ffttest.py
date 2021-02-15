import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt

dft = np.array([0, 2, 3, -15, 1.2])
freq = fft.fftfreq(len(dft))
print(freq)
domain_size = 20
step_size = 0.01
#x = fft.fftfreq(domain_size)
x = np.arange(0, domain_size, step_size)
#y = sum(np.abs(i) * np.sin(2 * np.pi * freq[i] * x + np.angle(i)) for i in dft)

y = np.zeros(int(domain_size / step_size))
for i in range(len(dft)):
    ftv = dft[i]
    amplitude = np.abs(ftv)
    frequency = freq[i]
    f = 2*np.pi*frequency
    phase = np.angle(ftv)
    
    new = amplitude * np.cos(f * x + phase)
    
    y += new
    #print(f"{amplitude}cos({2*np.pi*frequency}x + {phase})")

fig, ax = plt.subplots()
l1, = ax.plot(x, y)
#ax.set_ylim(0)
plt.show()