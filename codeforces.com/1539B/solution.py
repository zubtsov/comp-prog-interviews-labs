song_length, number_of_questions = map(int, input().split())
song = list(map(lambda c: ord(c) - ord('a') + 1, input()))
song_lengths = [0, song[0]]
for i in range(1, song_length):
    song_lengths.append(song_lengths[i] + song[i])  # TODO: we could lazily initialize it

for q in range(number_of_questions):
    left, right = map(int, input().split())
    str_length = song_lengths[right] - song_lengths[left - 1]
    print(str_length)
