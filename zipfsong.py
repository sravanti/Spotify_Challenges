from __future__ import division

def calculate_zipf(inputfile):
	with open(inputfile, 'r') as file:
		album_info = file.readline().split()
		num_songs = int(album_info[0])
		num_select = int(album_info[1])
		song_data = file.read().splitlines()
		song_data = [line.split() for line in song_data]
		first_song_plays = int(song_data[0][0])
		for song in range(0, len(song_data)):
			song_data[song][0] = int(song_data[song][0])/(first_song_plays/(song+1))
		song_data.sort(reverse=True)
		print song_data
		for song in range(0, int(num_select)):
			print song_data[song][1]

		
	
