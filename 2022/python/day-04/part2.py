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
    overlap = set(section1) & set(section2)
    if len(overlap) != 0:
        count+=1
    
print(count)