import collections #import for counter, tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox



#root/main window
root = Tk()
root.title("Fetch - Meet your dog")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
#Set up universal variables
dogName = StringVar()   #str - dogs name
adoptedDogName = StringVar()    #str - adopted dogs name - used to remove dog from database
username = StringVar()  #str - username for shelter employees to edit the database
password = StringVar()  #str - password for shelter employees to login and verify identity before gaining access to the database.
train = IntVar()    #int - training
energy = IntVar()   #int
shed = IntVar()     #int
groom = IntVar()    #int
bark = IntVar()     #int
size = IntVar()     #int
firstDog = IntVar()     #int
children = IntVar()     #int
pets = IntVar()     #int
home = IntVar()     #int
yard = IntVar()     #int
allergy = IntVar()      #int
addTrain = IntVar()     #int
addEnergy = IntVar()    #int
addShed = IntVar()      #int
addGroom = IntVar()     #nt
addBark = IntVar()  #int
addSize = IntVar()  #int
addFirstDog = IntVar()  #int
addChildren = IntVar()  #int
addPets = IntVar()  #int
addHome = IntVar()  #int
addYard = IntVar()  #int
addAllergy = IntVar()   #int
adoptedDogsName = StringVar()   #str
highTrain = []
easyTrain = []
lessTrain = []
stubbornTrain = []
highEnergy = []
moreEnergy = []
moderateEnergy = []
lowEnergy = []
highShed = []
averageShed = []
lowShed = []
noShed = []
highGroom = []
moreGroom = []
averageGroom = []
lowGroom = []
highBark = []
moreBark = []
averageBark = []
lessBark = []
xlargeSize = []
largeSize = []
mediumSize = []
smallSize = []
firstDogNo = []
firstDogYes = []
childrenOlder = []
childrenYounger = []
childrenNo = []
petsDog = []
petsCat = []
petOther = []
homeHouse = []
homeApartment = []
largeYard = []
smallYard = []
yardNo = []
lowAllergyYes = []
breedChoice = ['']
breedExclude = ['']
topMatches = []

#Read and add Data from DB-
# Training***
highTrain = [] #set list
highTrain = open('highTrain.txt').read().split(' ') #Read database
for item in highTrain: #Download info to Fetch
    if item in highTrain:
        continue
    else:
        highTrain.append(item) #Add missing Data
easyTrain = []
easyTrain = open('easyTrain.txt').read().split(' ')
for item in easyTrain:
    if item in easyTrain:
        continue
    else:
        easyTrain.append(item)
lessTrain = []
lessTrain = open('lessTrain.txt').read().split(' ')
for item in lessTrain:
    if item in lessTrain:
        continue
    else:
        lessTrain.append(item)
stubbornTrain = []
stubbornTrain = open('stubbornTrain.txt').read().split(' ')
for item in stubbornTrain:
    if item in stubbornTrain:
        continue
    else:
        stubbornTrain.append(item)
#***Energy**
highEnergy = []
highEnergy = open('highEnergy.txt').read().split(' ')
for item in highEnergy:
    if item in highEnergy:
        continue
    else:
        highEnergy.append(item)
moreEnergy = []
moreEnergy = open('moreEnergy.txt').read().split(' ')
for item in moreEnergy:
    if item in moreEnergy:
        continue
    else:
        moreEnergy.append(item)
moderateEnergy = []
moderateEnergy = open('moderateEnergy.txt').read().split(' ')
for item in moderateEnergy:
    if item in moderateEnergy:
        continue
    else:
        moderateEnergy.append(item)
lowEnergy = []
lowEnergy = open('lowEnergy.txt').read().split(' ')
for item in lowEnergy:
    if item in lowEnergy:
        continue
    else:
        lowEnergy.append(item)

#**Shedding***
highShed = []
highShed = open('highShed.txt').read().split(' ')
for item in highShed:
    if item in highShed:
        continue
    else:
        highShed.append(item)
averageShed = []
averageShed = open('averageShed.txt').read().split(' ')
for item in averageShed:
    if item in averageShed:
        continue
    else:
        averageShed.append(item)
lowShed = []
lowShed = open('lowShed.txt').read().split(' ')
for item in lowShed:
    if item in lowShed:
        continue
    else:
        lowShed.append(item)
noShed = []
noShed = open('noShed.txt').read().split(' ')
for item in noShed:
    if item in noShed:
        continue
    else:
        noShed.append(item)

#***Grooming***
highGroom = []
highGroom = open('highGroom.txt').read().split(' ')
for item in highGroom:
    if item in highGroom:
        continue
    else:
        highGroom.append(item)
moreGroom = []
moreGroom = open('moreGroom.txt').read().split(' ')
for item in moreGroom:
    if item in moreGroom:
        continue
    else:
        moreGroom.append(item)
averageGroom = []
averageGroom = open('averageGroom.txt').read().split(' ')
for item in averageGroom:
    if item in averageGroom:
        continue
    else:
        averageGroom.append(item)
lowGroom = []
lowGroom = open('lowGroom.txt').read().split(' ')
for item in lowGroom:
    if item in lowGroom:
        continue
    else:
        lowGroom.append(item)

#***Barking***
highBark = []
highBark = open('highBark.txt').read().split(' ')
for item in highBark:
    if item in highBark:
        continue
    else:
        highBark.append(item)
moreBark = []
moreBark = open('moreBark.txt').read().split(' ')
for item in moreBark:
    if item in moreBark:
        continue
    else:
        moreBark.append(item)
averageBark = []
averageBark = open('averageBark.txt').read().split(' ')
for item in averageBark:
    if item in averageBark:
        continue
    else:
        averageBark.append(item)
lessBark = []
lessBark = open('lessBark.txt').read().split(' ')
for item in lessBark:
    if item in lessBark:
        continue
    else:
        lessBark.append(item)

#***Size***
xlargeSize = []
xlargeSize = open('xlargeSize.txt').read().split(' ')
for item in xlargeSize:
    if item in xlargeSize:
        continue
    else:
        xlargeSize.append(item)
largeSize = []
largeSize = open('largeSize.txt').read().split(' ')
for item in largeSize:
    if item in largeSize:
        continue
    else:
        largeSize.append(item)
mediumSize = []
mediumSize = open('mediumSize.txt').read().split(' ')
for item in mediumSize:
    if item in mediumSize:
        continue
    else:
        mediumSize.append(item)
smallSize = []
smallSize = open('smallSize.txt').read().split(' ')
for item in smallSize:
    if item in smallSize:
        continue
    else:
        smallSize.append(item)

#***Other questions***
firstDogNo = []
firstDogNo = open('firstDogNo.txt').read().split(' ')
for item in firstDogNo:
    if item in firstDogNo:
        continue
    else:
        firstDogNo.append(item)
firstDogYes = []
firstDogYes = open('firstDogYes.txt').read().split(' ')
for item in firstDogYes:
    if item in firstDogYes:
        continue
    else:
        firstDogYes.append(item)
childrenOlder = []
childrenOlder = open('childrenOlder.txt').read().split(' ')
for item in childrenOlder:
    if item in childrenOlder:
        continue
    else:
        childrenOlder.append(item)
childrenYounger = []
childrenYounger = open('childrenYounger.txt').read().split(' ')
for item in childrenYounger:
    if item in childrenYounger:
        continue
    else:
        childrenYounger.append(item)
childrenNo = []
childrenNo = open('childrenNo.txt').read().split(' ')
for item in childrenNo:
    if item in childrenNo:
        continue
    else:
        childrenNo.append(item)
petsDog = []
petsDog = open('petsDog.txt').read().split(' ')
for item in petsDog:
    if item in petsDog:
        continue
    else:
        petsDog.append(item)
petsCat = []
petsCat = open('petsCat.txt').read().split(' ')
for item in petsCat:
    if item in petsCat:
        continue
    else:
        petsCat.append(item)
petOther = []
petOther = open('petOther.txt').read().split(' ')
for item in petOther:
    if item in petOther:
        continue
    else:
        petOther.append(item)
homeHouse = []
homeHouse = open('homeHouse.txt').read().split(' ')
for item in homeHouse:
    if item in homeHouse:
        continue
    else:
        homeHouse.append(item)
homeApartment = []
homeApartment = open('homeApartment.txt').read().split(' ')
for item in homeApartment:
    if item in homeApartment:
        continue
    else:
        homeApartment.append(item)
largeYard = []
largeYard = open('largeYard.txt').read().split(' ')
for item in largeYard:
    if item in largeYard:
        continue
    else:
        largeYard.append(item)
smallYard = []
smallYard = open('smallYard.txt').read().split(' ')
for item in smallYard:
    if item in smallYard:
        continue
    else:
        smallYard.append(item)
yardNo = []
yardNo = open('yardNo.txt').read().split(' ')
for item in yardNo:
    if item in yardNo:
        continue
    else:
        yardNo.append(item)
lowAllergyYes = []
lowAllergyYes = open('lowAllergyYes.txt').read().split(' ')
for item in lowAllergyYes:
    if item in lowAllergyYes:
        continue
    else:
        lowAllergyYes.append(item)


#Set up Employee Window
def openEmployeeLoginWindow():
    employeeLoginWindow = Toplevel(root)
    employeeLoginWindow.title("Shelter Employee Login")
#Set up log in verification
    def employeeLogin():
        if username.get() == "Shelter1" and password.get() == "employeepassword":   #Verify credentials
            employeeLoginWindow.destroy()
            openNewWindow()
        else:
            messagebox.showerror("Error", "Username or Password are incorrect") #Error message for bad log in

    Label(employeeLoginWindow, text="Shelter Employee Username: ").grid(column=0, row=0)
    Label(employeeLoginWindow, text="Password: ").grid(column=0, row=1)
    Entry(employeeLoginWindow, textvariable=username).grid(column=1, row=0)
    Entry(employeeLoginWindow, textvariable=password, show="*").grid(column=1, row=1)
    Button(employeeLoginWindow, text="Login", command=employeeLogin).grid(column=1, row=2)
    Button(employeeLoginWindow, text="Return", command=employeeLoginWindow.destroy).grid(column=2, row=2)


#Set up Adoption window
def openAdoptWindow():
    adoptWindow = Toplevel(root)
    adoptWindow.title("Match with a Dog")
    #Adopter form
    ttk.Label(adoptWindow, text="What are you looking for in a dog?").grid(column=2, row=1)
    ttk.Label(adoptWindow, text="Ready to meet your new best friend?").grid(column=2, row=25)
    ttk.Button(adoptWindow, text="Fetch!", command=calculate).grid(column=3, row=25, sticky=W)
    Button(adoptWindow, text="Return", command=adoptWindow.destroy).grid(column=4, row=25, sticky=W)

    High = ttk.Radiobutton(adoptWindow, text='High', variable=train, value=1).grid(column=1, row=17, sticky=W)
    Easy = ttk.Radiobutton(adoptWindow, text='Easy', variable=train, value=2).grid(column=1, row=18, sticky=W)
    Less = ttk.Radiobutton(adoptWindow, text='Less Easy', variable=train, value=3).grid(column=1, row=19, sticky=W)
    Stubborn = ttk.Radiobutton(adoptWindow, text='Stubborn', variable=train, value=4).grid(column=1, row=20, sticky=W)
    Nopreference = ttk.Radiobutton(adoptWindow, text='No Preference', variable=train, value=5).grid(column=1, row=21, sticky=W)
    ttk.Label(adoptWindow, text="Trainability?").grid(column=1, row=16, sticky=W)

    High = ttk.Radiobutton(adoptWindow, text='High', variable=energy, value=1).grid(column=2, row=17, sticky=W)
    More = ttk.Radiobutton(adoptWindow, text='More', variable=energy, value=2).grid(column=2, row=18, sticky=W)
    Moderate = ttk.Radiobutton(adoptWindow, text='Moderate', variable=energy, value=3).grid(column=2, row=19, sticky=W)
    Low = ttk.Radiobutton(adoptWindow, text='Low', variable=energy, value=4).grid(column=2, row=20, sticky=W)
    Nopreference = ttk.Radiobutton(adoptWindow, text='No Preference', variable=energy, value=5).grid(column=2, row=21,sticky=W)
    ttk.Label(adoptWindow, text="Energy Level?").grid(column=2, row=16, sticky=W)

    High = ttk.Radiobutton(adoptWindow, text='High', variable=shed, value=1).grid(column=3, row=17, sticky=W)
    Average = ttk.Radiobutton(adoptWindow, text='Average', variable=shed, value=2).grid(column=3, row=18, sticky=W)
    Low = ttk.Radiobutton(adoptWindow, text='Low', variable=shed, value=3).grid(column=3, row=19, sticky=W)
    Noshed = ttk.Radiobutton(adoptWindow, text='None', variable=shed, value=4).grid(column=3, row=20, sticky=W)
    Nopreference = ttk.Radiobutton(adoptWindow, text='No Preference', variable=shed, value=5).grid(column=3, row=21,sticky=W)
    ttk.Label(adoptWindow, text="Shed Level?").grid(column=3, row=16, sticky=W)

    High = ttk.Radiobutton(adoptWindow, text='High', variable=groom, value=1).grid(column=4, row=17, sticky=W)
    More = ttk.Radiobutton(adoptWindow, text='More', variable=groom, value=2).grid(column=4, row=18, sticky=W)
    Average = ttk.Radiobutton(adoptWindow, text='Average', variable=groom, value=3).grid(column=4, row=19, sticky=W)
    Low = ttk.Radiobutton(adoptWindow, text='Low', variable=groom, value=4).grid(column=4, row=20, sticky=W)
    Nopreference = ttk.Radiobutton(adoptWindow, text='No Preference', variable=groom, value=5).grid(column=4, row=21, sticky=W)
    ttk.Label(adoptWindow, text="Grooming Level?").grid(column=4, row=16, sticky=W)

    High = ttk.Radiobutton(adoptWindow, text='High', variable=bark, value=1).grid(column=5, row=17, sticky=W)
    More = ttk.Radiobutton(adoptWindow, text='More', variable=bark, value=2).grid(column=5, row=18, sticky=W)
    Average = ttk.Radiobutton(adoptWindow, text='Average', variable=bark, value=3).grid(column=5, row=19, sticky=W)
    Low = ttk.Radiobutton(adoptWindow, text='Low', variable=bark, value=4).grid(column=5, row=20, sticky=W)
    Nopreference = ttk.Radiobutton(adoptWindow, text='No Preference', variable=bark, value=5).grid(column=5, row=21, sticky=W)
    ttk.Label(adoptWindow, text="Barking Level?").grid(column=5, row=16, sticky=W)

    XLarge = ttk.Radiobutton(adoptWindow, text='X-Large', variable=size, value=1).grid(column=6, row=17, sticky=W)
    Large = ttk.Radiobutton(adoptWindow, text='Large', variable=size, value=2).grid(column=6, row=18, sticky=W)
    Average = ttk.Radiobutton(adoptWindow, text='Medium', variable=size, value=3).grid(column=6, row=19, sticky=W)
    Low = ttk.Radiobutton(adoptWindow, text='Small', variable=size, value=4).grid(column=6, row=20, sticky=W)
    Nopreference = ttk.Radiobutton(adoptWindow, text='No Preference', variable=size, value=6).grid(column=6, row=21,sticky=W)
    ttk.Label(adoptWindow, text="Size?").grid(column=6, row=16, sticky=W)

    Yes = ttk.Radiobutton(adoptWindow, text='Yes', variable=firstDog, value=1).grid(column=2, row=3, sticky=W)
    No = ttk.Radiobutton(adoptWindow, text='No', variable=firstDog, value=2).grid(column=3, row=3, sticky=W)
    ttk.Label(adoptWindow, text="First Dog?").grid(column=1, row=3, sticky=E)

    yesOlder = ttk.Radiobutton(adoptWindow, text='Yes 10 and older', variable=children, value=1).grid(column=2, row=4, sticky=W)
    yesYounger = ttk.Radiobutton(adoptWindow, text='Yes 10 and younger', variable=children, value=2).grid(column=3, row=4, sticky=W)
    noKids = ttk.Radiobutton(adoptWindow, text='No', variable=children, value=3).grid(column=4, row=4, sticky=W)
    ttk.Label(adoptWindow, text="Any children in the home?").grid(column=1, row=4, sticky=E)

    otherDog = ttk.Radiobutton(adoptWindow, text='Yes, Dogs', variable=pets, value=1).grid(column=2, row=5, sticky=W)
    otherCat = ttk.Radiobutton(adoptWindow, text='Yes, Cats', variable=pets, value=2).grid(column=3, row=5, sticky=W)
    otherOther = ttk.Radiobutton(adoptWindow, text='Yes, Other', variable=pets, value=3).grid(column=4, row=5, sticky=W)
    noPets = ttk.Radiobutton(adoptWindow, text='No', variable=pets, value=4).grid(column=5, row=5, sticky=W)
    ttk.Label(adoptWindow, text="Other Pets?").grid(column=1, row=5, sticky=E)

    house = ttk.Radiobutton(adoptWindow, text='House', variable=home, value=1).grid(column=2, row=6, sticky=W)
    apartment = ttk.Radiobutton(adoptWindow, text='Apartment', variable=home, value=2).grid(column=3, row=6, sticky=W)
    ttk.Label(adoptWindow, text="House or Apartment?").grid(column=1, row=6, sticky=E)

    yardLarge = ttk.Radiobutton(adoptWindow, text='Yes, Large Yard', variable=yard, value=1).grid(column=2, row=8, sticky=W)
    yardSmall = ttk.Radiobutton(adoptWindow, text='Yes, Small Yard', variable=yard, value=2).grid(column=3, row=8, sticky=W)
    noYard = ttk.Radiobutton(adoptWindow, text='No', variable=yard, value=3).grid(column=4, row=8, sticky=W)
    ttk.Label(adoptWindow, text="Do you have a yard?").grid(column=1, row=8, sticky=E)

    Yes = ttk.Radiobutton(adoptWindow, text='Yes', variable=allergy, value=1).grid(column=2, row=10, sticky=W)
    No = ttk.Radiobutton(adoptWindow, text='No', variable=allergy, value=2).grid(column=3, row=10, sticky=W)
    ttk.Label(adoptWindow, text="Do you need a low allergy dog?").grid(column=1, row=10, sticky=E)
#Define calculate matches
def calculate(*args):
    selection1 = train.get() #Get entry result
    if selection1 == 1: #Compare entry to available options
        breedChoice.extend(highTrain)   #Record Dogs matching selections to a list for results
    if selection1 == 2:
        breedChoice.extend(easyTrain)
    if selection1 == 3:
        breedChoice.extend(lessTrain)
    if selection1 == 4:
        breedChoice.extend(stubbornTrain)
    selection2 = energy.get()
    if selection2 == 1:
        breedChoice.extend(highEnergy)
    if selection2 == 2:
        breedChoice.extend(moreEnergy)
    if selection2 == 3:
        breedChoice.extend(moderateEnergy)
    if selection2 == 4:
        breedChoice.extend(lowEnergy)
    selection3 = shed.get()
    if selection3 == 1:
        breedChoice.extend(highShed)
    if selection3 == 2:
        breedChoice.extend(averageShed)
    if selection3 == 3:
        breedChoice.extend(lowShed)
    if selection3 == 4:
        breedChoice.extend(noShed)
    selection4 = groom.get()
    if selection4 == 1:
        breedChoice.extend(highGroom)
    if selection4 == 2:
        breedChoice.extend(moreGroom)
    if selection4 == 3:
        breedChoice.extend(averageGroom)
    if selection4 == 4:
        breedChoice.extend(lowGroom)
    selection5 = bark.get()
    if selection5 == 1:
        breedChoice.extend(highBark)
    if selection5 == 2:
        breedChoice.extend(moreBark)
    if selection5 == 3:
        breedChoice.extend(averageBark)
    if selection5 == 4:
        breedChoice.extend(lessBark)
    selection6 = size.get()
    if selection6 == 1:
        breedChoice.extend(xlargeSize)
    if selection6 == 2:
        breedChoice.extend(largeSize)
    if selection6 == 3:
        breedChoice.extend(mediumSize)
    if selection6 == 4:
        breedChoice.extend(smallSize)
    selection10 = home.get()
    if selection10 == 1:
        breedChoice.extend(homeHouse)
    if selection10 == 2:
        breedChoice.extend(homeApartment)
    selection11 = yard.get()
    if selection11 == 1:
        breedChoice.extend(largeYard)
    if selection11 == 2:
        breedChoice.extend(smallYard)
    selection7 = firstDog.get()
    if selection7 == 1:
        breedExclude.extend(firstDogYes)    #record dogs to a seperate list who can not go to a first time owner/can't live with kids/exc. to exclude from final results
    selection8 = children.get()
    if selection8 == 1:
         breedExclude.extend(childrenOlder)
    if selection8 == 2:
        breedExclude.extend(childrenYounger)
    selection9 = pets.get()
    if selection9 == 1:
        breedExclude.extend(petsDog)
    if selection9 == 2:
        breedExclude.extend(petsCat)
    if selection9 == 3:
        breedExclude.extend(petOther)
    if selection11 == 3:
        breedExclude.extend(yardNo)
    selection12 = allergy.get()
    if selection12 == 1:
        breedExclude.extend(lowAllergyYes)
    openResultsWindow() #open success/results window
#Set up Results page for top matches
def openResultsWindow():
    printResults = Toplevel(root)
    result = [i for i in breedChoice if i not in breedExclude]  #Remove excluded dogs from results
    topMatches = collections.Counter(result).most_common(3) #Count matches and return top three
    for x in range(len(topMatches)):    #Print up to top three best matched dogs
        matchName = str(topMatches[x])
        Label(printResults, text=matchName).grid(column=1, row=2+x)
    Label(printResults, text="Top Matches: ").grid(column=1, row=1, sticky=W)
    Button(printResults, text="Close", command=printResults.destroy).grid(column=1, row=6, sticky=W)
#Define launch add/remove dog window
def openNewWindow():

    #define command remove dog from Fetch
    def removeDog(*args):
        adoptedDogsName = adoptedDogName.get() #Get entry for Dog name
        if adoptedDogsName in highTrain:       #compare to database
            with open('highTrain.txt', 'r') as file:
                text = file.read()
            with open('highTrain.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')  #Remove Dog's name
                file.write(new_text)        #rewrite back to the Database
        if adoptedDogsName in easyTrain:
            with open('easyTrain.txt', 'r') as file:
                text = file.read()
            with open('easyTrain.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in lessTrain:
            with open('lessTrain.txt', 'r') as file:
                text = file.read()
            with open('lessTrain.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in stubbornTrain:
            with open('stubbornTrain.txt', 'r') as file:
                text = file.read()
            with open('stubbornTrain.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in highEnergy:
            with open('highEnergy.txt', 'r') as file:
                text = file.read()
            with open('highEnergy.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in moreEnergy:
            with open('moreEnergy.txt', 'r') as file:
                text = file.read()
            with open('moreEnergy.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in moderateEnergy:
            with open('moderateEnergy.txt', 'r') as file:
                text = file.read()
            with open('moderateEnergy.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in lowEnergy:
            with open('lowEnergy.txt', 'r') as file:
                text = file.read()
            with open('lowEnergy.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in highShed:
            with open('highShed.txt', 'r') as file:
                text = file.read()
            with open('highShed.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in averageShed:
            with open('averageShed.txt', 'r') as file:
                text = file.read()
            with open('averageShed.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in lowShed:
            with open('lowShed.txt', 'r') as file:
                text = file.read()
            with open('lowShed.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in noShed:
            with open('noShed.txt', 'r') as file:
                text = file.read()
            with open('noShed.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in highGroom:
            with open('highGroom.txt', 'r') as file:
                text = file.read()
            with open('highGroom.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in moreGroom:
            with open('moreGroom.txt', 'r') as file:
                text = file.read()
            with open('moreGroom.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in averageGroom:
            with open('averageGroom.txt', 'r') as file:
                text = file.read()
            with open('averageGroom.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in lowGroom:
            with open('lowGroom.txt', 'r') as file:
                text = file.read()
            with open('lowGroom.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in highBark:
            with open('highBark.txt', 'r') as file:
                text = file.read()
            with open('highBark.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in moreBark:
            with open('moreBark.txt', 'r') as file:
                text = file.read()
            with open('moreBark.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in lessBark:
            with open('lessBark.txt', 'r') as file:
                text = file.read()
            with open('lessBark.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in averageBark:
            with open('averageBark.txt', 'r') as file:
                text = file.read()
            with open('averageBark.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in xlargeSize:
            with open('xlargeSize.txt', 'r') as file:
                text = file.read()
            with open('xlargeSize.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in largeSize:
            with open('largeSize.txt', 'r') as file:
                text = file.read()
            with open('largeSize.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in mediumSize:
            with open('mediumSize.txt', 'r') as file:
                text = file.read()
            with open('mediumSize.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in smallSize:
            with open('smallSize.txt', 'r') as file:
                text = file.read()
            with open('smallSize.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in firstDogYes:
            with open('firstDogYes.txt', 'r') as file:
                text = file.read()
            with open('firstDogYes.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in firstDogNo:
            with open('firstDogNo.txt', 'r') as file:
                text = file.read()
            with open('firstDogNo.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in childrenOlder:
            with open('childrenOlder.txt', 'r') as file:
                text = file.read()
            with open('childrenOlder.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in childrenYounger:
            with open('childrenYounger.txt', 'r') as file:
                text = file.read()
            with open('childrenYounger.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in childrenNo:
            with open('childrenNo.txt', 'r') as file:
                text = file.read()
            with open('childrenNo.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in petsDog:
            with open('petsDog.txt', 'r') as file:
                text = file.read()
            with open('petsDog.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in petsCat:
            with open('petsCat.txt', 'r') as file:
                text = file.read()
            with open('petsCat.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in petOther:
            with open('petOther.txt', 'r') as file:
                text = file.read()
            with open('petOther.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in homeApartment:
            with open('homeApartment.txt', 'r') as file:
                text = file.read()
            with open('homeApartment.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in homeHouse:
            with open('homeHouse.txt', 'r') as file:
                text = file.read()
            with open('homeHouse.txtm', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in largeYard:
            with open('largeYard.txt', 'r') as file:
                text = file.read()
            with open('largeYard.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in smallYard:
            with open('smallYard.txt', 'r') as file:
                text = file.read()
            with open('smallYard.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in yardNo:
            with open('yardNo.txt', 'r') as file:
                text = file.read()
            with open('yardNo.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        if adoptedDogsName in lowAllergyYes:
            with open('lowAllergyYes.txt', 'r') as file:
                text = file.read()
            with open('lowAllergyYes.txt', 'w') as file:
                new_text = text.replace(adoptedDogsName, '')
                file.write(new_text)
        removeSuccessWindow() #Launch 'success' message when finished
#Define remove success window
    def removeSuccessWindow():
        removeSuccess = Toplevel(root)
        Label(removeSuccess, text="Congrats!The dog is now removed from Fetch").grid(column=1, row=2)
        Button(removeSuccess, text="Close", command=removeSuccess.destroy).grid(column=1, row=3, sticky=W)

    #Define command: adding dog to Fetch
    def addDog(*args):
        dogsName = dogName.get() #Get dog name
        selectionAdd1 = addTrain.get()
        if selectionAdd1 == 1:  #Check for entry, if match add dog to the database
            with open('highTrain.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd1 == 2:
            with open('easyTrain.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd1 == 3:
            with open('lessTrain.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd1 == 4:
            with open('stubbornTrain.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        selectionAdd2 = addEnergy.get()
        if selectionAdd2 == 1:
            with open('highEnergy.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd2 == 2:
            with open('moreEnergy.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd2 == 3:
            with open('moderateEnergy.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd2 == 4:
            with open('lowEnergy.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        selectionAdd3 = addShed.get()
        if selectionAdd3 == 1:
            with open('highShed.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd3 == 2:
            with open('averageShed.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd3 == 3:
            with open('lowShed.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd3 == 4:
            with open('noShed.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        selectionAdd4 = addGroom.get()
        if selectionAdd4 == 1:
            with open('highGroom.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd4 == 2:
            with open('moreGroom.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd4 == 3:
            with open('averageGroom.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd4 == 4:
            with open('lowGroom.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        selectionAdd5 = addBark.get()
        if selectionAdd5 == 1:
            with open('highBark.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd5 == 2:
            with open('moreBark.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd5 == 3:
            with open('averageBark.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd5 == 4:
            with open('lessBark.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        selectionAdd6 = addSize.get()
        if selectionAdd6 == 1:
            with open('xlargeSize.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd6 == 2:
            with open('largeSize.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd6 == 3:
            with open('mediumSize.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd6 == 4:
            with open('smallSize.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        selectionAdd7 = addFirstDog.get()
        if selectionAdd7 == 1:
            with open('firstDogYes.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        selectionAdd8 = addChildren.get()
        if selectionAdd8 == 1:
            with open('childrenOlder.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd8 == 2:
            with open('childrenYounger.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        selectionAdd9 = addPets.get()
        if selectionAdd9 == 1:
            with open('petsDog.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd9 == 2:
            with open('petsCat.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd9 == 3:
            with open('petOther.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        selectionAdd10 = addHome.get()
        if selectionAdd10 == 1:
            with open('homeHouse.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd10 == 2:
            with open('homeApartment.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        selectionAdd11 = addYard.get()
        if selectionAdd11 == 1:
            with open('largeYard.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd11 == 2:
            with open('smallYard.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        if selectionAdd11 == 3:
            with open('yardNo.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        selectionAdd12 = addAllergy.get()
        if selectionAdd12 == 1:
            with open('lowAllergyYes.txt', 'a') as f:
                f.write("{}{}".format(dogsName, " "))
        addSuccessWindow() #launch success message when finished

#define success window
    def addSuccessWindow():
        addSuccess = Toplevel(root)
        Label(addSuccess, text="Good Luck! The dog has been added to Fetch").grid(column=1, row=2)
        Button(addSuccess, text="Close", command=addSuccess.destroy).grid(column=1, row=3, sticky=W)
#Label for shelter page
    newWindow = Toplevel(root)
    newWindow.title("Add/Remove Dog from Fetch")

### Add/Remove Dog from Fetch window
    ttk.Label(newWindow, text="New Dog Profile").grid(column=3, row=0)
    ttk.Button(newWindow, text="Submit", command=addDog).grid(column=3, row=25, sticky=W)
    ttk.Label(newWindow, text="Name?").grid(column=1, row=2, sticky=E)
    ttk.Entry(newWindow, textvariable=dogName).grid(column=2, row=2, sticky=W)
    ttk.Entry(newWindow, textvariable=adoptedDogName).grid(column=3, row=28, sticky=W)
    ttk.Button(newWindow, text="Remove", command=removeDog).grid(column=4, row=28, sticky=S)
    ttk.Label(newWindow, text="Dog been Adopted?").grid(column=3, row=27)
    ttk.Label(newWindow, text="Enter the name here to be removed from the list").grid(column=2, row=28)
    ttk.Button(newWindow, text="Return", command=newWindow.destroy).grid(column =5, row=28)


    addTrain = IntVar()
    High = ttk.Radiobutton(newWindow, text='Highly trainable', variable=addTrain, value=1).grid(column=1, row=17, sticky=W)
    Easy = ttk.Radiobutton(newWindow, text='Easily', variable=addTrain, value=2).grid(column=1, row=18, sticky=W)
    Less = ttk.Radiobutton(newWindow, text='Less Easy', variable=addTrain, value=3).grid(column=1, row=19, sticky=W)
    Stubborn = ttk.Radiobutton(newWindow, text='Stubborn', variable=addTrain, value=4).grid(column=1, row=20, sticky=W)
    noData = ttk.Radiobutton(newWindow, text='Not sure/No data', variable=addTrain, value=5).grid(column=1, row=21, sticky=W)
    ttk.Label(newWindow, text="Does the dog learn quickly?").grid(column=1, row=16, sticky=W)

    addEnergy = IntVar()
    High = ttk.Radiobutton(newWindow, text='High', variable=addEnergy, value=1).grid(column=2, row=17, sticky=W)
    More = ttk.Radiobutton(newWindow, text='More', variable=addEnergy, value=2).grid(column=2, row=18, sticky=W)
    Moderate = ttk.Radiobutton(newWindow, text='Moderate', variable=addEnergy, value=3).grid(column=2, row=19, sticky=W)
    Low = ttk.Radiobutton(newWindow, text='Low', variable=addEnergy, value=4).grid(column=2, row=20, sticky=W)
    noData = ttk.Radiobutton(newWindow, text='Not sure/No data', variable=addEnergy, value=5).grid(column=2, row=21, sticky=W)
    ttk.Label(newWindow, text="Energy Level?").grid(column=2, row=16, sticky=W)

    addShed = IntVar()
    High = ttk.Radiobutton(newWindow, text='High', variable=addShed, value=1).grid(column=3, row=17, sticky=W)
    Average = ttk.Radiobutton(newWindow, text='Average', variable=addShed, value=2).grid(column=3, row=18, sticky=W)
    Low = ttk.Radiobutton(newWindow, text='Low', variable=addShed, value=3).grid(column=3, row=19, sticky=W)
    Noshed = ttk.Radiobutton(newWindow, text='None', variable=addShed, value=4).grid(column=3, row=20, sticky=W)
    noData = ttk.Radiobutton(newWindow, text='Not sure/No data', variable=addShed, value=5).grid(column=3, row=21, sticky=W)
    ttk.Label(newWindow, text="Shed Level?").grid(column=3, row=16, sticky=W)

    addGroom = IntVar()
    High = ttk.Radiobutton(newWindow, text='High', variable=addGroom, value=1).grid(column=4, row=17, sticky=W)
    More = ttk.Radiobutton(newWindow, text='More', variable=addGroom, value=2).grid(column=4, row=18, sticky=W)
    Average = ttk.Radiobutton(newWindow, text='Average', variable=addGroom, value=3).grid(column=4, row=19, sticky=W)
    Low = ttk.Radiobutton(newWindow, text='Low', variable=addGroom, value=4).grid(column=4, row=20, sticky=W)
    noData = ttk.Radiobutton(newWindow, text='Not sure/No data', variable=addGroom, value=5).grid(column=4, row=21, sticky=W)
    ttk.Label(newWindow, text="Grooming Level?").grid(column=4, row=16, sticky=W)

    addBark = IntVar()
    High = ttk.Radiobutton(newWindow, text='High', variable=addBark, value=1).grid(column=5, row=17, sticky=W)
    More = ttk.Radiobutton(newWindow, text='More', variable=addBark, value=2).grid(column=5, row=18, sticky=W)
    Average = ttk.Radiobutton(newWindow, text='Average', variable=addBark, value=3).grid(column=5, row=19, sticky=W)
    Low = ttk.Radiobutton(newWindow, text='Low', variable=addBark, value=4).grid(column=5, row=20, sticky=W)
    noData = ttk.Radiobutton(newWindow, text='Not sure/No data', variable=addBark, value=5).grid(column=5, row=21, sticky=W)
    ttk.Label(newWindow, text="Barking Level?").grid(column=5, row=16, sticky=W)

    addSize = IntVar()
    XLarge = ttk.Radiobutton(newWindow, text='X-Large', variable=addSize, value=1).grid(column=6, row=17, sticky=W)
    Large = ttk.Radiobutton(newWindow, text='Large', variable=addSize, value=2).grid(column=6, row=18, sticky=W)
    Average = ttk.Radiobutton(newWindow, text='Medium', variable=addSize, value=3).grid(column=6, row=19, sticky=W)
    Low = ttk.Radiobutton(newWindow, text='Small', variable=addSize, value=4).grid(column=6, row=20, sticky=W)
    noData = ttk.Radiobutton(newWindow, text='Not sure/No data', variable=addSize, value=6).grid(column=5, row=21, sticky=W)
    ttk.Label(newWindow, text="Size?").grid(column=6, row=16, sticky=W)

    addFirstDog = IntVar()
    Yes = ttk.Radiobutton(newWindow, text='Yes', variable=addFirstDog, value=2).grid(column=2, row=3, sticky=W)
    No = ttk.Radiobutton(newWindow, text='No', variable=addFirstDog, value=1).grid(column=3, row=3, sticky=W)
    ttk.Label(newWindow, text="Suitable for a first time dog owner?").grid(column=1, row=3, sticky=E)

    addChildren = IntVar()
    yesOlder = ttk.Radiobutton(newWindow, text='Yes', variable=addChildren, value=3).grid(column=2, row=4, sticky=W)
    yesYounger = ttk.Radiobutton(newWindow, text='Yes, 10 and older only', variable=addChildren, value=2).grid(column=3, row=4, sticky=W)
    noKids = ttk.Radiobutton(newWindow, text='No', variable=addChildren, value=1).grid(column=4, row=4, sticky=W)
    ttk.Label(newWindow, text="Suitable around kids?").grid(column=1, row=4, sticky=E)

    addPets = IntVar()
    otherDog = ttk.Radiobutton(newWindow, text='No Dogs', variable=addPets, value=1).grid(column=2, row=5, sticky=W)
    otherCat = ttk.Radiobutton(newWindow, text='No Cats', variable=addPets, value=2).grid(column=3, row=5, sticky=W)
    otherOther = ttk.Radiobutton(newWindow, text='No Other', variable=addPets, value=3).grid(column=4, row=5, sticky=W)
    noPets = ttk.Radiobutton(newWindow, text='Yes', variable=addPets, value=4).grid(column=5, row=5, sticky=W)
    ttk.Label(newWindow, text="Safe with other Pets?").grid(column=1, row=5, sticky=E)

    addHome = IntVar()
    house = ttk.Radiobutton(newWindow, text='House', variable=addHome, value=1).grid(column=2, row=6, sticky=W)
    apartment = ttk.Radiobutton(newWindow, text='Apartment', variable=addHome, value=2).grid(column=3, row=6, sticky=W)
    ttk.Label(newWindow, text="House or Apartment?").grid(column=1, row=6, sticky=E)

    addYard = IntVar()
    yardLarge = ttk.Radiobutton(newWindow, text='Large Yard', variable=addYard, value=1).grid(column=2, row=8, sticky=W)
    yardSmall = ttk.Radiobutton(newWindow, text='Small Yard', variable=addYard, value=2).grid(column=3, row=8, sticky=W)
    noData = ttk.Radiobutton(newWindow, text='Not Sure/No Data', variable=addYard, value=3).grid(column=4, row=8, sticky=W)
    ttk.Label(newWindow, text="Yard size preference?").grid(column=1, row=8, sticky=E)

    addAllergy = IntVar()
    Yes = ttk.Radiobutton(newWindow, text='Yes', variable=addAllergy, value=2).grid(column=2, row=10, sticky=W)
    No = ttk.Radiobutton(newWindow, text='No', variable=addAllergy, value=1).grid(column=3, row=10, sticky=W)
    ttk.Label(newWindow, text="Low allergy?").grid(column=1, row=10, sticky=E)
    newWindow.mainloop()
#Set up for main window
Label(root, text="Shelter?").grid(column=1, row=28, sticky=W)
Label(root, text="Looking to Adopt?").grid(column=1, row=27, sticky=W)
Button(root, text="Match with a Dog", command=openAdoptWindow).grid(column=2, row=27)
Button(root, text="Shelter Login", command=openEmployeeLoginWindow).grid(column=2, row=28)
Button(root, text="Close", command=root.destroy).grid(column=2, row=29, sticky=W)

root.mainloop()