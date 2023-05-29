"""
COMS W4705 - Natural Language Processing - Fall 2022
Homework 2 - Parsing with Context Free Grammars 
Instructor: Daniel Bauer
Student: Yuanyang Teng
"""

import sys
from collections import defaultdict
import math

class Pcfg(object): 
    """
    Represent a probabilistic context free grammar. 
    """

    def __init__(self, grammar_file): 
        self.rhs_to_rules = defaultdict(list)
        self.lhs_to_rules = defaultdict(list)
        self.startsymbol = None 
        self.read_rules(grammar_file)      
 
    def read_rules(self, grammar_file):
        
        for line in grammar_file: 
            line = line.strip()
            if line and not line.startswith("#"):
                if "->" in line: 
                    rule = self.parse_rule(line.strip())
                    lhs, rhs, prob = rule
                    self.rhs_to_rules[rhs].append(rule)
                    self.lhs_to_rules[lhs].append(rule)
                else: 
                    startsymbol, prob = line.rsplit(";")
                    self.startsymbol = startsymbol.strip()
                    
     
    def parse_rule(self, rule_s):
        lhs, other = rule_s.split("->")
        lhs = lhs.strip()
        rhs_s, prob_s = other.rsplit(";",1) 
        prob = float(prob_s)
        rhs = tuple(rhs_s.strip().split())
        return (lhs, rhs, prob)

    def verify_grammar(self):
        """
        Return True if the grammar is a valid PCFG in CNF.
        Otherwise return False. 
        """
        nonterminals = list(self.lhs_to_rules.keys())

        valid = True

        for key, value in self.lhs_to_rules.items():

            probsum = 0

            #in keys, check the nonterminals are upper cases
            if key.isupper() == False:
                valid = False

            #in values, check if nonterminals are upper cases
            for tup in value:
                if tup[0].isupper() == False:
                    valid = False
                for i in tup[1]:
                    if i.isupper() == True:
                        if i not in nonterminals:
                            valid = False

                #check sum of prob for same key
                probsum += tup[2]

            if math.isclose(probsum, 1.0) == False:
                valid = False

        return valid


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as grammar_file:
        grammar = Pcfg(grammar_file)

    if grammar.verify_grammar() == True:
        print("The grammar is valid")
    else:
        print("Error: The grammar is not valid")

