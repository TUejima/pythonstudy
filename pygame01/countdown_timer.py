import argparse
import time
import sys
import os
from mutagen.mp3 import MP3
import pygame

class CountDownTimer:
    def __init__(self, minutes, mp3_filepath):
        self.minutes = minutes
        self.seconds = 0
        self.mp3_file_path = mp3_filepath

    def validate_arg_minutes(self):
        """引数の時間をチェック"""
        if self.minutes < 0:
            print('時間には０以上の整数を入力してください')
            return False
        return True

    def validate_arg_mp3_filepath(self):
        """引数のｍｐ３ファイルをチェック"""
        if self.mp3_file_path == '':
            print('mp3ファイルのパスを入力して下さい')
            return False
        if not os.path.exists(self.mp3_file_path):
            print('ファイルが見つかりませんでした')
            return False
        _, ext = os.path.splitext(self.mp3_file_path)
        if ext != '.mp3':
            print('拡張子が{}です。mp3ファイルを指定してください。'.format(ext))
            return False
        return True

    def count_down(self):
        if not self.validate_arg_minutes():
            return
        if not self.validate_arg_mp3_filepath():
            return

        while self.minutes >= 0 and self.seconds >= 0:
            print('r残り時間: {}:{:0>2}'.format(self.minutes, self.seconds), end='')
            self.seconds -= 1
            if self.seconds < 0:
                self.minutes -= 1
                self.seconds - 59
            if self.minutes < 0:
                break
            time.sleep(1)

        pygame.mixer.init()
        pygame.mixer.music.load(self.mp3_file_path)
        mp3_length = MP3(self.mp3_file_path).info.length

        print('\n時間になりました')
        print('終了するにはCtrl+Cを押してください')

        try:
            while True:
                pygame.mixer.music.play(1)
                time.sleep(mp3_length + 0.1)
        except KeyboardInterrupt:
            pygame.mixer_music.stop()
            sys.exit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='引数で指定した時間(分単位)後にmp3ファイルを鳴らす')
    parser.add_argument('minutes', type=int, help='指定時間(分単位)')
    parser.add_argument('mp3_file_path', type=str, help='mp3ファイルのパス')

    args = parser.parse_args()
    countdown_timer = CountDownTimer(args.minutes, args.mp3_file_path)
    countdown_timer.count_down()