#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Brennan
#
# Created:     01/09/2015
# Copyright:   (c) Brennan 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Person:
    def __init__(self, name, race, sex, age):
        """constructor method for the people
        started be declaring all the attributes"""
        self.Race = race
        self.Sex = sex
        self.Age = age
        self.Name = name

    def ConstuctSentence(self):
        print("My name is "+ str(self.Name))

    def MyAge(self):
        print("And my age is "+str(self.Age))

    def MySex(self):
        print("And I am"+str(self.Sex))



Brennan = Person("Brennan","White","Male", 17)

