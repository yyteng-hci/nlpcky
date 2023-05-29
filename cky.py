"""
COMS W4705 - Natural Language Processing - Fall 2022
Homework 2 - Parsing with Probabilistic Context Free Grammars 
Instructor: Daniel Bauer
Student: Yuanyang Teng
"""
import math
import sys
from grammar import Pcfg

### Use the following two functions to check the format of your data structures in part 3 ###
def check_table_format(table):
    """
    Return true if the backpointer table object is formatted correctly.
    Otherwise return False and print an error.  
    """
    if not isinstance(table, dict): 
        sys.stderr.write("Backpointer table is not a dict.\n")
        return False
    for split in table: 
        if not isinstance(split, tuple) and len(split) ==2 and \
          isinstance(split[0], int)  and isinstance(split[1], int):
            sys.stderr.write("Keys of the backpointer table must be tuples (i,j) representing spans.\n")
            return False
        if not isinstance(table[split], dict):
            sys.stderr.write("Value of backpointer table (for each span) is not a dict.\n")
            return False
        for nt in table[split]:
            if not isinstance(nt, str): 
                sys.stderr.write("Keys of the inner dictionary (for each span) must be strings representing nonterminals.\n")
                return False
            bps = table[split][nt]
            if isinstance(bps, str): # Leaf nodes may be strings
                continue 
            if not isinstance(bps, tuple):
                sys.stderr.write("Values of the inner dictionary (for each span and nonterminal) must be a pair ((i,k,A),(k,j,B)) of backpointers. Incorrect type: {}\n".format(bps))
                return False
            if len(bps) != 2:
                sys.stderr.write("Values of the inner dictionary (for each span and nonterminal) must be a pair ((i,k,A),(k,j,B)) of backpointers. Found more than two backpointers: {}\n".format(bps))
                return False
            for bp in bps: 
                if not isinstance(bp, tuple) or len(bp)!=3:
                    sys.stderr.write("Values of the inner dictionary (for each span and nonterminal) must be a pair ((i,k,A),(k,j,B)) of backpointers. Backpointer has length != 3.\n".format(bp))
                    return False
                if not (isinstance(bp[0], str) and isinstance(bp[1], int) and isinstance(bp[2], int)):
                    print(bp)
                    sys.stderr.write("Values of the inner dictionary (for each span and nonterminal) must be a pair ((i,k,A),(k,j,B)) of backpointers. Backpointer has incorrect type.\n".format(bp))
                    return False
    return True

def check_probs_format(table):
    """
    Return true if the probability table object is formatted correctly.
    Otherwise return False and print an error.  
    """
    if not isinstance(table, dict): 
        sys.stderr.write("Probability table is not a dict.\n")
        return False
    for split in table: 
        if not isinstance(split, tuple) and len(split) ==2 and isinstance(split[0], int) and isinstance(split[1], int):
            sys.stderr.write("Keys of the probability must be tuples (i,j) representing spans.\n")
            return False
        if not isinstance(table[split], dict):
            sys.stderr.write("Value of probability table (for each span) is not a dict.\n")
            return False
        for nt in table[split]:
            if not isinstance(nt, str): 
                sys.stderr.write("Keys of the inner dictionary (for each span) must be strings representing nonterminals.\n")
                return False
            prob = table[split][nt]
            if not isinstance(prob, float):
                sys.stderr.write("Values of the inner dictionary (for each span and nonterminal) must be a float.{}\n".format(prob))
                return False
            if prob > 0:
                sys.stderr.write("Log probability may not be > 0.  {}\n".format(prob))
                return False
    return True



class CkyParser(object):
    """
    A CKY parser.
    """

    def __init__(self, grammar): 
        """
        Initialize a new parser instance from a grammar. 
        """
        self.grammar = grammar

    def is_in_language(self,tokens):
        """
        Membership checking. Parse the input tokens and return True if 
        the sentence is in the language described by the grammar. Otherwise
        return False
        """
        n = len(tokens)
        pt = {} #pt - parse table
        valid = False

        for i in range(n + 1):
            for j in range(i + 1, n + 1):
                pt[(i, j)] = {}

        for i in range(n):
            for key, value in self.grammar.rhs_to_rules.items():
                if tokens[i] == key[0]:
                    for v in value:
                        pt[(i, i + 1)][v[0]] = tokens[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length
                for k in range(i + 1, j):
                    for key, value in self.grammar.rhs_to_rules.items():
                        for B in pt[(i, k)]:
                            for C in pt[(k, j)]:
                                if key[0] == B and key[1] == C:
                                    for v in value:
                                        pt[(i, j)][v[0]] = ((key[0], i, k), (key[1], k, j))


        # return True if TOP is in span[0, len(tokens)]
        if self.grammar.startsymbol in pt[(0, n)]:
            valid = True

        return valid
       
    def parse_with_backpointers(self, tokens):
        """
        Parse the input tokens and return a parse table and a probability table.
        """
        table = {}
        probs = {}

        n = len(tokens)

        for i in range(n + 1):
            for j in range(i + 1, n + 1):
                table[(i, j)] = {}
                probs[(i, j)] = {}

        for i in range(n):
            for key, value in self.grammar.rhs_to_rules.items():
                if tokens[i] == key[0]:
                    for v in value:
                        table[(i, i + 1)][v[0]] = tokens[i]
                        probs[(i, i + 1)][v[0]] = math.log2(v[2])

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length
                for k in range(i + 1, j):
                    for key in self.grammar.rhs_to_rules.keys():
                        for B in table[(i, k)]:
                            for C in table[(k, j)]:
                                if key[0] == B and key[1] == C:
                                    values = self.grammar.rhs_to_rules[(B, C)]

                                    for v in values:
                                        nt = v[0]
                                        prob = v[2]

                                        if nt not in table[(i, j)]:
                                            table[(i, j)][nt] = ((key[0], i, k), (key[1], k, j))
                                            probs[(i, j)][nt] = math.log(prob) + probs[(i, k)][key[0]] + probs[(k, j)][key[1]]
                                        else:
                                            if probs[(i, j)][nt] < math.log(prob) + probs[(i, k)][key[0]] + probs[(k, j)][key[1]]:
                                                table[(i, j)][nt] = ((key[0], i, k), (key[1], k, j))
                                                probs[(i, j)][nt] = math.log(prob) + probs[(i, k)][key[0]] + probs[(k, j)][key[1]]



        return table, probs


def get_tree(chart, i,j,nt): 
    """
    Return the parse-tree rooted in non-terminal nt and covering span i,j.
    """
    v = chart[(i, j)][nt]

    tree = tuple()
    tree += (nt,)

    # v is a nonterminal token
    if type(v) == tuple:
        for i in range(len(v)):
            tree += (get_tree(chart, v[i][1], v[i][2], v[i][0]), )
    # v is terminal
    else:
        tree += (v, )

    return tree
 
       
if __name__ == "__main__":
    
    with open('atis3.pcfg','r') as grammar_file: 
        grammar = Pcfg(grammar_file) 
        parser = CkyParser(grammar)
        toks =['flights', 'from','miami', 'to', 'cleveland','.'] #True

        #Part 2 tests
        # toks = ['flights', 'to', 'miami', 'from', 'cleveland', '.'] #True
        # toks = ['flights', 'miami', 'cleveland', 'to', '.'] #False

        #print(parser.is_in_language(toks))
        # table,probs = parser.parse_with_backpointers(toks)
        # print(table)
        # print(probs)
        # print(check_table_format(table))
        # print(check_probs_format(probs))
        #
        # tree = get_tree(table, 0, len(toks), 'TOP')
        # print(tree)

