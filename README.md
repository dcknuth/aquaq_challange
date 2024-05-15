# aquaq_challange
Coding puzzles from https://challenges.aquaq.co.uk/

## Found these while looking for some additional challenges that look like the Advent of Code challenges. These are a little different and are not from a person using Python by default, but pretty good. I will put a little about each challenge here

* 0 - What's a numpad? - You will generate a message from the input using the old texting/phone input method. I agree with the low difficulty rating listed on this one
* 1 - Rose by any other name - Change a string into an RGB hex color. I didn't know browsers would do that. Neat
* 2 - One is all you need - Remove some bad sections of data. Since the input is short, lots of ways to do this. I probably should have tried to come up with a regex, but just flipped the remaining list a bunch to search in reverse.
* 3 - Short walks - Move square by square until out of instructions. Similar to the easier map walks in Advent of Code
* 4 - This is good co-primen - There are not too many numbers and they are not too large, so a brute force method of doing this one works fine. I stopped there, but could see this with a much larger list with much larger numbers as a later day of Advent of code. Assuming there is a faster prime math way to resolve this
* 5 - Snake eyes - We need to rotate two dice a number of times as given by the input. Again, brute force is fine, and it's not too bad
* 6 - Let me count the ways - Find how many ways you can sum a number. Since we only count the sum of three numbers and the number is not too big we can do this with a two deep nested for, so not too bad.
* 7 - What is best in life? - You are scoring a ping pong tourney using the ELO chess scoring method. The only trouble here was getting the correct order in the (Rb-Ra) part. It was fun to read the Wiki page on chess scoring as I didn't know how they did that. The 400 and 20 constants can also be changed to fit your application and seem to be the middle tier constants used for chess
* 8 - Cron Flakes - Here you run through a daily routine of eating cereal and shopping for groceries. I think this would have a much easier rating except that the instructions have to be read very carefully. I needed to see that milk expires on the fifth day, after you use it and carefully do that part. Also, I needed to note that you are on your first shopping trip of the day when you give your answer, not the second shopping trip of the day (yes, you shop twice a day)
* 9 - Big Data? - Not for Python. Since Python automatically handles very large integers, this is trivial and should be rated 1.6 for Python users
* 10 - Troll Toll - Again, if you use Python and allow yourself the use of NetworkX this is probably a 2.5 level of difficulty. It is a fun one to do and I loved the phrase "how much to get Diddy his fiddy" and after the 2024 accusations, one asks, "What is the fifty for? ;-)"
* 11 - Boxed In - This one was medium hard only as it again requires a careful read and recall of the instructions. Remember you are looking for "total, contiguous tiles needed" not the count of overlapping tiles and not including sections outside the main one with overlaps
* 12 - A Day In The Lift - One needs to read the example very carefully here to get the correct intention. After that, not too bad and in-line with the posted difficulty. Reminds me of the state machine type problems in Advent of Code
