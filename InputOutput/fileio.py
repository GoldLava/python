# read only
# grab_me = open("C:/Users/fulle/Desktop/MyNotes.txt", 'r')
#
# for line in grab_me:
#     if "added" in line.lower():
#         print(line, end='')
#
# grab_me.close()
# ANOTHER VERSION
# with open("C:/Users/fulle/Desktop/MyNotes.txt", 'r') as jabber:
#     for line in jabber:
#         if "added" in line.upper():
#             print(line, end='')
# USING WHILE INSTEAD OF A FOR LOOP TO READ
# with open("C:/Users/fulle/Desktop/MyNotes.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()
# CONVERTED AS A LIST
# with open("C:/Users/fulle/Desktop/MyNotes.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')

