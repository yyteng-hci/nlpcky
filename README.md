# CKY Algorithm for CFG and PCFG parsing

The project implements the CKY algorithm for CFG and PCFG parsing. It includes the following parts:
- reading and verifying the grammar
- membership checking with CKY
- parsing with backpointers
- retrieving a parse tree
- evaluating the parser

## Usage
'''python
python evaluate_parser.py atis3.pcfg atis3_test.ptb
'''

## Output

## Data
Data is extracted from the ATIS (Air Travel Information Services) subsection of the Penn Treebank. ATIS is originally a spoken language corpus containing user queries about air travel. These queries have been transcribed into text and annotated with Penn Treebank phrase structure syntax. 

There are 2 data files:
- atis3.pcfg contains the PCFG grammar
- atis3_test.ptb contains the test corpus
