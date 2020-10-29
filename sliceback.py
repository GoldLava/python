letters = "abcdefghijklmnopqrstuvwxyz"
#[::1] is usually a reversing idiom
backwards = letters[::-1]
print(backwards)

#slice that produces characters qpo
tri = letters[16:13:-1]
print(tri)
#string to produce edcba
aloha = letters[4::-1]
print(aloha)
#slice string to produce last 8 char in reverse order
lastEight = letters[26:17:-1]
print(lastEight)



