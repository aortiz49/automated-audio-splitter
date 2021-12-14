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
    no_rain_dir = f'{OUT_PATH}/BDSP_NO_RAIN'
    with_rain_dir = f'{OUT_PATH}/BDSP_RAIN'
    fade_dir = f'{OUT_PATH}/FADE'

    if not os.path.exists(f'{no_rain_dir}'):
        os.makedirs(f'{no_rain_dir}')

    if not os.path.exists(f'{fade_dir}'):
        os.makedirs(f'{fade_dir}')

    os.makedirs(os.path.dirname(f'{SOURCE_PATH}/strong_rain.flac'), exist_ok=True)

    # double the sound of the rain
    subprocess.run(["ffmpeg", "-i", f'{SOURCE_PATH}/rain.flac', "-filter:a", "volume=2.0",
                    f'{SOURCE_PATH}/strong_rain.flac'])

    for key, val in tracks.items():
        name = tracks[f'{key}'][0]
        start = tracks[f'{key}'][1]
        end = tracks[f'{key}'][2]
        file_name = f'{key}_{name}.flac'
        no_rain_file = f'{no_rain_dir}/{file_name}'
        rain_file = f'{with_rain_dir}/{file_name}'
        fade_file = f'{fade_dir}/{file_name}'

        # split large track found in ORIGIN_TRACK into individual subtracks at no_rain_file
        # reduce the sound of the music
        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", f'{start}',
                        "-to", f'{end}', "-i", f'{ORIGIN_TRACK}', "-filter:a", "volume=0.65",
                        f'{no_rain_file}'], check=True)

        # obtain the duration of the track no_rain_file
        duration = float(subprocess.run(["ffprobe", "-i", f'{no_rain_file}', "-show_entries",
                                         "format=duration", "-v", "quiet", "-of", "csv=p=0"],
                                        capture_output=True, encoding='UTF-8').stdout)

        # ensure duration is long enough
        if duration >= 10:
            # apply fade-in and fade-out effect to track no_rain_file, store in faded_file
            subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", f'{no_rain_file}',
                            "-af", f'afade=t=in:st=0:d=4,afade=t=out:st={float(duration) - 4}:d=4',
                            f'{fade_file}'])


        print(bcolors.OKCYAN + f'{name}' + bcolors.ENDC)
