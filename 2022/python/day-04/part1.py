def convertSectionToNumbers(section: str):
    sections=list()
    start,end=section.split("-")
    for count in range(int(start),int(end)+1):
        sections.append(count)
    return sections

f = open("puzzle-input.txt","r")
lines = f.readlines()
count=0

for line in lines:
    line = line.replace('\n','')
    assignment1, assignment2 = line.split(",")
    section1 = convertSectionToNumbers(assignment1)
    section2 = convertSectionToNumbers(assignment2)
    result = all([item in section2 for item in section1])
    result2 = all([item in section1 for item in section2])
    # print(result,result2)
    if result == True or result2 == True:
        count+=1

print(count)