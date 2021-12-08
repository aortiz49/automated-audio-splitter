import subprocess
import os

# constants 
SOURCE_PATH = '/Users/renegade/MyRepos/automated-audio-splitter/in'
OUT_PATH = '/Users/renegade/MyRepos/automated-audio-splitter/out'
ORIGIN_TRACK = f'{SOURCE_PATH}/bdsp.flac'  # TODO: set this as path var


def parseTrackList():
    with open(f'{SOURCE_PATH}/audio_times.txt', 'r') as f:
        tracks = {}

        # create dictionary of tracks
        prev = ""
        curr = f.readline()

        # by reading the 1st line outside the loop, we can get all n and n+1 lines 
        # (except for the final one since we don't know the end time. This will be handled later.
        for line in f:
            # assign prev to the current line
            prev = curr

            # assign curr to the next line 
            curr = line

            # obtain information about the track
            substr = prev.strip('\n ', )
            track_id = substr.partition('.')[0]
            track_name = (substr[substr.find('.') + 1:substr.find(':')]).replace(" ", "_")
            start_time = substr.partition(':')[2]

            # obtain end time of the previous track by extracting the start time of the current
            # track
            end_time = curr.strip('\n ', ).partition(':')[2]

            tracks[track_id] = (track_name, start_time, end_time)

    # manage edge case for the last line in the file
    substr = curr.strip('\n ', )
    track_id = substr.partition('.')[0]
    track_name = substr[substr.find('.') + 1:substr.find(':')]
    start_time = substr.partition(':')[2]

    # get file length
    tot_duration = subprocess.run(["ffprobe", "-i", 'bdsp.flac', "-show_entries",
                                   "format=duration", "-v", "quiet", "-of", "csv=p=0",
                                   "-sexagesimal"], cwd=f'{SOURCE_PATH}', capture_output=True,
                                  encoding='UTF-8').stdout[:7]

    # add final track to dictionary
    tracks[track_id] = (track_name, start_time, tot_duration)

    # check that the file exists.If not, create the directory.
    file = f'{OUT_PATH}/out.txt'
    os.makedirs(os.path.dirname(file), exist_ok=True)

    # if the file exists, overwrite it
    with open(file, 'w') as filetowrite:
        filetowrite.write(' ------------------------------------\n')
        filetowrite.write(f'| Track | Name | startTime - endTime |\n')
        filetowrite.write(' ------------------------------------\n')

        for key, val in tracks.items():
            filetowrite.write(f'|{key}|{val[0]}|{val[1]}-{val[2]}|\n')

    return tracks
