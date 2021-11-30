import split_audio

SOURCE = split_audio.SOURCE_PATH

with open(f'{SOURCE}/audio_times.txt', 'r') as f:
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

        # line 1
        substr = prev.strip('\n ',)
        track_id = substr.partition('.')[0]
        track_name = substr[substr.find('.')+1:substr.find(':')]
        start_time = substr.partition(':')[2]

        # line 2
        end_time = curr.strip('\n ',).partition(':')[2]

        tracks[track_id] = (track_name, start_time, end_time)

for key,val in tracks.items():
    print(key,val)

