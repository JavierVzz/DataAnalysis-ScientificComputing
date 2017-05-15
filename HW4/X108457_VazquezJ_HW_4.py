from pylab import linspace, subplot, plot, title, xlabel, ylabel, grid, axis, show
from numpy import arange, log10, sqrt, mean, sum
from scipy.io.wavfile import read
from scipy import fft, ceil
import sounddevice as sd

# Source of sound http://www.dictionary.com/browse/ball?s=t
# Converted to WAV with http://www.online-convert.com/
# (Fs, x) = read("ball.wav")
#
# print(x, Fs)
#
# sd.play(x, samplerate=Fs)

# win = int(Fs/4)
# x_fft = fft(x, win)
# sig_pow = (abs(x_fft)/len(x)) ** 2
# Freqs = arange(0, win, 2) * (Fs/win)
# sig_pow = sig_pow[0:(len(sig_pow))/2]
#
# time = win/Fs
# t = linspace(0, time, win)
# subplot(2,1,1), plot(t, x[0:win])
# title("Sound plot of a .wav file")
# xlabel("Time")
# ylabel("Amplitude")
# axis("tight")
# grid(True)
# show()

Fs = 8000
duration = 3

sd.default.samplerate = Fs
sd.default.channels =2

recorded_audio_2 = sd.rec(duration * Fs, dtype="float64", blocking=True)
sd.play(recorded_audio_2,Fs)