Spotify_Challenges
==================
#Puzzle 1:

Yi has moved to Sweden and now goes to school here. The first years of schooling she got in China, and the curricula do not match completely in the two countries. Yi likes mathematics, but now… The teacher explains the algorithm for subtraction on the board, and Yi is bored. Maybe it is possible to perform the same calculations on the numbers corresponding to the reversed binary representations of the numbers on the board? Yi dreams away and starts constructing a program that reverses the binary representation, in her mind. As soon as the lecture ends, she will go home and write it on her computer.

##Task

Your task will be to write a program for reversing numbers in binary. For instance, the binary representation of 13 is 1101, and reversing it gives 1011, which corresponds to number 11.

##Input

The input contains a single line with an integer N, 1 ≤ N ≤ 1000000000.

##Output

Output one line with one integer, the number we get by reversing the binary representation of N.

#Puzzle 2:
Your slightly pointy-bearded boss has assigned you to write software to find the best songs from different music albums. And the software should be finished in an hour. But don’t panic, you don’t have to solve the problem of writing an AI with good taste. At your disposal is the impeccable taste of a vast horde of long-tailed monkeys. Well, at least almost. The monkeys are not very communicative (or rather, you’re not sure which song “Ook!” is supposed to refer to) so you can’t ask them which songs are the best. What you can do however is to look at which songs the monkeys have listened to and use this information to deduce which songs are the best.

At first, you figure that the most listened to songs must be the best songs. However, you quickly realize that this approach is flawed. Even if all songs of the album are equally good, the early songs are more likely to be listened to more often than the later ones, because monkeys will tend to start listening to the first song, listen for a few songs and then, when their fickle ears start craving something else, stop listening. Instead, if all songs are equal, you expect that their play frequencies should follow Zipf’s Law.

Zipf’s Law is an empirical law originally formulated about word frequencies in natural languages, but it has been observed that many natural phenomena, such as population sizes and incomes, approximately follow the same law. It predicts that the relative frequency of thei’th most common object (in this case, a song) should be proportional to 1/i.

To illustrate this in our setting, suppose we have an album where all songs are equally good. Then by Zipf’s Law, you expect that the first song is listened to twice as often as the second song, and more generally that the first song is listened to i times as often as the i’th song. When some songs are better than others, those will be listened to more often than predicted by Zipf’s Law, and those are the songs your program should select as the good songs. Specifically, suppose that song i has been played fi times but that Zipf’s Law predicts that it would have been played zi times. Then you define the quality of song i to be qi = fi / zi. Your software should select the songs with the highest values of qi.
