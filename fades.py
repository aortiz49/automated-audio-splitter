import os
import subprocess
from audio_times_parser import *


if __name__ == "__main__":

    if not os.path.exists(f'{OUT_PATH}/FINAL_FILTERED'):
        os.makedirs(f'{OUT_PATH}/FINAL_FILTERED')

    # assume final exists
    files = sorted([f for f in os.listdir(f'{OUT_PATH}/FINAL') if not f.startswith('.')], key=str.lower)

       # get duration of a track
    for f in files:
        duration = subprocess.run(["ffprobe", "-i", f'{f}', "-show_entries",
                                       "format=duration", "-v", "quiet", "-of", "csv=p=0"], 
                                        cwd=f'{OUT_PATH}/FINAL', capture_output=True,
                                        encoding='UTF-8').stdout

          
        subprocess.run(["ffmpeg","-hide_banner", "-loglevel", "error", "-i", f'{f}', "-af",
                        f'afade=t=in:st=0:d=3,afade=t=out:st={float(duration)-3}:d=3', 
                        f'{OUT_PATH}/FINAL_FILTERED/{f}'],cwd=f'{OUT_PATH}/FINAL')

        print('Fading '+ f'{f}.')


    