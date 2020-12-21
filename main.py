import getopt
import sys

from pydub import AudioSegment


def main(argv):
    input_file = ''
    output_file = ''
    bpm = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:b:", ["ifile=", "ofile=", "bpm="])
    except getopt.GetoptError:
        print('test.py -i <inputFile>.wav -o <outputFile>.wav -b <bpm>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputFile>.wav -o <outputFile>.wav -b <bpm>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
        elif opt in ("-b", "--bpm"):
            bpm = arg
    if input_file == "" or bpm == "":
        exit(1)
    else:
        if output_file == "":
            convert(input_file, bpm)
        else:
            convert(input_file, bpm, output_file)


def convert(infile, bpm, outfile="tmp/output.wav"):
    song = AudioSegment.from_wav(infile)

    one_beat = 60_000 / int(bpm) * 4
    slices = song[::round(one_beat)]
    output = AudioSegment.empty()

    for beat in slices:
        length = len(beat) / 4
        beats = list(beat[::round(length)])
        output += beats[0]
        output += beats[3]
        output += beats[2]
        output += beats[1]
    output.export(outfile, format="wav")


if __name__ == "__main__":
    main(sys.argv[1:])
