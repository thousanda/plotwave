import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import librosa
import librosa.display


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', type=str, help='audio file name you want to visualize')
    return parser.parse_args()


def plot_waveform(filename: str):
    y, sr = librosa.load(filename)
    print(f'sampling rate = {sr}')
    print(f'data: {type(y)}, {len(y)}')
    fig, ax = plt.subplots(nrows=1, sharex=True)
    librosa.display.waveshow(y, sr=sr, ax=ax)
    #ax.set(title='Waveform')
    plt.show()


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

