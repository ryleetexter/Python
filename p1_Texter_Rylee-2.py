# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 16:02:33 2024

@author: rylee
"""

class Mstring():
    
    #initializes an instance of Mstring and sets the string attribute
    def __init__(self, obj):
        self.__string = str(obj)
        
    #returns the length of the current Mstring
    def __len__(self):
        return len(self.__string)
    
    #returns a string of the Mstring
    def __str__(self):
        return (self.__string)
    
    #returns a representation of the Mstring using __str__
    def __repr__(self):
        return(self.__str__())
    
    #adds an Mstring to another Mstring
    def __add__(self, mstring):
        new_string = self.__string + mstring.__string
        mstring = Mstring(new_string)
        return (mstring)
    
    #adds a string to an Mstring
    def __radd__(self, string):
        new_string = self.__string + string
        mstring = Mstring(new_string)
        return (mstring)
    
    #returns an item at a given index
    def __getitem__(self, index):
        try:
            return self.__string[index]
        except IndexError:
            return("index out of range")
    
    #sets a given character at a given index 
    def __setitem__(self, index, char):
        try:
            chars = []
            
            ##loops through self.__string and adds them to a list chars
            for cha in self.__string:
                chars.append(cha)
                
            #changes the char at given index
            chars[index] = char
            mstring = Mstring('')
            
            #loops through chars list and uses __radd__ to create a 
            #mstring with the correct string after looping
            for cha in chars:
                mstring = mstring.__radd__(cha)
                
            #sets the self.__string to the mstring.__string (string with change)
            self.__string = mstring.__string
        except IndexError as e:
            return("Please enter a valid index")
        
    #returns if two Mstrings are equal
    def __eq__(self, mstring2):
        if (isinstance(mstring2, str)):
            return(self.__string == mstring2)
        elif isinstance(mstring2, Mstring):
            return(self.__string == mstring2.__string)
        else:
            return(False)
        
    #returns if Mstrings do not equal eachother
    def __ne__(self, mstring2):
        if self.__eq__(mstring2):
            return False
        else:
            return True
        
    #replaces a substring in an Mstring with another substring
    #returns index of substring or -1 if not found
    def replace(self, s, t):
        if s in self.__string:
            
            #loops through characters in the self Mstring
            #to find index of substring
            for i in range(len(self.__string)):
                
                #checks if the current index is the substring
                if self.__string[i:i+len(s)] == s:
                    print('here')
                    rang = range(i, i+len(s))
                    count = 0
                    
                    #loops through the substring length and sets the 
                    #characters with the new substring
                    for j in rang:
                        self.__setitem__(t[count], j)
                        count += 1
                    return i
        else:
            return (-1)
      
    #finds the index of a substring in the Mstring and returns the
    #index
    def find(self, substring):
        if substring in self.__string:
            index = self.replace(substring, substring)
            return index
        else:
            return -1
        
#function to test methods and their success/failure
def testif(b, testname, msgOK='', msgFailed=''):
        if b:
            print("Success: " + testname+ "; "+msgOK)
        else:
            print("Failure:"+testname+";"+msgFailed)
        return b
    
    
##tests each Mstring method
def unit_tests():
    #testing __str__
    print("testing on Mstring('Hello World')")
    ms1 = Mstring("Hello World")
    testif(str(ms1) == "Hello World", "__str__() test")
    print()
    
    print("testing on Mstring('')")
    em1 = Mstring('')
    testif(str(em1) == '', "__str__() test")
    print()
    
    #testing __len__
    print("testing on Mstring('Hello World')")
    testif(len(ms1)==11, "__len__() test")
    print()
    
    print("testing on MString('')")
    testif(len(em1)==0, "__len__() test")
    print()
    
    #testing __add__
    print("Testing on Mstring('Hello World') and Mstring ('! Welcome to Python')")
    ms2 = Mstring("! Welcome to Python")
    ms3 = ms1+ms2
    testif(ms3 == "Hello World! Welcome to Python", "__add__() test")
    print()
    
    #testing __radd__
    print("testing on Mstring('World') and Mstring('Hello')")
    string = "World"
    ms4 = Mstring("Hello")
    ms5 = string + ms4
    testif(ms5 == "HelloWorld", "__radd__() test")
    print()
    
    
    #testing __eq__
    print("testing on Mstring('Hi') and Mstring('Hi')")
    ms6 = Mstring("Hi")
    ms7 = Mstring("Hi")
    testif(ms6 == ms7, "__eq__() test")
    print()
    
    #testing __setitem__
    print("Testing Mstring('Hi')[1] = 'a'")
    ms6[1] = 'a'
    testif(ms6 == "Ha", "__setitem__() test")
    print()
    
    #testing __ne__
    print("testing if Mstring('Hi') doesnt equal Mstring('Ha')")
    testif(ms6 != ms7, "__ne__() test")
    print()
    
    #testing __getitem__
    print("testing if Mstring('Hi')[0] == 'H'")
    char = ms7[0]
    testif(char == "H", "__getitem()__ test")
    print()
    
    
    #testing replace
    print("testing replace with Mstrings('rylee') and Mstring('tyler')")
    ms8 = "Hello my name is rylee"
    ms8 = (ms8.replace("rylee", "tyler"))
    testif(ms8 == "Hello my name is tyler", "replace() test")
    print()
    
    


##returns the sorted string of the Mstring
def quicksort(mstring):
    string = str(mstring)
    sorted_string = ''.join(sorted(string))
    return(sorted_string)
    

#tests the quicksort functioin on different Mstrings
def test_sort():
    print("testing quicksort() on Mstring('Hello World')")
    ms1 = Mstring("Hello World")
    print(quicksort(ms1))
    print()
    
    print("testing quicksort() on Mstring('')")
    ms2 = Mstring("")
    print(quicksort(ms2))
    print()
    
    print("testing quicksort() on Mstring(6392249)")
    ms3 = Mstring(6392249)
    print(quicksort(ms3))
    print()


#tests unit_tests() function and test_sort() function
def main():
    unit_tests()
    test_sort()

main()
