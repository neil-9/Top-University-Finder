# Shourya Nundy (251282929) 1026A Assignment 3

# Function to store important data taken from the university rankings file as lists
def getUni(rankingFileName):
    uni_list = []
    try:  # Using try-except for exception handling
        infile_uni = open(rankingFileName, "r", encoding="utf8")  # Opening rankings file to read data
        try:
            infile_uni.readline()  # Skipping first line containing all the headings
            for line in infile_uni:
                line = line.strip("\n").split(",")  # Removing newline character and splitting line to extract data from each column
                uni_list.append([line[0].upper(), line[1].upper(), line[2].upper(), line[3].upper(), line[8].upper()])  # Adding columns of data into list
            return uni_list
        finally:
            infile_uni.close()
    except FileNotFoundError as exception:
        print("Error:", str(exception))  # Printing exception error if file is not found
        quit()

# Function to store important data taken from the capitals file as lists
def getCapital(capitalsFileName):
    cap_list = []
    try:  # Using try-except for exception handling
        infile_cap = open(capitalsFileName, "r", encoding="utf8")  # Opening capitals file to read data
        try:
            infile_cap.readline()  # Skipping first line containing all the headings
            for line in infile_cap:
                line = line.strip("\n").split(",")  # Removing newline character and splitting line to extract data from each column
                cap_list.append([line[0].upper(), line[1].upper(), line[5].upper()])  # Adding columns of data into list
            return cap_list
        finally:
            infile_cap.close()
    except FileNotFoundError as exception:
        print("Error:", str(exception))  # Printing exception error if file is not found
        quit()

# Function to calculate and return the total number of universities in the rankings file
def TotalUni(univs):
    total = len(univs)
    return total

# Function to find the total number of countries in the rankings file and add them to a list
def countries(univs):
    cntryList = []
    for cntry in range(len(univs)):
        if univs[cntry][2] not in cntryList:  # Checking if country is already in the list or not
            cntryList.append(univs[cntry][2])  # Adding country names to list
    return cntryList

# Function to find the continents in the rankings file and add them to a list
def continents(univs, cap):
    cntryList = countries(univs)
    contiList = []
    for conti in range(len(cap)):
        if cap[conti][0] in cntryList and cap[conti][2] not in contiList:  # Adding to list if not already there
            contiList.append(cap[conti][2])
    return contiList

# Function to find the university with top international rank from the given country
def intRank(univs, selCountry):
    topRank = (999, "")
    for univ in univs:
        if univ[2] == selCountry:
            if int(univ[0]) < topRank[0]:  # Comparing ranks
                topRank = (int(univ[0]), univ[1])
    return topRank

# Function to find the university with top national rank from the given country
def natRank(univs, selCountry):
    topRank = (999, "")
    for univ in univs:
        if univ[2] == selCountry:
            if int(univ[3]) < topRank[0]:  # Comparing ranks
                topRank = (int(univ[3]), univ[1])
    return topRank

# Function to find the average score of all universities in the given country
def avgScore(univs, selCountry):
    sum = 0.0
    count = 0
    for univ in univs:
        if univ[2] == selCountry:
            sum += float(univ[4])
            count += 1
    avg = sum / count  # Calculating average
    return avg

# Function to find the continent relative score of the given country
def relScore(univs, cap, selCountry):
    avg = avgScore(univs, selCountry)
    for cntry in cap:
        if cntry[0] == selCountry:
            conti = cntry[2]
    highest = -1
    for continent in univs:
        for find in cap:
            if continent[2] in find[0]:
                if conti in find:
                    if float(continent[4]) > highest:
                        highest = float(continent[4])
    rel = (avg / highest) * 100  # Calculating continent relative score
    return rel, avg, highest, conti  # Returning relative score, average score, highest score and name of continent

# Function to return the capital of the given country
def capital(capital, selCountry):
    cap = ""
    for cntry in capital:
        if cntry[0] == selCountry:
            cap = cntry[1]
            break  # Breaking off loop when capital is found
    return cap

# Function to find the number of universities having the capital in their name
def capInName(univs, capList, selCountry):
    count = 1
    nameList = ""
    for univ in univs:
        cap = capital(capList, selCountry)
        if cap in univ[1]:
            nameList = nameList + "#%i %s\n" % (count, univ[1])
            count += 1
    return nameList

def getInformation(selectedCountry, rankingFileName, capitalsFileName):
    # Calling function to extract necessary data from rankings file and storing it into a list
    uni_list = getUni(rankingFileName)
    # Calling function to extract necessary data from capitals file and storing it into a list
    cap_list = getCapital(capitalsFileName)
    outfile = open("output.txt", "w")  # Opening the file to be used for writing data

    # Writing the total number of universities present
    outfile.write("Total number of universities => %d\n" % TotalUni(uni_list))

    cntryStr = ""
    # Calling function and storing country names in a list
    cntryList = countries(uni_list)
    # Using for loop to add all the country names to a single string
    for cntry in range(len(cntryList)):
        if cntryList[cntry] != cntryList[-1]:
            cntryStr = cntryStr + cntryList[cntry] + ", "
        else:
            cntryStr = cntryStr + cntryList[cntry]  # if-else statement to avoid extra comma after the last element
    # Writing the names of countries available
    outfile.write("Available countries => %s\n" % cntryStr)

    # Calling function and storing continent names in a list
    contiList = continents(uni_list, cap_list)
    contiString = ""
    # Using for loop to add all the continent names to a single string
    for conti in contiList:
        if conti != contiList[-1]:
            contiString = contiString + conti + ", "
        else:
            contiString = contiString + conti  # if-else statement to avoid extra comma after the last element
    # Writing the names of the available continents
    outfile.write("Available continents => %s\n" % contiString)

    # Calling function to store top international rank and university name of the given country as a tuple
    topRankInt = intRank(uni_list, selectedCountry.upper())
    # Writing name and rank of top international university of the given country
    outfile.write("At international rank => %i the university name is => %s\n" % (topRankInt[0], topRankInt[1]))

    # Calling function to store top national rank and university name of the given country as a tuple
    topRankNat = natRank(uni_list, selectedCountry.upper())
    # Writing name and rank of top national university of the given country
    outfile.write("At national rank => %i the university name is => %s\n" % (topRankNat[0], topRankNat[1]))

    # writing the average score of universities of a given country
    outfile.write("The average score => %.2f\n" % avgScore(uni_list, selectedCountry.upper()))

    # Calling function and storing data returned into multiple variables
    rel, average, highest, continent = relScore(uni_list, cap_list, selectedCountry.upper())
    # Writing the continent relative score in which the country is situated
    outfile.write("The relative score to the top university in %s is => (%.2f / %.2f) * 100%% = %.2f\n" % (continent, average, highest, rel))

    # Writing the name of capital of the given country
    outfile.write("The capital is => %s\n" % capital(cap_list, selectedCountry.upper()))

    # Writing the names of universities having the capital in their name
    outfile.write("The universities that contain the capital name:\n%s\n" % capInName(uni_list, cap_list, selectedCountry.upper()))

    # Closing the file in which data was being written
    outfile.close()

getInformation("japan", "TopUni.csv", "capitals.csv")