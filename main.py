import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import librosa
import librosa.display


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', type=str, help='audio file name you want to visualize')
    return parser.parse_args()


def plot_waveform(filename: str, show_axis: bool = True):
    y, sr = librosa.load(filename)
    print(f'sampling rate = {sr}')
    print(f'data length = {len(y)}')
    fig, ax = plt.subplots(figsize=(21, 9))
    # ax.set(title='Waveform')

    # 枠やラベル、メモリなどを表示しない場合はoffにする
    if not show_axis:
        ax.axis("off")

    # 描画
    librosa.display.waveshow(y, sr=sr, ax=ax)
    # librosa.display.waveshow(y[1*sr:3*sr], sr=sr, ax=ax)  # 表示範囲調整: 1秒から3秒だけ表示

    # ファイル書き出し & 表示
    plt.savefig('waveform.png')
    plt.show()


def main():
    args = get_args()
    filename: str = args.filename
    print(f'input file: {filename}')
    p = Path(filename)
    print(f'START: visualize waveform')
    plot_waveform(str(p), show_axis=True)
    print('END: done')


if __name__ == '__main__':
    main()

