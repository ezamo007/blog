#########################################################################
# Based off Andrew Ippoliti's Blog
# http://blog.acipo.com/wave-generation-in-python/
#########################################################################

import numpy as np
from scipy.io.wavfile import write
global waveform_integers
# Samples per second
sps = 44100
length = 10 #seconds
waveform_integers = np.zeros(length * sps)

#########################################################################
# Adds data to waveform_integers, at time t.
#########################################################################
def add(data, t):
    global waveform_integers
    index = int(t * sps)
    waveform_integers[index: index + len(data)] += data

#########################################################################
# Generate sound data for a sine curve given its frequency, duration,
# and volume.
#########################################################################
def gen_sound_data(freq_hz, duration_s, volume = 0.4):
    each_sample_number = np.arange(duration_s * sps)
    waveform = np.sin(2*np.pi * each_sample_number * freq_hz / sps) * volume
    return waveform

#########################################################################
# Writes the .wav file.
#########################################################################
def make_wav():
    global waveform_integers
    write('output.wav', sps, np.int16(waveform_integers  * 32767))


#########################################################################
# Properties of the sound file.
#########################################################################
min_freq = 200
max_freq = 800

#########################################################################
# K is the number of sections stitched together to produce the audio file.
#########################################################################

n = np.arange(1,100)

#########################################################################
# yt is the function of t we are making the sound for.
# Freqs contains the frequencies corresponding to f(x).
#########################################################################
an = (-1) ** n
bn = n

freqs_2 = (bn - min(bn)) / max(bn)
freqs_2 = min_freq + (max_freq - min_freq) * bn


freqs = (an - min(an)) / (max(an) - min(an))
freqs = min_freq + (max_freq - min_freq) * an

#########################################################################
# Adds the pieces to the main audio file.
#########################################################################
for i, freq in enumerate(freqs):
    beep = gen_sound_data(freq, 0.1)
    add(beep, i * 0.1)
#
# for i, freq in enumerate(freqs_2):
#     beep = gen_sound_data(freq, 0.1)
#     add(beep, i * 0.1)

make_wav()
