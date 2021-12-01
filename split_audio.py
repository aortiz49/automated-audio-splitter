import subprocess
from audio_times_parser import *

"""Audio trimmer (pokemon + rain sounds)

1. download youtube-dl (instructions on how to do so)
2. find a long video with timestamps you want the files of
3. find the rain video 
4. split each part of the song into its own audio file
5. mix each one with rain, take the shortest

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

    if not os.path.exists(f'{DESTINATION_PATH}'):
        os.makedirs(f'{DESTINATION_PATH}')

    if not os.path.exists(f'{OUT}'):
        os.makedirs(f'{DESTINATION_PATH}')    

    for key, val in tracks.items():
        name = tracks[f'{key}'][0]
        start = tracks[f'{key}'][1]
        end = tracks[f'{key}'][2]

        subprocess.run(
            ["ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", f'{start}', "-to", f'{end}',
             "-i", f'{ORIGIN_TRACK}', f'{key}.{DESTINATION_PATH}/{name}.flac'], cwd=f'{SOURCE_PATH}',
            check=True)

        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i",
                        f'{DESTINATION_PATH}/{name}.flac',
                        "-i", "rain.flac", "-filter_complex",
                        "amix=inputs=2:duration=first:weights='1 1.9':dropout_transition=0,"
                        "volume=2", f'{name}.flac'], cwd=f'{SOURCE_PATH}', check=True)
        print(bcolors.OKCYAN + f'{name}' + bcolors.ENDC)




    """        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", "01:49:42", "-to", "01:52:40", "-i", "bdsp.flac",  f'{DESTINATION_PATH}/Mt_Coronet.flac'],cwd=f'{SOURCE_PATH}',check=True)
    print(bcolors.OKCYAN + "Lake theme" + bcolors.ENDC)

    run(["ffmpeg","-hide_banner", "-loglevel", "error", "-i", "desriantion_path", "-i", "rain.flac", "-filter_complex" ,"amix=inputs=2:duration=first:weights='1 1.9':dropout_transition=0,volume=2", "Mt_Coronet.flac"],cwd=f'{SOURCE_PATH}',check=True)
    print(bcolors.OKCYAN + "Lake theme + RAIN" + bcolors.ENDC)

    run(["ffmpeg","-hide_banner", "-loglevel", "error", "-ss", "02:54:05", "-to", "02:57:38", "-i", "bdsp.flac",  f'{DESTINATION_PATH}/Old_Chateau.flac'],cwd=f'{SOURCE_PATH}',check=True)
    print(bcolors.OKCYAN + "Old Chateau" + bcolors.ENDC)

    run(["ffmpeg","-hide_banner", "-loglevel", "error", "-i", "BDSP/Old_Chateau.flac", "-i", "rain.flac", "-filter_complex" ,"amix=inputs=2:duration=first:weights='1 1.9':dropout_transition=0,volume=2", "Old_Chateau.flac"],cwd=f'{SOURCE_PATH}',check=True)
    print(bcolors.OKCYAN + "Old_Chateau + RAIN" + bcolors.ENDC)

    run(["ffmpeg","-hide_banner", "-loglevel", "error", "-ss", "02:18:56", "-to", "02:21:51", "-i", "bdsp.flac",  f'{DESTINATION_PATH}/Pokemon_Center_Night.flac'],cwd=f'{SOURCE_PATH}',check=True)
    print(bcolors.OKCYAN + "Pokemon Center (Night)" + bcolors.ENDC)

    run(["ffmpeg", "-i", "BDSP/Pokemon_Center_Night.flac", "-i", "rain.flac", "-filter_complex" ,"amix=inputs=2:duration=first:weights='1 1.9':dropout_transition=0,volume=2", "Pokemon_Center_Night.flac"],cwd=f'{SOURCE_PATH}',check=True)
    print(bcolors.OKCYAN + "Pokemon_Center (Night) + RAIN" + bcolors.ENDC)
"""

