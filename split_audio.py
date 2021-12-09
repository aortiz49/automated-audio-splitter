import subprocess
from audio_times_parser import *

"""Audio trimmer (pokemon + rain sounds)

1. download youtube-dl (instructions on how to do so)
2. find a long video with timestamps you want the files of
3. find the rain video 
4. split each part of the song into its own audio file
5. mix each one with rain, take the shortest do this for all files
6. select the ones you want to add to your mix
7. extract length, fade in and fade out

"""

# internal class to print colors to the terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if __name__ == "__main__":

    # obtains all information from tracks
    tracks = parseTrackList()

    if not os.path.exists(f'{OUT_PATH}/BDSP_NO_RAIN'):
        os.makedirs(f'{OUT_PATH}/BDSP_NO_RAIN')

    if not os.path.exists(f'{OUT_PATH}/BDSP_RAIN'):
        os.makedirs(f'{OUT_PATH}/BDSP_RAIN')  

    for key, val in tracks.items():
        name = tracks[f'{key}'][0]
        start = tracks[f'{key}'][1]
        end = tracks[f'{key}'][2]
        file_name = f'{key}_{name}.flac'

        subprocess.run(
            ["ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", f'{start}', "-to", f'{end}',
             "-i", f'{ORIGIN_TRACK}', f'{OUT_PATH}/BDSP_NO_RAIN/{file_name}'], check=True)

        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i",
                        f'{OUT_PATH}/BDSP_NO_RAIN/{file_name}',
                        "-i", f'{SOURCE_PATH}/rain.flac', "-filter_complex",
                        "amix=inputs=2:duration=first:weights='1 1.9':dropout_transition=0,"
                        "volume=2", f'{file_name}'], cwd=f'{OUT_PATH}/BDSP_RAIN', check=True)

        print(bcolors.OKCYAN + f'{name}' + bcolors.ENDC)


