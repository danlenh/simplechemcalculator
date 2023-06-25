#import class, system, and OS
import sys
import calculator
import os

#----------------------------------------------------------------------------------------------
#Intro
print("Hello, welcome to the compound and solution calculator!")

#Ask for name of compound/solution and append to list
compound_name = []
name_input = input("Enter the name of your compound:     \n")
compound_name.append(name_input)


#---------------------------------------------------------------------------------------------
#tuple of correct options to choose from
selection_list = ('1', '2', '3', 'MASS', 'VOLUME', 'MOLARITY')

#Reprompt entry until correct
while True:

    #Ask what value user wants to calculate
    print("What would you like to calculate today? \
      \n Please enter your choice (ex: '1' or 'Mass' to calculate Mass)")
    selection = input("1) MASS     2) VOLUME     3) MOLARITY     \n")

    
    if selection.upper() not in selection_list:
        print("Please enter a correct option. Example: '1' or 'Mass' to calculate Mass")
    else:
        break

#----------------------------------------------------------------------------------------------
#User is then given prompts to enter relevant values for their chosen calculation 

#Calculate mass

if selection == '1' or selection.upper() == 'MASS':
    print('Calculating Mass from molarity, molar mass, and volume')
    print("Please enter the molarity (M), molar mass (g/mol), and volume (liter)")

    while True:
        try:
            molarity = float(input('Please enter concentration in molars (M):     '))
            break
        except:
            print('Try again. Please enter a valid number (integer or float)')
            
    while True:
        try:
            molar_mass = float(input('Please enter molar mass (g/mol):     '))
            break
        except:
            print('Try again. Please enter a valid number (integer or float)')

    while True:
        try:
            volume = float(input('Please enter volume in liters (L):     '))
            break
        except:
            print('Try again. Please enter a valid number (integer or float)')


    #use the class methods to calculate mass
    def mass_data(molarity, molar_mass, volume):
        '''mass_data calculates mass from molarity, molar mass, and volume'''
        mass_object = calculator.Calculator_mass(float(molarity), float(molar_mass), float(volume))                                             
        mass_number = mass_object.calculate_mass()
        return round(mass_number, 3)

    #output
    statement = 'MASS of '
    print(str(statement) +  str(compound_name[0]) + ' is: ' + str(mass_data(molarity, molar_mass, volume)) + 'g')
    r = repr(calculator.Return_statement())
    print(r)

      
       
#Calculate volume
elif selection == '2' or selection.upper() == 'VOLUME':
    print("Calculating volume from mass, molar mass, and molarity")
    print("Please enter the mass (grams), molar mass (g/mol), and molarity (M)")

    while True:
        try:
            mass = float(input('Please enter mass of the compound (g):      '))
            test = 1/mass
            break
        except:
            print('Please enter a valid number (integer or float) and NO ZERO')
            
    while True:
        try:
            molar_mass = float(input('Please enter molar mass (g/mol):     '))

            test = 1/molar_mass
            break
        except:
            print('Please re-enter a valid number (integer or float) and NO ZERO.')
        else:
            print('Invalid Input, please try again.')

    while True:
        try:
            molarity = float(input('Please enter concentration in molars (M):     '))

            test = 1/molarity
            break
        except:
            print('Please re-enter a valid number (integer or float) and NO ZERO.')
        else:
            print('Invalid Input, please try again.')
            
            
    

    #use class methods to calculate volume
    def volume_data(mass, molar_mass, molarity):
        '''volume_data calculates volume from mass, molar mass, and molarity'''
        volume_object = calculator.Calculator_volume(float(molarity), float(molar_mass), float(mass))
        volume_number = volume_object.calculate_volume()
        return round(volume_number, 3)

    #output
    statement = 'VOLUME of '
    print(str(statement) +  str(compound_name[0]) + ' is: ' + str(volume_data(molarity, molar_mass, molarity)) + 'L')
    r = repr(calculator.Return_statement())
    print(r)       


#Calculate molarity
elif selection == '3' or selection.upper() == 'MOLARITY':
    print("Calculating molarity from mass, molar mass, and volume")
    print("Please enter the mass (grams), formula weight (daltons), and volume (liter)")

    while True:
        try:
            mass = float(input('Please enter mass of the compound (g):      '))
            test = 1/mass
            break
        except:
            print('Try again. Please enter a valid number (integer or float) and NO ZERO')
            
    while True:
        try:
            molar_mass = float(input('Please enter molar mass (g/mol):     '))
            test = 1/molar_mass
            break
        except:
            print('Please re-enter a valid number (integer or float) and NO ZERO.')
        else:
            print('Please try again.')

    while True:
        try:
            volume = float(input('Please enter volume in liters (L):     '))
            test = 1/volume
            break
        except:
            print('Please re-enter a valid number (integer or float) and NO ZERO.')
        else:
            print('Please try again.')

    #use class methods to calculate molarity
    def molarity_data(mass, molar_mass, volume):
        '''molarity_data calculates molarity from mass, molar mass, and volume'''
        molarity_object = calculator.Calculator_molarity(float(mass), float(molar_mass), float(volume))
        molarity_number = molarity_object.calculate_molarity()
        return round(molarity_number, 3)

    #output
    statement = 'MOLARITY of '
    print(str(statement) + str(compound_name[0]) + ' is: ' + str(molarity_data(mass, molar_mass, volume)) + 'M')
    r = repr(calculator.Return_statement())
    print(r)

#If invalid input, give user warning, and prompt user restart
else:
    sys.exit('You were not supposed to reach this. Congrats you broke the program!')


#------------------------------------------------------------------------------------------
#calculate half life option and ask user to exit/restart program


selection_set1 = {'Y', 'YES', 'N', 'NO'}

#prompt user to upload file to calculate half life
while True:
    prompt = input('UPLOAD data to calculate half life of a compound? YES/Y or NO/N: ')
    
    if prompt.upper() not in selection_set1:
        print('Please enter either YES/Y or NO/N')
    else:
        break

if prompt.upper() == 'YES' or prompt.upper() == 'Y':

    try:
        file1 = open("half_life.txt", 'r')

    except OSError:
        print("File error, check file.")
        sys.exit()

    #read the text file as str
    file1_read = str(file1.read())

    #extract words from string
    extract_words = file1_read.split()

    #get name from file
    name = extract_words[0]

    #try to extract decay_constant, and if non-valid number, error message
    try:
        decay_constant = float(extract_words[1])
    except:
        sys.exit('Please make sure decay constant in file is INT or FLOAT')

    #calculate half life from 0.693 constant and decay constant input from file    
    half_life = round(0.693/decay_constant, 3)

    print('The half life of {0} is {1} years'.format(name, half_life))             
      
else:
    print('Next Question: ')
    

#prompt to restart
print('\n')

selection_set = {'Y', 'YES', 'N', 'NO'}

while True:
    prompt = input('Would you like to run another calculation? Yes/Y or No/N: ')
    
    if prompt.upper() not in selection_set:
        print('Please enter either "Y" for Yes or "N" for No')
    else:
        break

if prompt.upper() == 'Y' or prompt.upper() == 'YES':
    print('Shell restarting.')
    os.execl(sys.executable, sys.executable, *sys.argv)
   
elif prompt.upper() == 'N' or prompt.upper() == 'NO':
    sys.exit('Thank you for using calculator')
    
else:
    print('Try again.')

    


#---------------------------------------------------------------------------------------------- 
