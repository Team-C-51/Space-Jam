import matplotlib.pyplot as plt
import sounddevice as sd
plt.close('all')

# 
Fs = 16000;
d = 10;

# record voice
print('Start Speaking')

a = sd.rec(int(d*Fs), Fs, 1,blocking = True)

sd.wait()
print('Stop Speaking')

print(plt.plot(a))
plt.title('Recorded Sound')

# Playing back recorded sound
sd.play(a, Fs)