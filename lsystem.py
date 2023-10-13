"""
lsystem.py
Jordyn Kim
CS151-B Computational Thinking: Visual Media
Fall 2020
11/22/2020
Lab 10: Event-based programming
Write Lsystem class that creates the L-system string with random variations
"""

import random


class Lsystem:
    def __init__(self, filename=None):
        '''L-system class constructor

        Parameters:
        -----------
        filename: str. Filename of the L-system text file with the base string 
        and 1+ replacement rules (DEFAULT: None)
        '''

        # Create an instance variable for the base string
        self.basestring = ''

        # Create an instance variable for your replacement rules
        self.replacementRule = []

        # Check if filename passed in (i.e. parameter is not None)
        # If so, read in the L-system from the file called
        # filename.
        if filename != None:
            self.read(filename) 
    

    def getBase(self):
        """
        Method to get the base string
        """
        return self.basestring


    def setBase(self, newBase):
        """
        Method to set the base string
        
        Parameters:
        -----------
        newBase = str. The new base string of the L-system text
        """
        self.basestring = newBase


    def getRule(self, ruleIdx):
        """
        Method to get the rule sublist (a two element list) at index 
    
        Parameters:
        -----------
        ruleIdx = int. The rule number 
        """
        return self.replacementRule[ruleIdx]
    

    def addRule(self, newRule):
        """
        Method to append a new replacement rule newRule to the current list of replacement rules.
        
        Parameters:
        -----------
        newRule = 2 item list. The new replacement rule that is a 2 item list
        """
        self.replacementRule.append(newRule)


    def numRules(self):
        """
        Method that returns the number of replacement rules currently in the L-system
        """
        return len(self.replacementRule)


    def read(self, filename):
        '''Reads the L-system base string and 1+ rules from a text file. Stores the data in the
        instance variables in the constructor in the format:

        base string: str.
            e.g. `'F-F-F-F'`
        replacement rules: list of elements sublists.
            e.g. `[['F', 'FF-F+F-F-FF']]` for one rule

        Parameters:
        -----------
        filename: str. Filename of the L-system text file with the base string and 1+ replacement
            rules
        '''
        # Open the file called filename
        file = open(filename, 'r')

        # Read in the file line-by-line.
        oneLine = file.readline() # read first line
        while oneLine != '':
            # For each line, split it into a list.
            oneLine = oneLine.strip()
            thisLine = oneLine.split(' ')

            #   If the first list item is 'base', set the L-system base string
            #   to the second item in the list.
            if thisLine[0] == 'base':
                self.setBase(thisLine[1])

            #   If the first list item is 'rule', add a rule to your replacement
            #   rules consisting of the find and replace strings
            #   (2nd, 3rd, etc. items in the list).
            #   Remember: We add a rule in list format: [find str, replace str]
            elif thisLine[0] == 'rule':
                thisRule = []
                for item in thisLine[1:]:
                    thisRule.append(item)
                self.addRule(thisRule)

            # Read next line
            oneLine = file.readline()
            
        # Close the file
        file.close()


    def replace(self, currString):
        '''Applies the full set of replacement rules to current 'base' L-system string `currString`.

        Overall strategy:
        - Scan the L-system string left to right, char by char
        - Apply AT MOST ONE replacement rule to a matching character.
            Example: If the current char is 'F' and that matches a rule's find string 'F', apply
            that rule then move onto the next character in the L-system string (don't try to match
            more rules to the current char).
        - If no rule matches a rule find string, we just add the char as-is to the new string.

        Parameters:
        -----------
        currString: str. The current L-system base string.

        Returns:
        -----------
        newString: str. The base string `currString` with replacement rules applied to it.
        '''
        newString = ''

        for char in currString:
            # check to see if char matches
            # find string in rules
            found = False
            for rule in self.replacementRule:
                # check to see if the character matches any replacement rule
                # if found, the new string abides by the replacement rule
                if char == rule[0]:
                    wordPick = random.choice(rule[1:])
                    newString += wordPick
                    found = True
                    break

            # if not found, the new string consists of the original character    
            if not found:
                newString += char
        
        return newString


    def buildString(self, n):
        '''Starting with the base string, apply the L-system replacement rules for `n` iterations.

        You should NOT change your base string instance variable here!

        Parameters:
        -----------
        n: int. Number of times you go through the L-system string to apply the replacement rules.

        Returns:
        -----------
        str: The L-system string after apply the replacement rules `n` times.
        '''
        # get the current basestring
        str = self.basestring

        # use the replacement method on the string 'n' many times
        for i in range(n):
            str = self.replace(str)

        return str