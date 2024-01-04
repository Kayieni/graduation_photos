import urllib.request
import csv

photocode=0
total=0

# The code provided by the photographers is the "40140". 
# The letter "S" following the above number represents the set of photos depending on 
    # the date and time of the graduation. It is not standard and this has to change manually.
# Please modify the url accordingly.

url="https://img.snaphoto.gr/orkomosies/40140S/large/"

# csv file should have the following structure in order to work
#   each line represents a set of photos:
#       first column has the total photos of the set (e.g. from number 001 to number 010, there are 10 photos)
#       second column has the name of the first photo of the set copied as shown in the original website 
#       third column is optional; it can contain the last 2 digits of the name of the last photo from the current set, 
#           for checking purposes only. Its not used by the program

with open("grad.csv", mode="r") as f:
    print("working on it, be patient...")
    file = csv.reader(f,delimiter="\t")
    for lines in file:
        counter=int(lines[0])
        photocode=int(lines[1].split("-")[2])
        while counter!=0:
            urllib.request.urlretrieve(url + str(photocode).zfill(5) + ".jpg", "photos/"+ str(photocode).zfill(5) + ".png") 
            counter-=1
            photocode+=1
            total+=1
    print(total)