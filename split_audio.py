import subprocess

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

# constants 
SOURCE_PATH = '/Users/renegade/MyRepos/automated-audio-splitter/'
DESTINATION_PATH = '/Users/renegade/MyRepos/automated-audio-splitter/BDSP/'


subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", "01:49:42", "-to", "01:52:40", "-i", f'bdsp.flac',  f'{DESTINATION_PATH}/Mt_Coronet.flac'],cwd=f'{SOURCE_PATH}',check=True)
print(bcolors.OKCYAN + "Lake theme" + bcolors.ENDC)

# 
subprocess.run(["ffmpeg", "-i", "BDSP/Mt_Coronet.flac", "-i", "rain.flac", "-filter_complex" ,"amix=inputs=2:duration=first:weights='1 2':dropout_transition=0,volume=2", "Mt_Coronet.flac"],cwd=f'{SOURCE_PATH}',check=True)
print(bcolors.OKCYAN + "Lake theme + RAIN" + bcolors.ENDC)

"""subprocess.run(["ffmpeg","-hide_banner", "-loglevel", "error", "-ss", "02:54:05", "-to", "02:57:38", "-i", "bdsp.flac",  "Old_Chateau.flac"],cwd=f'{SOURCE_PATH}',check=True)
print(bcolors.OKCYAN + "Old Chateau" + bcolors.ENDC)
"""


