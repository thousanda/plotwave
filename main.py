import argparse
from pathlib import Path

import librosa


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', type=str, help='audio file name you want to visualize')
    return parser.parse_args()


def plot_waveform(filename: str):
    x, sr = librosa.load(filename)
    librosa.display.waveplot(x, sr)


def main():
    args = get_args()
    filename: str = args.filename
    print(f'input file: {filename}')
    p = Path(filename)
    print(f'START: visualize waveform')
    plot_waveform(filename)
    print('END: done')


if __name__ == '__main__':
    main()

