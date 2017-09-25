#Blob Detection
#By Vlad Sinitsa
#Using Python 2.7
import sys


def readfile(filename):
    blob_array = []
    try:
        fin = open(filename, "r")
    except IOError:
        print("Error opening file")
        return False
    for line in fin:
        blob_array.append(line.strip().split(" "))
    return blob_array


#modified recursive dfs search, to search for only the specified character
def find_count(startx, starty, x, y, character, count, array):
    array[x][y] = "F" #mark current location as visited
    count += 1
    if x - 1 >= 0:
        if not(startx == x - 1 and starty == y) and array[x - 1][y] == character:
            count = find_count(x, y, x-1, y, character, count, array)

    if y + 1 < len(array[0]):
        if not(startx == x and starty == y + 1) and array[x][y + 1] == character:
            count = find_count(x, y, x, y+1, character, count, array)

    if x + 1 < len(array):
        if not(startx == x + 1 and starty == y) and array[x + 1][y] == character:
            count = find_count(x, y, x + 1, y, character, count, array)

    if y - 1 >= 0:
        if not(startx == x and starty == y - 1) and array[x][y - 1] == character:
            count = find_count(x, y, x, y-1, character, count, array)

    return count


def run(array):
    output = {"X": 0, "O": 0}  # output dictionary to be printed
    for x in range(len(array)):
        for y in range(len(array[x])):
            '''Since the algorithm marks spots that its already visited I don't need to send every point 
            in the array through the recursive function just the next point that hasn't been visited by the previous 
            blob'''
            if not(array[x][y] == "F"):
                char = array[x][y]
                temp = find_count(x,y,x,y,array[x][y], 0, array)
                if temp > output.get(char):
                    output[char] = temp
    return output

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Please provide a file!")
        exit()
    else:
        filename = sys.argv[1]

    if not readfile(filename):
        exit(1)
    else:
        blob_array = readfile(filename)
        print(run(blob_array))
