from os import path
from pydub import AudioSegment

# files                                                                         
src = "audioclip-1582727790000-3088.mp4"
dst = "converted.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp4(src)
sound.export(dst, format="wav")
