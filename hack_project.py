"""
Authors: Timothy Fievet, Joseph Lee

computes prestige of songs and outputs a score
"""
import textstat
import random
import csv

#open csv with format artist/song name/link/lyrics
with open('data.csv', 'r') as file:
    songs = list(csv.reader(file))
    row_count = sum(1 for row in songs)

picked = False
counter = 0
random_choice = False

#either input random song or search
list = []
user_input = input("Pick a song or type 'random' for random song: ").strip()
if (user_input == 'random'):
    random_num = random.randint(1, row_count)
    list.append(songs[random_num])
else:
    for i in range (2, row_count):
        if (user_input.lower() == songs[i][1].lower()):
            list.append(songs[i])

#if song DNE, exit, if multiple songs exist then pick one
if len(list) == 0:
    print('This song does not exist')
    exit()
elif(len(list) == 1):
    picked_song = list[0]
else:
    D = {}
    ans = 0

    while ans not in D.keys():
        c = 1
        prompt = "\nMultible possible artists, which artist did you want?\n\n"
        for l in list:
            prompt += str(c) + "." + l[0] + "\n"
            D[str(c)] = l
            c+=1
        ans = input(prompt + ">> ")
    picked_song = D[ans]
picked_song[3] = picked_song[3].split()
file.close()



"""
Decription: Determines the complexity of a song's lyrics by adding up the number of letters of unique words contained within the song
extra points for having hairy dawg's favorite words

@parameter song: list of form ['artist','song title','lyrics']
@return: gauaged value of a song
"""
def song_value(song):
    value = 0
    S = set()
    for i in range(len(song[3])):      
        S.add(song[3][i].lower())
    for x in S:
        D = {}
        for i in x:
            if i in D.keys():
                D[i]+= 1
                if D[i] > 4:
                    value -= 1
            else:
                D[i] = 1
        value += len(x)
        if x in ["dawg"]:
            value += 3
        elif x in ["dog"]:    
            value += 1
        elif x in ["wreck","ramble","bee","buzz","georgia"]:
            value += 2
    return round((value/len(S))*10, 2)

#print summary data about song score
print('Song Score: ' + picked_song[1] + ' by ' + picked_song[0] + ', ' + str(song_value(picked_song)))