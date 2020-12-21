from pydub import AudioSegment

song = AudioSegment.from_wav("tmp/original.wav")
bpm = 128
oneBeat = 60_000 / bpm * 4

slices = song[::round(oneBeat)]
output = AudioSegment.empty()
for beat in slices:
    length = len(beat) / 4
    beats = list(beat[::round(length)])
    output += beats[0]
    output += beats[3]
    output += beats[2]
    output += beats[1]

output.export("tmp/output.wav", format="wav")
