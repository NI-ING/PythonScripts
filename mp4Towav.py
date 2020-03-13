#import subprocess
#command = "ffmpeg -i audioclip-1582727790000-3088.mp4 -ab 160k -ac 2 -ar 44100 -vn converted.wav"
#subprocess.call(command, shell=True)

import os
import argparse

from pydub import AudioSegment

formats_to_convert = ['.mp4']

for (dirpath, dirnames, filenames) in os.walk("mp4_files/"):
    for filename in filenames:
        if filename.endswith(tuple(formats_to_convert)):

            filepath = dirpath + '/' + filename
            (path, file_extension) = os.path.splitext(filepath)
            file_extension_final = file_extension.replace('.', '')
            try:
                track = AudioSegment.from_file(filepath,
                        file_extension_final)
                wav_filename = filename.replace(file_extension_final, 'wav')
                wav_path = dirpath + '/' + wav_filename
                print('CONVERTING: ' + str(filepath))
                file_handle = track.export(wav_path, format='wav')
                os.remove(filepath)
            except:
                print("ERROR CONVERTING " + str(filepath))
