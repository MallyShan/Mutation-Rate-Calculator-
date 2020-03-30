# MRIDULA SHAN - COVID19 GLOBAL HACKATHON APPLICATION 
# Calculates the Mutation Rate between two different genomic sequences
def MutationRate(positions, genome1, genome2):
    mutationrate = 0
    if len(genome1) == len(genome2):
        mutationrate = len(positions) / (2 * len(genome1))
    if len(genome1) > len(genome2):
        mutationrate = len(positions) / len(genome2)
    if len(genome1) < len(genome2):
        mutationrate = len(positions) / len(genome1)
    return mutationrate

#Iterates through a genomic sequence and returns the indexes where differences occur
def Comparison(genome1, genome2):
    positions = []
    if (len(genome1) == len(genome2)):
        for i in range(len(genome1)):
            if genome1[i] != genome2[i]:
                positions.append(i)
        return positions

    if (len(genome1) > len(genome2)):
        for i in range(len(genome2)):
            if genome1[i] != genome2[i]:
                positions.append(i)
        if len(positions) == 0:
            positions.append(len(genome1) - 1)
        return positions
    if (len(genome1) < len(genome2)):
        for i in range(len(genome1)):
            if (genome1[i] != genome2[i]):
                positions.append(i)
        if len(positions) == 0:
            positions.append(len(genome2) - 1)
        return positions

# Opens up  all eleven files of the genetic sequences for each virus type and saves to variable
file1 = open('WuhanVirus.txt')
for char in file1:
    genome1 = char

file2 = open('ItalyVirus.txt')
for char in file2:
    genome2 = char

file3 = open('USVirus.txt')
for char in file3:
    genome3 = char

file4 = open('IndiaVirus.txt')
for char in file4:
    genome4 = char

file5 = open('BrazilVirus.txt')
for char in file5:
    genome5 = char

file6 = open('PakistanVirus.txt')
for char in file6:
    genome6 = char

file7 = open('AustraliaVirus.txt')
for char in file7:
    genome7 = char

file8 = open('JapanVirus.txt')
for char in file8:
    genome8 = char

file9 = open('NepalVirus.txt')
for char in file9:
    genome9 = char

file10 = open('SwedenVirus.txt')
for char in file10:
    genome10 = char

file11 = open('TaiwanVirus.txt')
for char in file11:
    genome11 = char

#Below prints out all the combinations for the 11 different viruses
#Calls each function for every combination 
# -------------- 1)WUHAN VIRUS---------------------------
# Italy
print("Wuhan & Italy")
positions = Comparison((genome1), (genome2))
print(positions)
mutationrate = MutationRate(positions, genome1, genome2)
print(mutationrate)
# US
print("Wuhan & US")
positions = Comparison((genome1), (genome3))
print(positions)
mutationrate = MutationRate(positions, genome1, genome3)
print(mutationrate)
# India
print("Wuhan & India")
positions = Comparison((genome1), (genome4))
print(positions)
mutationrate = MutationRate(positions, genome1, genome4)
print(mutationrate)
# Brazil
print("Wuhan & Brazil")
positions = Comparison((genome1), (genome5))
print(positions)
mutationrate = MutationRate(positions, genome1, genome5)
print(mutationrate)
# Pakistan
print("Wuhan & Pakistan")
positions = Comparison((genome1), (genome6))
print(positions)
mutationrate = MutationRate(positions, genome1, genome6)
print(mutationrate)
# Australia
print("Wuhan & Australia")
positions = Comparison((genome1), (genome7))
print(positions)
mutationrate = MutationRate(positions, genome1, genome7)
print(mutationrate)
# Japan
print("Wuhan & Japan")
positions = Comparison((genome1), (genome8))
print(positions)
mutationrate = MutationRate(positions, genome1, genome8)
print(mutationrate)
# Nepal
print("Wuhan & Nepal")
positions = Comparison((genome1), (genome9))
print(positions)
mutationrate = MutationRate(positions, genome1, genome9)
print(mutationrate)
# Sweden
print("Wuhan & Sweden")
positions = Comparison((genome1), (genome10))
print(positions)
mutationrate = MutationRate(positions, genome1, genome10)
print(mutationrate)
# Taiwan
print("Wuhan & Taiwan")
positions = Comparison((genome1), (genome11))
print(positions)
mutationrate = MutationRate(positions, genome1, genome11)
print(mutationrate)
# -------------- 2) ITALY VIRUS---------------------------
# Wuhan
print("Italy & Wuhan")
positions = Comparison((genome2), (genome1))
print(positions)
mutationrate = MutationRate(positions, genome2, genome1)
print(mutationrate)
# US
print("Italy & US")
positions = Comparison((genome2), (genome3))
print(positions)
mutationrate = MutationRate(positions, genome2, genome3)
print(mutationrate)
# India
print("Italy & India")
positions = Comparison((genome2), (genome4))
print(positions)
mutationrate = MutationRate(positions, genome2, genome4)
print(mutationrate)
# Brazil
print("Italy & Brazil")
positions = Comparison((genome2), (genome5))
print(positions)
mutationrate = MutationRate(positions, genome2, genome5)
print(mutationrate)
# Pakistan
print("Italy & Pakistan")
positions = Comparison((genome2), (genome6))
print(positions)
mutationrate = MutationRate(positions, genome2, genome6)
print(mutationrate)
# Australia
print("Italy & Australia")
positions = Comparison((genome2), (genome7))
print(positions)
mutationrate = MutationRate(positions, genome2, genome7)
print(mutationrate)
# Japan
print("Italy & Japan")
positions = Comparison((genome2), (genome8))
print(positions)
mutationrate = MutationRate(positions, genome2, genome8)
print(mutationrate)
# Nepal
print("Italy & Nepal")
positions = Comparison((genome2), (genome9))
print(positions)
mutationrate = MutationRate(positions, genome2, genome9)
print(mutationrate)
# Sweden
print("Italy & Sweden")
positions = Comparison((genome2), (genome10))
print(positions)
mutationrate = MutationRate(positions, genome2, genome10)
print(mutationrate)
# Taiwan
print("Italy & Taiwan")
positions = Comparison((genome2), (genome11))
print(positions)
mutationrate = MutationRate(positions, genome2, genome11)
print(mutationrate)
# -------------- 3)US VIRUS---------------------------
# Wuhan
print("US & Wuhan")
positions = Comparison((genome3), (genome1))
print(positions)
mutationrate = MutationRate(positions, genome3, genome1)
print(mutationrate)
# Italy
print("US & Italy")
positions = Comparison((genome3), (genome2))
print(positions)
mutationrate = MutationRate(positions, genome3, genome2)
print(mutationrate)
# India
print("US & India")
positions = Comparison((genome3), (genome4))
print(positions)
mutationrate = MutationRate(positions, genome3, genome4)
print(mutationrate)
# Brazil
print("US & Brazil")
positions = Comparison((genome3), (genome5))
print(positions)
mutationrate = MutationRate(positions, genome3, genome5)
print(mutationrate)
# Pakistan
print("US & Pakistan")
positions = Comparison((genome3), (genome6))
print(positions)
mutationrate = MutationRate(positions, genome3, genome6)
print(mutationrate)
# Australia
print("US & Australia")
positions = Comparison((genome3), (genome7))
print(positions)
mutationrate = MutationRate(positions, genome3, genome7)
print(mutationrate)
# Japan
print("US & Japan")
positions = Comparison((genome3), (genome8))
print(positions)
mutationrate = MutationRate(positions, genome3, genome8)
print(mutationrate)
# Nepal
print("US & Nepal")
positions = Comparison((genome3), (genome9))
print(positions)
mutationrate = MutationRate(positions, genome3, genome9)
print(mutationrate)
# Sweden
print("US & Sweden")
positions = Comparison((genome3), (genome10))
print(positions)
mutationrate = MutationRate(positions, genome3, genome10)
print(mutationrate)
# Taiwan
print("US & Taiwan")
positions = Comparison((genome3), (genome11))
print(positions)
mutationrate = MutationRate(positions, genome3, genome11)
print(mutationrate)
# --------------4)INDIA VIRUS---------------------------
# Wuhan
print("India & Wuhan")
positions = Comparison((genome4), (genome1))
print(positions)
mutationrate = MutationRate(positions, genome4, genome1)
print(mutationrate)
# Italy
print("India & Italy")
positions = Comparison((genome4), (genome2))
print(positions)
mutationrate = MutationRate(positions, genome4, genome2)
print(mutationrate)
# US
print("India & US")
positions = Comparison((genome4), (genome3))
print(positions)
mutationrate = MutationRate(positions, genome4, genome3)
print(mutationrate)
# Brazil
print("India & Brazil")
positions = Comparison((genome4), (genome5))
print(positions)
mutationrate = MutationRate(positions, genome4, genome5)
print(mutationrate)
# Pakistan
print("India & Pakistan")
positions = Comparison((genome4), (genome6))
print(positions)
mutationrate = MutationRate(positions, genome4, genome6)
print(mutationrate)
# Australia
print("India & Australia")
positions = Comparison((genome4), (genome7))
print(positions)
mutationrate = MutationRate(positions, genome4, genome7)
print(mutationrate)
# Japan
print("India & Japan")
positions = Comparison((genome4), (genome8))
print(positions)
mutationrate = MutationRate(positions, genome4, genome8)
print(mutationrate)
# Nepal
print("India & Nepal")
positions = Comparison((genome4), (genome9))
print(positions)
mutationrate = MutationRate(positions, genome4, genome9)
print(mutationrate)
# Sweden
print("India & Sweden")
positions = Comparison((genome4), (genome10))
print(positions)
mutationrate = MutationRate(positions, genome4, genome10)
print(mutationrate)
# Taiwan
print("India & Taiwan")
positions = Comparison((genome4), (genome11))
print(positions)
mutationrate = MutationRate(positions, genome4, genome11)
print(mutationrate)
# --------------5)BRAZIL VIRUS---------------------------
# Wuhan
print("Brazil & Wuhan")
positions = Comparison((genome5), (genome1))
print(positions)
mutationrate = MutationRate(positions, genome5, genome1)
print(mutationrate)
# Italy
print("Brazil & Italy")
positions = Comparison((genome5), (genome2))
print(positions)
mutationrate = MutationRate(positions, genome5, genome2)
print(mutationrate)
# US
print("Brazil & US")
positions = Comparison((genome5), (genome3))
print(positions)
mutationrate = MutationRate(positions, genome5, genome3)
print(mutationrate)
# India
print("Brazil & India")
positions = Comparison((genome5), (genome4))
print(positions)
mutationrate = MutationRate(positions, genome5, genome4)
print(mutationrate)
# Pakistan
print("Brazil & Pakistan")
positions = Comparison((genome5), (genome6))
print(positions)
mutationrate = MutationRate(positions, genome5, genome6)
print(mutationrate)
# Australia
print("Brazil & Australia")
positions = Comparison((genome5), (genome7))
print(positions)
mutationrate = MutationRate(positions, genome5, genome7)
print(mutationrate)
# Japan
print("Brazil & Japan")
positions = Comparison((genome5), (genome8))
print(positions)
mutationrate = MutationRate(positions, genome5, genome8)
print(mutationrate)
# Nepal
print("Brazil & Nepal")
positions = Comparison((genome5), (genome9))
print(positions)
mutationrate = MutationRate(positions, genome5, genome9)
print(mutationrate)
# Sweden
print("Brazil & Sweden")
positions = Comparison((genome5), (genome10))
print(positions)
mutationrate = MutationRate(positions, genome5, genome10)
print(mutationrate)
# Taiwan
print("Brazil & Taiwan")
positions = Comparison((genome5), (genome11))
print(positions)
mutationrate = MutationRate(positions, genome5, genome11)
print(mutationrate)

# --------------6)PAKISTAN VIRUS---------------------------
# Wuhan
print("Pakistan & Wuhan")
positions = Comparison((genome6), (genome1))
print(positions)
mutationrate = MutationRate(positions, genome6, genome1)
print(mutationrate)
# Italy
print("Pakistan & Italy")
positions = Comparison((genome6), (genome2))
print(positions)
mutationrate = MutationRate(positions, genome6, genome2)
print(mutationrate)
# US
print("Pakistan & US")
positions = Comparison((genome6), (genome3))
print(positions)
mutationrate = MutationRate(positions, genome6, genome3)
print(mutationrate)
# India
print("Pakistan & India")
positions = Comparison((genome6), (genome4))
print(positions)
mutationrate = MutationRate(positions, genome6, genome4)
print(mutationrate)
# Brazil
print("Pakistan & India")
positions = Comparison((genome6), (genome5))
print(positions)
mutationrate = MutationRate(positions, genome6, genome5)
print(mutationrate)
# Australia
print("Pakistan & Australia")
positions = Comparison((genome6), (genome7))
print(positions)
mutationrate = MutationRate(positions, genome6, genome7)
print(mutationrate)
# Japan
print("Pakistan & Japan")
positions = Comparison((genome6), (genome8))
print(positions)
mutationrate = MutationRate(positions, genome6, genome8)
print(mutationrate)
# Nepal
print("Pakistan & Nepal")
positions = Comparison((genome6), (genome9))
print(positions)
mutationrate = MutationRate(positions, genome6, genome9)
print(mutationrate)
# Sweden
print("Pakistan & Sweden")
positions = Comparison((genome6), (genome10))
print(positions)
mutationrate = MutationRate(positions, genome6, genome10)
print(mutationrate)
# Taiwan
print("Pakistan & Taiwan")
positions = Comparison((genome6), (genome11))
print(positions)
mutationrate = MutationRate(positions, genome6, genome11)
print(mutationrate)

# --------------7)AUSTRALIA VIRUS---------------------------
# Wuhan
print("Australia & Wuhan")
positions = Comparison((genome7), (genome1))
print(positions)
mutationrate = MutationRate(positions, genome7, genome1)
print(mutationrate)
# Italy
print("Australia & Italy")
positions = Comparison((genome7), (genome2))
print(positions)
mutationrate = MutationRate(positions, genome7, genome2)
print(mutationrate)
# US
print("Australia & US")
positions = Comparison((genome7), (genome3))
print(positions)
mutationrate = MutationRate(positions, genome7, genome3)
print(mutationrate)
# India
print("Australia & India")
positions = Comparison((genome7), (genome4))
print(positions)
mutationrate = MutationRate(positions, genome7, genome4)
print(mutationrate)
# Brazil
print("Australia & Brazil")
positions = Comparison((genome7), (genome5))
print(positions)
mutationrate = MutationRate(positions, genome7, genome5)
print(mutationrate)
# Pakistan
print("Australia & Pakistan")
positions = Comparison((genome7), (genome6))
print(positions)
mutationrate = MutationRate(positions, genome7, genome6)
print(mutationrate)
# Japan
print("Australia & Japan")
positions = Comparison((genome7), (genome8))
print(positions)
mutationrate = MutationRate(positions, genome7, genome8)
print(mutationrate)
# Nepal
print("Australia & Nepal")
positions = Comparison((genome7), (genome9))
print(positions)
mutationrate = MutationRate(positions, genome7, genome9)
print(mutationrate)
# Sweden
print("Australia & Sweden")
positions = Comparison((genome7), (genome10))
print(positions)
mutationrate = MutationRate(positions, genome7, genome10)
print(mutationrate)
# Taiwan
print("Australia & Taiwan")
positions = Comparison((genome7), (genome11))
print(positions)
mutationrate = MutationRate(positions, genome7, genome11)
print(mutationrate)

# --------------8)JAPAN VIRUS---------------------------
# Wuhan
print("Japan & Wuhan")
positions = Comparison((genome8), (genome1))
print(positions)
mutationrate = MutationRate(positions, genome8, genome1)
print(mutationrate)
# Italy
print("Japan & Italy")
positions = Comparison((genome8), (genome2))
print(positions)
mutationrate = MutationRate(positions, genome8, genome2)
print(mutationrate)
# US
print("Japan & US")
positions = Comparison((genome8), (genome3))
print(positions)
mutationrate = MutationRate(positions, genome8, genome3)
print(mutationrate)
# India
print("Japan & India")
positions = Comparison((genome8), (genome4))
print(positions)
mutationrate = MutationRate(positions, genome8, genome4)
print(mutationrate)
# Brazil
print("Japan & Brazil")
positions = Comparison((genome8), (genome5))
print(positions)
mutationrate = MutationRate(positions, genome8, genome5)
print(mutationrate)
# Pakistan
print("Japan & Pakistan")
positions = Comparison((genome8), (genome6))
print(positions)
mutationrate = MutationRate(positions, genome8, genome6)
print(mutationrate)
# Australia
print("Japan & Australia")
positions = Comparison((genome8), (genome7))
print(positions)
mutationrate = MutationRate(positions, genome8, genome7)
print(mutationrate)
# Nepal
print("Japan & Nepal")
positions = Comparison((genome8), (genome9))
print(positions)
mutationrate = MutationRate(positions, genome8, genome9)
print(mutationrate)
# Sweden
print("Japan & Sweden")
positions = Comparison((genome8), (genome10))
print(positions)
mutationrate = MutationRate(positions, genome8, genome10)
print(mutationrate)
# Taiwan
print("Japan & Taiwan")
positions = Comparison((genome8), (genome11))
print(positions)
mutationrate = MutationRate(positions, genome8, genome11)
print(mutationrate)

# --------------9)NEPAL VIRUS---------------------------
# Wuhan
print("Nepal & Wuhan")
positions = Comparison((genome9), (genome1))
print(positions)
mutationrate = MutationRate(positions, genome9, genome1)
print(mutationrate)
# Italy
print("Nepal & Italy")
positions = Comparison((genome9), (genome2))
print(positions)
mutationrate = MutationRate(positions, genome9, genome2)
print(mutationrate)
# US
print("Nepal & US")
positions = Comparison((genome9), (genome3))
print(positions)
mutationrate = MutationRate(positions, genome9, genome3)
print(mutationrate)
# India
print("Nepal & India")
positions = Comparison((genome9), (genome4))
print(positions)
mutationrate = MutationRate(positions, genome9, genome4)
print(mutationrate)
# Brazil
print("Nepal & Brazil")
positions = Comparison((genome9), (genome5))
print(positions)
mutationrate = MutationRate(positions, genome9, genome5)
print(mutationrate)
# Pakistan
print("Nepal & Pakistan")
positions = Comparison((genome9), (genome6))
print(positions)
mutationrate = MutationRate(positions, genome9, genome6)
print(mutationrate)
# Australia
print("Nepal & Australia")
positions = Comparison((genome9), (genome7))
print(positions)
mutationrate = MutationRate(positions, genome9, genome7)
print(mutationrate)
# Japan
print("Nepal & Japan")
positions = Comparison((genome9), (genome8))
print(positions)
mutationrate = MutationRate(positions, genome9, genome8)
print(mutationrate)
# Sweden
print("Nepal & Sweden")
positions = Comparison((genome9), (genome10))
print(positions)
mutationrate = MutationRate(positions, genome9, genome10)
print(mutationrate)
# Taiwan
print("Nepal & Taiwan")
positions = Comparison((genome9), (genome11))
print(positions)
mutationrate = MutationRate(positions, genome9, genome11)
print(mutationrate)

# --------------10)SWEDEN VIRUS---------------------------
# Wuhan
print("Sweden & Wuhan")
positions = Comparison((genome10), (genome1))
print(positions)
mutationrate = MutationRate(positions, genome10, genome1)
print(mutationrate)
# Italy
print("Sweden & Italy")
positions = Comparison((genome10), (genome2))
print(positions)
mutationrate = MutationRate(positions, genome10, genome2)
print(mutationrate)
# US
print("Sweden & US")
positions = Comparison((genome10), (genome3))
print(positions)
mutationrate = MutationRate(positions, genome10, genome3)
print(mutationrate)
# India
print("Sweden & India")
positions = Comparison((genome10), (genome4))
print(positions)
mutationrate = MutationRate(positions, genome10, genome4)
print(mutationrate)
# Brazil
print("Sweden & Brazil")
positions = Comparison((genome10), (genome5))
print(positions)
mutationrate = MutationRate(positions, genome10, genome5)
print(mutationrate)
# Pakistan
print("Sweden & Pakistan")
positions = Comparison((genome10), (genome6))
print(positions)
mutationrate = MutationRate(positions, genome10, genome6)
print(mutationrate)
# Australia
print("Sweden & Australia")
positions = Comparison((genome10), (genome7))
print(positions)
mutationrate = MutationRate(positions, genome10, genome7)
print(mutationrate)
# Japan
print("Sweden & Japan")
positions = Comparison((genome10), (genome8))
print(positions)
mutationrate = MutationRate(positions, genome10, genome8)
print(mutationrate)
# Nepal
print("Sweden & Nepal")
positions = Comparison((genome10), (genome9))
print(positions)
mutationrate = MutationRate(positions, genome10, genome9)
print(mutationrate)
# Taiwan
print("Sweden & Taiwan")
positions = Comparison((genome10), (genome11))
print(positions)
mutationrate = MutationRate(positions, genome10, genome11)
print(mutationrate)

# --------------11)TAIWAN VIRUS---------------------------
# Wuhan
print("Taiwan & Wuhan")
positions = Comparison((genome11), (genome1))
print(positions)
mutationrate = MutationRate(positions, genome11, genome1)
print(mutationrate)
# Italy
print("Taiwan & Italy")
positions = Comparison((genome11), (genome2))
print(positions)
mutationrate = MutationRate(positions, genome11, genome2)
print(mutationrate)
# US
print("Taiwan & US")
positions = Comparison((genome11),(genome3))
print(positions)
mutationrate = MutationRate(positions,genome11,genome3)
print(mutationrate)
# India
print("Taiwan & India")
positions = Comparison((genome11),(genome4))
print(positions)
mutationrate = MutationRate(positions,genome11,genome4)
print(mutationrate)
# Brazil
print("Taiwan & Brazil")
positions = Comparison((genome11),(genome5))
print(positions)
mutationrate = MutationRate(positions,genome11,genome5)
print(mutationrate)
# Pakistan
print("Taiwan & Pakistan")
positions = Comparison((genome11),(genome6))
print(positions)
mutationrate = MutationRate(positions,genome11,genome6)
print(mutationrate)
# Australia
print("Taiwan & Australia")
positions = Comparison((genome11),(genome7))
print(positions)
mutationrate = MutationRate(positions,genome11,genome7)
print(mutationrate)
# Japan
print("Taiwan & Japan")
positions = Comparison((genome11),(genome8))
print(positions)
mutationrate = MutationRate(positions,genome11,genome8)
print(mutationrate)
# Nepal
print("Taiwan & Nepal")
positions = Comparison((genome11),(genome9))
print(positions)
mutationrate = MutationRate(positions,genome11,genome9)
print(mutationrate)
# Sweden
print("Taiwan & Sweden")
positions = Comparison((genome11),(genome10))
print(positions)
mutationrate = MutationRate(positions,genome11,genome10)
print(mutationrate)