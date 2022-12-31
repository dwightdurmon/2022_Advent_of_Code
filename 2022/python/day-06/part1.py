
# import pprint


# lineList=list()

# f = open("validation-input.txt","r")
# lines = f.readlines()
# characterPosition=0

# for line in lines:
#     line = line.replace('\n','')
#     packetMarker,data = line.split(":")
#     lineLen = len(data)
#     print(packetMarker,lineLen)
#     for i in range(int(lineLen)):
#         tempstring=data[i:i+4]
#         print(i,i+4)
#         charCount=dict()
#         for character in tempstring:
#             # if tempstring has duplicates
#             # then next tempstring 
#             if character in charCount:
#                 charCount[character] += 1
#             else:
#                 charCount[character] = 1
#         print(charCount)
#         flag=False
#         for value in charCount:
#             print(value)
#             if value == 2:
#                 flag=True
#                 break 
#         print(i)

### Not my solution - From https://old.reddit.com/r/adventofcode/comments/zdw0u6/2022_day_6_solutions/j1lkpwn/

with open("puzzle-input.txt") as f:
    raw = list(f.readlines()[0].strip())
i = 0
while i < len(raw):

    if len(set(raw[i:i+4])) == len(raw[i:i+4]): # if there are 4 unique characters, length of set is the same as the length of the list
        print (i + 4)
        break
    i +=1

i = 0
while i < len(raw):
    if len(set(raw[i:i+14])) == len(raw[i:i+14]):
        print (i + 14)

        break
    i +=1