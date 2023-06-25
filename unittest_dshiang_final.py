#Unittest for Daniel Shiang Final Project


#import sys
import sys
#import unittest
import unittest
#import Calculator
#import calculator

#COPIED OVER CALCULATOR MODULE FOR CONVENIENCE
#-----------------------------------------------------------------
#create class for calculating mass
class Calculator_mass:
    '''Calculator_mass class calculates mass from molar mass, molarity, volume input'''
    #initialize and attributes
    def __init__(self, molar_mass, molarity, volume):
        self.__molar_mass = molar_mass
        self.molarity = molarity
        self.volume = volume


    def __volmm (self):
        '''__volmm method calculates the total molar mass by volume input'''
        vm = self.__molar_mass * self.volume

        return vm


    def calculate_mass(m):
        '''calculate_mass method multiplies from molarity and __volmm'''
        mass_calc = m.molarity * m.__volmm()
        return mass_calc

    
#create class for calculating volume   
class Calculator_volume:
    '''Calculator_volume class calculates volume from molar mass, molarity, mass input'''
    #initialize and attributes
    def __init__(self, molar_mass, molarity, mass):
        self.__molar_mass = molar_mass
        self.molarity = molarity
        self.mass = mass

    #calculate
    def calculate_volume(v):
        '''calculate_volume method divides mass by molarity and molar mass'''
        volume_calc = (v.mass)/(v.molarity * v.__molar_mass)
        return volume_calc
    

#create class for calculating molarity
class Calculator_molarity:
    '''Calculator_molarity class finds molarity from inputs
        molar mass, volume, and mass'''
    #initialize and attributes
    def __init__(self, molar_mass, volume, mass):
        self.__molar_mass = molar_mass
        self.volume = volume
        self.mass = mass

    #calculate
    def calculate_molarity(mol):
        '''calculate_molarity method divides mass by molar mass and volume'''
        molarity_calc = (mol.mass)/(mol.__molar_mass * mol.volume)
        return molarity_calc



# UNIT TEST BELOW
#----------------------------------------------------------------------------------------

#check the sentence check to see if it works
class Calculator_test(unittest.TestCase):
    '''Calculator_test class passes numbers to calculator module to evaluate module's classes'''

    def test_mass(self):
        '''Test calculate_mass method'''
        #set up
        molar_mass = 1
        molarity = 1
        volume = 1
        
        #action
        result = Calculator_mass(molar_mass, molarity, volume)

        #assert
        self.assertTrue(result, 1)
    

    def test_volume(self):
        ''' Test calculate_volume method'''
        #set up
        molar_mass = 1
        molarity = 1
        mass = 1
        
        #action
        result = Calculator_volume(molar_mass, molarity, mass)

        #assert
        self.assertTrue(result, 1)

    def test_molarity(self):
        '''Test calculate_molarity method'''
        #set up
        molar_mass = 1
        volume = 1
        mass = 1
        
        #action
        result = Calculator_molarity(molar_mass, volume, mass)

        #assert
        self.assertTrue(result, 1)
        

if __name__ == "__main__":
    unittest.main()
