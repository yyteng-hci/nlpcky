# CKY Algorithm for CFG and PCFG parsing

The project implements the CKY algorithm for CFG and PCFG parsing. It includes the following parts:
- reading and verifying the grammar
- membership checking with CKY
- parsing with backpointers
- retrieving a parse tree
- evaluating the parser

## Data
Data is extracted from the ATIS (Air Travel Information Services) subsection of the Penn Treebank. ATIS is originally a spoken language corpus containing user queries about air travel. These queries have been transcribed into text and annotated with Penn Treebank phrase structure syntax. 

There are 2 data files:
- atis3.pcfg contains the PCFG grammar
- atis3_test.ptb contains the test corpus

## Usage
```python
python evaluate_parser.py atis3.pcfg atis3_test.ptb
```

## Output
```python
input:  ['flights', 'from', 'los', 'angeles', 'to', 'pittsburgh', '.']
target:     ('TOP', ('NP', ('NP', 'flights'), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', ('LOS', 'los'), ('ANGELES', 'angeles'))), ('PP', ('TO', 'to'), ('NP', 'pittsburgh')))), ('PUN', '.'))
predicted:  ('TOP', ('NP', ('NP', 'flights'), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', ('LOS', 'los'), ('ANGELES', 'angeles'))), ('PP', ('TO', 'to'), ('NP', 'pittsburgh')))), ('PUN', '.'))
P:1.0 R:1.0 F:1.0

input:  ['with', 'the', 'least', 'expensive', 'fare', '.']
target:     ('TOP', ('PP', ('WITH', 'with'), ('NP', ('THE', 'the'), ('NPBAR', ('ADJP', ('LEAST', 'least'), ('EXPENSIVE', 'expensive')), ('FARE', 'fare')))), ('PUN', '.'))
predicted:  ()
P:0.0 R:0.0 F:0.0

input:  ['flights', 'between', 'tampa', 'and', 'saint', 'louis', '.']
target:     ('TOP', ('NP', ('NP', 'flights'), ('PP', ('BETWEEN', 'between'), ('NP', ('NP', 'tampa'), ('NPBAR', ('AND', 'and'), ('NP', ('SAINT', 'saint'), ('LOUIS', 'louis')))))), ('PUN', '.'))
predicted:  ('TOP', ('NP', ('NP', 'flights'), ('NPBAR', ('PP', ('BETWEEN', 'between'), ('NP', 'tampa')), ('NPBAR', ('AND', 'and'), ('NP', ('SAINT', 'saint'), ('LOUIS', 'louis'))))), ('PUN', '.'))
P:0.8461538461538461 R:0.8461538461538461 F:0.8461538461538461

input:  ['i', "'d", 'like', 'a', 'flight', 'tomorrow', 'from', 'columbus', 'to', 'houston', 'with', 'a', 'stopover', 'in', 'nashville', '.']
target:     ('TOP', ('S', ('NP', 'i'), ('VP', ("'D", "'d"), ('VP', ('LIKE', 'like'), ('NP', ('NP', ('A', 'a'), ('FLIGHT', 'flight')), ('NPBAR', ('NP', 'tomorrow'), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'columbus')), ('NPBAR', ('PP', ('TO', 'to'), ('NP', 'houston')), ('PP', ('WITH', 'with'), ('NP', ('NP', ('A', 'a'), ('STOPOVER', 'stopover')), ('PP', ('IN', 'in'), ('NP', 'nashville'))))))))))), ('PUN', '.'))
predicted:  ()
P:0.0 R:0.0 F:0.0

input:  ['display', 'the', 'fare', 'codes', '.']
target:     ('TOP', ('VP', ('DISPLAY', 'display'), ('NP', ('THE', 'the'), ('NPBAR', ('FARE', 'fare'), ('CODES', 'codes')))), ('PUN', '.'))
predicted:  ()
P:0.0 R:0.0 F:0.0

input:  ['what', 'flights', 'from', 'kansas', 'city', 'to', 'denver', '.']
target:     ('TOP', ('WHNP', ('WHNP', ('WHAT', 'what'), ('FLIGHTS', 'flights')), ('WHNPBAR', ('PP', ('FROM', 'from'), ('NP', ('KANSAS', 'kansas'), ('CITY', 'city'))), ('PP', ('TO', 'to'), ('NP', 'denver')))), ('PUN', '.'))
predicted:  ('TOP', ('WHNP', ('WHNP', ('WHAT', 'what'), ('FLIGHTS', 'flights')), ('WHNPBAR', ('PP', ('FROM', 'from'), ('NP', ('KANSAS', 'kansas'), ('CITY', 'city'))), ('PP', ('TO', 'to'), ('NP', 'denver')))), ('PUN', '.'))
P:1.0 R:1.0 F:1.0

input:  ['what', 'flights', 'from', 'minneapolis', 'to', 'pittsburgh', '.']
target:     ('TOP', ('WHNP', ('WHNP', ('WHAT', 'what'), ('FLIGHTS', 'flights')), ('WHNPBAR', ('PP', ('FROM', 'from'), ('NP', 'minneapolis')), ('PP', ('TO', 'to'), ('NP', 'pittsburgh')))), ('PUN', '.'))
predicted:  ('TOP', ('WHNP', ('WHNP', ('WHAT', 'what'), ('FLIGHTS', 'flights')), ('WHNPBAR', ('PP', ('FROM', 'from'), ('NP', 'minneapolis')), ('PP', ('TO', 'to'), ('NP', 'pittsburgh')))), ('PUN', '.'))
P:1.0 R:1.0 F:1.0

input:  ['what', 'flights', 'from', 'tampa', 'to', 'cincinnati', '.']
target:     ('TOP', ('WHNP', ('WHNP', ('WHAT', 'what'), ('FLIGHTS', 'flights')), ('WHNPBAR', ('PP', ('FROM', 'from'), ('NP', 'tampa')), ('PP', ('TO', 'to'), ('NP', 'cincinnati')))), ('PUN', '.'))
predicted:  ('TOP', ('WHNP', ('WHNP', ('WHAT', 'what'), ('FLIGHTS', 'flights')), ('WHNPBAR', ('PP', ('FROM', 'from'), ('NP', 'tampa')), ('PP', ('TO', 'to'), ('NP', 'cincinnati')))), ('PUN', '.'))
P:1.0 R:1.0 F:1.0

input:  ['which', 'of', 'these', 'leave', 'after', 'noon', 'and', 'stop', 'in', 'phoenix', '.']
target:     ('TOP', ('SBARQ', ('WHNP', ('WHNP', 'which'), ('PP', ('OF', 'of'), ('NP', 'these'))), ('VP', ('VP', ('LEAVE', 'leave'), ('PP', ('AFTER', 'after'), ('NP', 'noon'))), ('VPBAR', ('AND', 'and'), ('VP', ('STOP', 'stop'), ('PP', ('IN', 'in'), ('NP', 'phoenix')))))), ('PUN', '.'))
predicted:  ('TOP', ('SBARQ', ('WHNP', ('WHNP', 'which'), ('PP', ('OF', 'of'), ('NP', 'these'))), ('VP', ('LEAVE', 'leave'), ('VPBAR', ('PP', ('AFTER', 'after'), ('NP', 'noon')), ('VPBAR', ('AND', 'and'), ('VP', ('STOP', 'stop'), ('PP', ('IN', 'in'), ('NP', 'phoenix'))))))), ('PUN', '.'))
P:0.9523809523809523 R:0.9523809523809523 F:0.9523809523809523

input:  ['flights', 'from', 'boston', 'to', 'pittsburgh', '.']
target:     ('TOP', ('NP', ('NP', 'flights'), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'boston')), ('PP', ('TO', 'to'), ('NP', 'pittsburgh')))), ('PUN', '.'))
predicted:  ('TOP', ('NP', ('NP', 'flights'), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'boston')), ('PP', ('TO', 'to'), ('NP', 'pittsburgh')))), ('PUN', '.'))
P:1.0 R:1.0 F:1.0

input:  ['i', 'prefer', 'a', 'morning', 'flight', '.']
target:     ('TOP', ('S', ('NP', 'i'), ('VP', ('PREFER', 'prefer'), ('NP', ('A', 'a'), ('NPBAR', ('MORNING', 'morning'), ('FLIGHT', 'flight'))))), ('PUN', '.'))
predicted:  ()
P:0.0 R:0.0 F:0.0

input:  ['show', 'me', 'the', 'first', 'flight', 'that', 'arrives', 'in', 'toronto', 'from', 'cincinnati', '.']
target:     ('TOP', ('VP', ('SHOW', 'show'), ('VPBAR', ('NP', 'me'), ('NP', ('NP', ('THE', 'the'), ('NPBAR', ('FIRST', 'first'), ('FLIGHT', 'flight'))), ('NPBAR', ('SBAR', ('WHNP', 'that'), ('VP', ('ARRIVES', 'arrives'), ('PP', ('IN', 'in'), ('NP', 'toronto')))), ('PP', ('FROM', 'from'), ('NP', 'cincinnati')))))), ('PUN', '.'))
predicted:  ('TOP', ('VP', ('SHOW', 'show'), ('VPBAR', ('NP', 'me'), ('NP', ('THE', 'the'), ('NPBAR', ('ADVP', 'first'), ('NP', ('NP', 'flight'), ('SBAR', ('WHNP', 'that'), ('VP', ('ARRIVES', 'arrives'), ('VPBAR', ('PP', ('IN', 'in'), ('NP', 'toronto')), ('PP', ('FROM', 'from'), ('NP', 'cincinnati')))))))))), ('PUN', '.'))
P:0.6956521739130435 R:0.6956521739130435 F:0.6956521739130435

input:  ['which', 'of', 'these', 'is', 'last', '.']
target:     ('TOP', ('SBARQ', ('WHNP', ('WHNP', 'which'), ('PP', ('OF', 'of'), ('NP', 'these'))), ('VP', ('IS', 'is'), ('ADJP', 'last'))), ('PUN', '.'))
predicted:  ('TOP', ('SBARQ', ('WHNP', ('WHNP', 'which'), ('PP', ('OF', 'of'), ('NP', 'these'))), ('VP', ('IS', 'is'), ('ADJP', 'last'))), ('PUN', '.'))
P:1.0 R:1.0 F:1.0

input:  ['i', "'d", 'like', 'a', 'flight', 'tomorrow', 'from', 'san', 'diego', 'to', 'toronto', '.']
target:     ('TOP', ('S', ('NP', 'i'), ('VP', ("'D", "'d"), ('VP', ('LIKE', 'like'), ('NP', ('NP', ('A', 'a'), ('FLIGHT', 'flight')), ('NPBAR', ('NP', 'tomorrow'), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', ('SAN', 'san'), ('DIEGO', 'diego'))), ('PP', ('TO', 'to'), ('NP', 'toronto')))))))), ('PUN', '.'))
predicted:  ('TOP', ('S', ('NP', 'i'), ('VP', ("'D", "'d"), ('VP', ('LIKE', 'like'), ('NP', ('NP', ('A', 'a'), ('FLIGHT', 'flight')), ('NP', ('NP', 'tomorrow'), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', ('SAN', 'san'), ('DIEGO', 'diego'))), ('PP', ('TO', 'to'), ('NP', 'toronto')))))))), ('PUN', '.'))
P:0.9565217391304348 R:0.9565217391304348 F:0.9565217391304348

input:  ['which', 'of', 'those', 'leave', 'before', 'eight', 'a.m', '.']
target:     ('TOP', ('SBARQ', ('WHNP', ('WHNP', 'which'), ('PP', ('OF', 'of'), ('NP', 'those'))), ('VP', ('LEAVE', 'leave'), ('PP', ('BEFORE', 'before'), ('NP', ('EIGHT', 'eight'), ('A.M', 'a.m'))))), ('PUN', '.'))
predicted:  ()
P:0.0 R:0.0 F:0.0

input:  ['what', 'airlines', 'from', 'washington', 'd', 'c', 'to', 'columbus', '.']
target:     ('TOP', ('FRAG', ('WHNP', ('WHAT', 'what'), ('AIRLINES', 'airlines')), ('FRAGBAR', ('PP', ('FROM', 'from'), ('NP', ('NP', 'washington'), ('NP', ('D', 'd'), ('C', 'c')))), ('PP', ('TO', 'to'), ('NP', 'columbus')))), ('PUN', '.'))
predicted:  ('TOP', ('WHNP', ('WHNP', ('WHAT', 'what'), ('AIRLINES', 'airlines')), ('WHNPBAR', ('PP', ('FROM', 'from'), ('NP', ('NP', 'washington'), ('NP', ('D', 'd'), ('C', 'c')))), ('PP', ('TO', 'to'), ('NP', 'columbus')))), ('PUN', '.'))
P:0.8823529411764706 R:0.8823529411764706 F:0.8823529411764706

input:  ['what', 'flights', 'from', 'chicago', 'to', 'kansas', 'city', 'in', 'the', 'morning', '.']
target:     ('TOP', ('WHNP', ('NP', ('WHAT', 'what'), ('FLIGHTS', 'flights')), ('WHNPBAR', ('PP', ('FROM', 'from'), ('NP', 'chicago')), ('WHNPBAR', ('PP', ('TO', 'to'), ('NP', ('KANSAS', 'kansas'), ('CITY', 'city'))), ('PP', ('IN', 'in'), ('NP', ('THE', 'the'), ('MORNING', 'morning')))))), ('PUN', '.'))
predicted:  ('TOP', ('WHNP', ('WHNP', ('WHAT', 'what'), ('FLIGHTS', 'flights')), ('WHNPBAR', ('PP', ('FROM', 'from'), ('NP', 'chicago')), ('WHNPBAR', ('PP', ('TO', 'to'), ('NP', ('KANSAS', 'kansas'), ('CITY', 'city'))), ('PP', ('IN', 'in'), ('NP', ('THE', 'the'), ('MORNING', 'morning')))))), ('PUN', '.'))
P:0.9523809523809523 R:0.9523809523809523 F:0.9523809523809523

input:  ['what', 'type', 'of', 'aircraft', 'is', 'used', 'on', 'those', 'flights', '.']
target:     ('TOP', ('SBARQ', ('WHNP', ('WHNP', ('WHAT', 'what'), ('TYPE', 'type')), ('PP', ('OF', 'of'), ('NP', 'aircraft'))), ('VP', ('IS', 'is'), ('VP', ('USED', 'used'), ('PP', ('ON', 'on'), ('NP', ('THOSE', 'those'), ('FLIGHTS', 'flights')))))), ('PUN', '.'))
predicted:  ()
P:0.0 R:0.0 F:0.0

input:  ['price', 'of', 'flight', 'a', 'a', 'one', 'thousand', 'three', 'hundred', 'nineteen', '.']
target:     ('TOP', ('NP', ('NP', 'price'), ('PP', ('OF', 'of'), ('NP', ('FLIGHT', 'flight'), ('NPBAR', ('A', 'a'), ('NPBAR', ('A', 'a'), ('NPBAR', ('ONE', 'one'), ('NPBAR', ('THOUSAND', 'thousand'), ('NPBAR', ('THREE', 'three'), ('NPBAR', ('HUNDRED', 'hundred'), ('NINETEEN', 'nineteen')))))))))), ('PUN', '.'))
predicted:  ()
P:0.0 R:0.0 F:0.0

input:  ['show', 'me', 'the', 'ground', 'transportation', 'available', '.']
target:     ('TOP', ('VP', ('SHOW', 'show'), ('VPBAR', ('NP', 'me'), ('NP', ('NP', ('THE', 'the'), ('NPBAR', ('GROUND', 'ground'), ('TRANSPORTATION', 'transportation'))), ('ADJP', 'available')))), ('PUN', '.'))
predicted:  ()
P:0.0 R:0.0 F:0.0

input:  ['which', 'is', 'the', 'latest', '.']
target:     ('TOP', ('SBARQ', ('WHNP', 'which'), ('VP', ('IS', 'is'), ('NP', ('THE', 'the'), ('LATEST', 'latest')))), ('PUN', '.'))
predicted:  ()
P:0.0 R:0.0 F:0.0

input:  ['what', 'about', 'after', 'seven', 'p.m', '.']
target:     ('TOP', ('FRAG', ('X', ('WHAT', 'what'), ('ABOUT', 'about')), ('PP', ('AFTER', 'after'), ('NP', ('SEVEN', 'seven'), ('P.M', 'p.m')))), ('PUN', '.'))
predicted:  ('TOP', ('FRAG', ('X', ('WHAT', 'what'), ('ABOUT', 'about')), ('PP', ('AFTER', 'after'), ('NP', ('SEVEN', 'seven'), ('P.M', 'p.m')))), ('PUN', '.'))
P:1.0 R:1.0 F:1.0

input:  ['what', 'flights', 'from', 'salt', 'lake', 'city', 'to', 'las', 'vegas', '.']
target:     ('TOP', ('FRAG', ('WHNP', ('WHNP', ('WHAT', 'what'), ('FLIGHTS', 'flights')), ('PP', ('FROM', 'from'), ('NP', ('SALT', 'salt'), ('NPBAR', ('LAKE', 'lake'), ('CITY', 'city'))))), ('PP', ('TO', 'to'), ('NP', ('LAS', 'las'), ('VEGAS', 'vegas')))), ('PUN', '.'))
predicted:  ('TOP', ('WHNP', ('WHNP', ('WHAT', 'what'), ('FLIGHTS', 'flights')), ('WHNPBAR', ('PP', ('FROM', 'from'), ('NP', ('SALT', 'salt'), ('NPBAR', ('LAKE', 'lake'), ('CITY', 'city')))), ('PP', ('TO', 'to'), ('NP', ('LAS', 'las'), ('VEGAS', 'vegas'))))), ('PUN', '.'))
P:0.8947368421052632 R:0.8947368421052632 F:0.8947368421052632

input:  ['flights', 'after', 'twelve', 'hundred', 'hours', '.']
target:     ('TOP', ('NP', ('NP', 'flights'), ('PP', ('AFTER', 'after'), ('NP', ('TWELVE', 'twelve'), ('NPBAR', ('HUNDRED', 'hundred'), ('HOURS', 'hours'))))), ('PUN', '.'))
predicted:  ('TOP', ('FRAG', ('NP', 'flights'), ('PP', ('AFTER', 'after'), ('NP', ('TWELVE', 'twelve'), ('NPBAR', ('HUNDRED', 'hundred'), ('HOURS', 'hours'))))), ('PUN', '.'))
P:0.9090909090909091 R:0.9090909090909091 F:0.9090909090909091

input:  ['what', 'is', 'the', 'price', 'of', 'united', 'airlines', 'flight', 'nine', 'seven', '.']
target:     ('TOP', ('SBARQ', ('WHNP', 'what'), ('SQ', ('IS', 'is'), ('NP', ('NP', ('THE', 'the'), ('PRICE', 'price')), ('PP', ('OF', 'of'), ('NP', ('UNITED', 'united'), ('NPBAR', ('AIRLINES', 'airlines'), ('NPBAR', ('FLIGHT', 'flight'), ('NPBAR', ('NINE', 'nine'), ('SEVEN', 'seven'))))))))), ('PUN', '.'))
predicted:  ('TOP', ('SBARQ', ('WHNP', 'what'), ('SQ', ('IS', 'is'), ('NP', ('NP', ('THE', 'the'), ('PRICE', 'price')), ('NPBAR', ('PP', ('OF', 'of'), ('NP', ('UNITED', 'united'), ('AIRLINES', 'airlines'))), ('NPBAR', ('FLIGHT', 'flight'), ('NPBAR', ('NINE', 'nine'), ('SEVEN', 'seven'))))))), ('PUN', '.'))
P:0.8571428571428571 R:0.8571428571428571 F:0.8571428571428571

input:  ['cheapest', 'airfare', 'from', 'orlando', 'to', 'tacoma', '.']
target:     ('TOP', ('NP', ('NP', ('CHEAPEST', 'cheapest'), ('AIRFARE', 'airfare')), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'orlando')), ('PP', ('TO', 'to'), ('NP', 'tacoma')))), ('PUN', '.'))
predicted:  ('TOP', ('NP', ('NP', ('CHEAPEST', 'cheapest'), ('AIRFARE', 'airfare')), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'orlando')), ('PP', ('TO', 'to'), ('NP', 'tacoma')))), ('PUN', '.'))
P:1.0 R:1.0 F:1.0

input:  ['price', 'of', 'flight', 'from', 'cleveland', 'to', 'nashville', '.']
target:     ('TOP', ('NP', ('NP', 'price'), ('PP', ('OF', 'of'), ('NP', ('NP', 'flight'), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'cleveland')), ('PP', ('TO', 'to'), ('NP', 'nashville')))))), ('PUN', '.'))
predicted:  ('TOP', ('FRAG', ('NP', 'price'), ('PP', ('OF', 'of'), ('NP', ('FLIGHT', 'flight'), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'cleveland')), ('PP', ('TO', 'to'), ('NP', 'nashville')))))), ('PUN', '.'))
P:0.8666666666666667 R:0.8666666666666667 F:0.8666666666666667

input:  ['what', 'is', 'the', 'price', '.']
target:     ('TOP', ('SBARQ', ('WHNP', 'what'), ('SQ', ('IS', 'is'), ('NP', ('THE', 'the'), ('PRICE', 'price')))), ('PUN', '.'))
predicted:  ('TOP', ('SBARQ', ('WHNP', 'what'), ('SQ', ('IS', 'is'), ('NP', ('THE', 'the'), ('PRICE', 'price')))), ('PUN', '.'))
P:1.0 R:1.0 F:1.0

input:  ['what', 'is', 'the', 'price', 'of', 'flights', 'from', 'indianapolis', 'to', 'memphis', '.']
target:     ('TOP', ('SBARQ', ('WHNP', 'what'), ('SQ', ('IS', 'is'), ('NP', ('NP', ('THE', 'the'), ('PRICE', 'price')), ('PP', ('OF', 'of'), ('NP', ('NP', 'flights'), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'indianapolis')), ('PP', ('TO', 'to'), ('NP', 'memphis')))))))), ('PUN', '.'))
predicted:  ('TOP', ('SBARQ', ('WHNP', 'what'), ('SQ', ('IS', 'is'), ('NP', ('NP', ('THE', 'the'), ('PRICE', 'price')), ('NPBAR', ('PP', ('OF', 'of'), ('NP', 'flights')), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'indianapolis')), ('PP', ('TO', 'to'), ('NP', 'memphis'))))))), ('PUN', '.'))
P:0.9047619047619048 R:0.9047619047619048 F:0.9047619047619048

input:  ['show', 'me', 'the', 'flights', 'from', 'newark', 'new', 'jersey', 'to', 'ontario', 'international', 'next', 'saturday', '.']
target:     ('TOP', ('VP', ('SHOW', 'show'), ('VPBAR', ('NP', 'me'), ('NP', ('NP', ('THE', 'the'), ('FLIGHTS', 'flights')), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', ('NP', 'newark'), ('NP', ('NEW', 'new'), ('JERSEY', 'jersey')))), ('NPBAR', ('PP', ('TO', 'to'), ('NP', ('ONTARIO', 'ontario'), ('INTERNATIONAL', 'international'))), ('NP', ('NEXT', 'next'), ('SATURDAY', 'saturday'))))))), ('PUN', '.'))
predicted:  ()
P:0.0 R:0.0 F:0.0

input:  ['what', 'flights', 'leave', 'phoenix', 'on', 'wednesday', '.']
target:     ('TOP', ('SBARQ', ('WHNP', ('WHAT', 'what'), ('FLIGHTS', 'flights')), ('VP', ('LEAVE', 'leave'), ('VPBAR', ('NP', 'phoenix'), ('PP', ('ON', 'on'), ('NP', 'wednesday'))))), ('PUN', '.'))
predicted:  ('TOP', ('SBARQ', ('WHNP', ('WHAT', 'what'), ('FLIGHTS', 'flights')), ('VP', ('LEAVE', 'leave'), ('VPBAR', ('NP', 'phoenix'), ('PP', ('ON', 'on'), ('NP', 'wednesday'))))), ('PUN', '.'))
P:1.0 R:1.0 F:1.0

input:  ['show', 'me', 'the', 'meal', '.']
target:     ('TOP', ('VP', ('SHOW', 'show'), ('VPBAR', ('NP', 'me'), ('NP', ('THE', 'the'), ('MEAL', 'meal')))), ('PUN', '.'))
predicted:  ()
P:0.0 R:0.0 F:0.0

input:  ['show', 'business', 'class', 'fares', '.']
target:     ('TOP', ('VP', ('SHOW', 'show'), ('NP', ('BUSINESS', 'business'), ('NPBAR', ('CLASS', 'class'), ('FARES', 'fares')))), ('PUN', '.'))
predicted:  ('TOP', ('VP', ('SHOW', 'show'), ('NP', ('BUSINESS', 'business'), ('NPBAR', ('CLASS', 'class'), ('FARES', 'fares')))), ('PUN', '.'))
P:1.0 R:1.0 F:1.0

input:  ['i', 'have', 'a', 'friend', 'living', 'in', 'denver', 'that', 'would', 'like', 'to', 'visit', 'me', 'here', 'in', 'washington', 'd', 'c', '.']
target:     ('TOP', ('S', ('NP', 'i'), ('VP', ('HAVE', 'have'), ('NP', ('NP', ('A', 'a'), ('FRIEND', 'friend')), ('NPBAR', ('VP', ('LIVING', 'living'), ('PP', ('IN', 'in'), ('NP', 'denver'))), ('SBAR', ('WHNP', 'that'), ('VP', ('WOULD', 'would'), ('VP', ('LIKE', 'like'), ('VP', ('TO', 'to'), ('VP', ('VISIT', 'visit'), ('VPBAR', ('NP', 'me'), ('ADVP', ('ADVP', 'here'), ('PP', ('IN', 'in'), ('NP', ('NP', 'washington'), ('NP', ('D', 'd'), ('C', 'c'))))))))))))))), ('PUN', '.'))
predicted:  ()
P:0.0 R:0.0 F:0.0

input:  ['cheapest', '.']
target:     ('TOP', ('ADJP', 'cheapest'), ('PUN', '.'))
predicted:  ()
P:0.0 R:0.0 F:0.0

input:  ['list', 'nonstop', 'flights', 'from', 'burbank', 'to', 'denver', 'arriving', 'by', 'six', 'p.m', '.']
target:     ('TOP', ('VP', ('LIST', 'list'), ('NP', ('NP', ('NONSTOP', 'nonstop'), ('FLIGHTS', 'flights')), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'burbank')), ('NPBAR', ('PP', ('TO', 'to'), ('NP', 'denver')), ('VP', ('ARRIVING', 'arriving'), ('PP', ('BY', 'by'), ('NP', ('SIX', 'six'), ('P.M', 'p.m')))))))), ('PUN', '.'))
predicted:  ('TOP', ('VP', ('LIST', 'list'), ('NP', ('NP', ('NONSTOP', 'nonstop'), ('FLIGHTS', 'flights')), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'burbank')), ('NPBAR', ('PP', ('TO', 'to'), ('NP', 'denver')), ('VP', ('ARRIVING', 'arriving'), ('PP', ('BY', 'by'), ('NP', ('SIX', 'six'), ('P.M', 'p.m')))))))), ('PUN', '.'))
P:1.0 R:1.0 F:1.0

input:  ['shortest', 'morning', 'flights', 'from', 'cincinnati', 'to', 'tampa', '.']
target:     ('TOP', ('NP', ('NP', ('SHORTEST', 'shortest'), ('NPBAR', ('MORNING', 'morning'), ('FLIGHTS', 'flights'))), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'cincinnati')), ('PP', ('TO', 'to'), ('NP', 'tampa')))), ('PUN', '.'))
predicted:  ('TOP', ('NP', ('NP', ('SHORTEST', 'shortest'), ('NPBAR', ('MORNING', 'morning'), ('FLIGHTS', 'flights'))), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'cincinnati')), ('PP', ('TO', 'to'), ('NP', 'tampa')))), ('PUN', '.'))
P:1.0 R:1.0 F:1.0

input:  ['flights', 'from', 'kansas', 'city', 'to', 'cleveland', '.']
target:     ('TOP', ('NP', ('NP', 'flights'), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', ('KANSAS', 'kansas'), ('CITY', 'city'))), ('PP', ('TO', 'to'), ('NP', 'cleveland')))), ('PUN', '.'))
predicted:  ('TOP', ('NP', ('NP', 'flights'), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', ('KANSAS', 'kansas'), ('CITY', 'city'))), ('PP', ('TO', 'to'), ('NP', 'cleveland')))), ('PUN', '.'))
P:1.0 R:1.0 F:1.0

input:  ['from', 'toronto', 'to', 'atlanta', 'in', 'the', 'afternoon', '.']
target:     ('TOP', ('FRAG', ('PP', ('FROM', 'from'), ('NP', 'toronto')), ('FRAGBAR', ('PP', ('TO', 'to'), ('NP', 'atlanta')), ('PP', ('IN', 'in'), ('NP', ('THE', 'the'), ('AFTERNOON', 'afternoon'))))), ('PUN', '.'))
predicted:  ('TOP', ('FRAG', ('PP', ('FROM', 'from'), ('NP', 'toronto')), ('FRAGBAR', ('PP', ('TO', 'to'), ('NP', 'atlanta')), ('PP', ('IN', 'in'), ('NP', ('THE', 'the'), ('AFTERNOON', 'afternoon'))))), ('PUN', '.'))
P:1.0 R:1.0 F:1.0

input:  ['now', 'i', 'need', 'a', 'flight', 'on', 'tuesday', 'from', 'phoenix', 'to', 'detroit', '.']
target:     ('TOP', ('S', ('ADVP', 'now'), ('SBAR', ('NP', 'i'), ('VP', ('NEED', 'need'), ('NP', ('NP', ('A', 'a'), ('FLIGHT', 'flight')), ('NPBAR', ('PP', ('ON', 'on'), ('NP', 'tuesday')), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'phoenix')), ('PP', ('TO', 'to'), ('NP', 'detroit')))))))), ('PUN', '.'))
predicted:  ('TOP', ('S', ('ADVP', 'now'), ('SBAR', ('NP', 'i'), ('VP', ('NEED', 'need'), ('NP', ('NP', ('A', 'a'), ('FLIGHT', 'flight')), ('NPBAR', ('PP', ('ON', 'on'), ('NP', 'tuesday')), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'phoenix')), ('PP', ('TO', 'to'), ('NP', 'detroit')))))))), ('PUN', '.'))
P:1.0 R:1.0 F:1.0

input:  ['i', 'need', 'a', 'flight', 'the', 'next', 'day', 'from', 'newark', 'to', 'orlando', '.']
target:     ('TOP', ('S', ('NP', 'i'), ('VP', ('NEED', 'need'), ('NP', ('NP', ('A', 'a'), ('FLIGHT', 'flight')), ('NPBAR', ('NP', ('THE', 'the'), ('NPBAR', ('NEXT', 'next'), ('DAY', 'day'))), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'newark')), ('PP', ('TO', 'to'), ('NP', 'orlando'))))))), ('PUN', '.'))
predicted:  ('TOP', ('S', ('NP', 'i'), ('VP', ('NEED', 'need'), ('NP', ('NP', ('A', 'a'), ('FLIGHT', 'flight')), ('NP', ('NP', ('THE', 'the'), ('NPBAR', ('NEXT', 'next'), ('DAY', 'day'))), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'newark')), ('PP', ('TO', 'to'), ('NP', 'orlando'))))))), ('PUN', '.'))
P:0.9565217391304348 R:0.9565217391304348 F:0.9565217391304348

input:  ['flights', 'from', 'pittsburgh', 'to', 'newark', '.']
target:     ('TOP', ('NP', ('NP', 'flights'), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'pittsburgh')), ('PP', ('TO', 'to'), ('NP', 'newark')))), ('PUN', '.'))
predicted:  ('TOP', ('NP', ('NP', 'flights'), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'pittsburgh')), ('PP', ('TO', 'to'), ('NP', 'newark')))), ('PUN', '.'))
P:1.0 R:1.0 F:1.0

input:  ['what', 'is', 'airline', 'f', 'f', '.']
target:     ('TOP', ('SBARQ', ('WHNP', 'what'), ('SQ', ('IS', 'is'), ('NP', ('AIRLINE', 'airline'), ('NPBAR', ('F', 'f'), ('F', 'f'))))), ('PUN', '.'))
predicted:  ()
P:0.0 R:0.0 F:0.0

input:  ['julysixteenth', 'please', '.']
target:     ('TOP', ('FRAG', ('NP', 'julysixteenth'), ('INTJ', 'please')), ('PUN', '.'))
predicted:  ()
P:0.0 R:0.0 F:0.0

input:  ['airports', 'in', 'new', 'york', '.']
target:     ('TOP', ('NP', ('NP', 'airports'), ('PP', ('IN', 'in'), ('NP', ('NEW', 'new'), ('YORK', 'york')))), ('PUN', '.'))
predicted:  ('TOP', ('FRAG', ('NP', 'airports'), ('PP', ('IN', 'in'), ('NP', ('NEW', 'new'), ('YORK', 'york')))), ('PUN', '.'))
P:0.8888888888888888 R:0.8888888888888888 F:0.8888888888888888

input:  ['show', 'me', 'the', 'flights', 'from', 'baltimore', 'to', 'seattle', '.']
target:     ('TOP', ('VP', ('SHOW', 'show'), ('VPBAR', ('NP', 'me'), ('NP', ('NP', ('THE', 'the'), ('FLIGHTS', 'flights')), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'baltimore')), ('PP', ('TO', 'to'), ('NP', 'seattle')))))), ('PUN', '.'))
predicted:  ('TOP', ('VP', ('SHOW', 'show'), ('VPBAR', ('NP', 'me'), ('NP', ('NP', ('THE', 'the'), ('FLIGHTS', 'flights')), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'baltimore')), ('PP', ('TO', 'to'), ('NP', 'seattle')))))), ('PUN', '.'))
P:1.0 R:1.0 F:1.0

input:  ['friday', 'afternoon', '.']
target:     ('TOP', ('NP', ('FRIDAY', 'friday'), ('AFTERNOON', 'afternoon')), ('PUN', '.'))
predicted:  ('TOP', ('NP', ('FRIDAY', 'friday'), ('AFTERNOON', 'afternoon')), ('PUN', '.'))
P:1.0 R:1.0 F:1.0

input:  ['how', 'many', 'stops', 'are', 'there', '.']
target:     ('TOP', ('SBAR', ('WHNP', ('WHADJP', ('HOW', 'how'), ('MANY', 'many')), ('STOPS', 'stops')), ('SQ', ('ARE', 'are'), ('NP', 'there'))), ('PUN', '.'))
predicted:  ()
P:0.0 R:0.0 F:0.0

input:  ['flights', 'from', 'pittsburgh', 'to', 'los', 'angeles', 'thursday', 'evening', '.']
target:     ('TOP', ('NP', ('NP', 'flights'), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'pittsburgh')), ('NPBAR', ('PP', ('TO', 'to'), ('NP', ('LOS', 'los'), ('ANGELES', 'angeles'))), ('NP', ('THURSDAY', 'thursday'), ('EVENING', 'evening'))))), ('PUN', '.'))
predicted:  ('TOP', ('FRAG', ('NP', 'flights'), ('FRAGBAR', ('PP', ('FROM', 'from'), ('NP', 'pittsburgh')), ('FRAGBAR', ('PP', ('TO', 'to'), ('NP', ('LOS', 'los'), ('ANGELES', 'angeles'))), ('NP', ('THURSDAY', 'thursday'), ('EVENING', 'evening'))))), ('PUN', '.'))
P:0.8235294117647058 R:0.8235294117647058 F:0.8235294117647058

input:  ['show', 'me', 'thelatestflight', 'from', 'salt', 'lake', 'city', 'to', 'phoenix', '.']
target:     ('TOP', ('VP', ('SHOW', 'show'), ('VPBAR', ('NP', 'me'), ('NP', ('NP', 'thelatestflight'), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', ('SALT', 'salt'), ('NPBAR', ('LAKE', 'lake'), ('CITY', 'city')))), ('PP', ('TO', 'to'), ('NP', 'phoenix')))))), ('PUN', '.'))
predicted:  ('TOP', ('VP', ('SHOW', 'show'), ('VPBAR', ('NP', 'me'), ('NP', ('NP', 'thelatestflight'), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', ('SALT', 'salt'), ('NPBAR', ('LAKE', 'lake'), ('CITY', 'city')))), ('PP', ('TO', 'to'), ('NP', 'phoenix')))))), ('PUN', '.'))
P:1.0 R:1.0 F:1.0

input:  ['of', 'those', 'flights', 'which', 'ones', 'stop', 'in', 'minneapolis', '.']
target:     ('TOP', ('SBARQ', ('PP', ('OF', 'of'), ('NP', ('THOSE', 'those'), ('FLIGHTS', 'flights'))), ('SBARQBAR', ('WHNP', ('WHICH', 'which'), ('ONES', 'ones')), ('VP', ('STOP', 'stop'), ('PP', ('IN', 'in'), ('NP', 'minneapolis'))))), ('PUN', '.'))
predicted:  ('TOP', ('S', ('PP', ('OF', 'of'), ('NP', ('NP', 'those'), ('FLIGHTS', 'flights'))), ('SBAR', ('WHNP', ('WHICH', 'which'), ('ONES', 'ones')), ('VP', ('STOP', 'stop'), ('PP', ('IN', 'in'), ('NP', 'minneapolis'))))), ('PUN', '.'))
P:0.8235294117647058 R:0.8235294117647058 F:0.8235294117647058

input:  ['tuesday', '.']
target:     ('TOP', ('NP', 'tuesday'), ('PUN', '.'))
predicted:  ('TOP', ('NP', 'tuesday'), ('PUN', '.'))
P:1.0 R:1.0 F:1.0

input:  ['flights', 'from', 'miami', 'to', 'cleveland', '.']
target:     ('TOP', ('NP', ('NP', 'flights'), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'miami')), ('PP', ('TO', 'to'), ('NP', 'cleveland')))), ('PUN', '.'))
predicted:  ('TOP', ('NP', ('NP', 'flights'), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', 'miami')), ('PP', ('TO', 'to'), ('NP', 'cleveland')))), ('PUN', '.'))
P:1.0 R:1.0 F:1.0

input:  ['what', 'is', 'b', 'n', 'a', '.']
target:     ('TOP', ('SBARQ', ('WHNP', 'what'), ('SQ', ('IS', 'is'), ('NP', ('B', 'b'), ('NPBAR', ('N', 'n'), ('A', 'a'))))), ('PUN', '.'))
predicted:  ()
P:0.0 R:0.0 F:0.0

input:  ['show', 'me', 'the', 'flights', 'that', 'accept', 'frequent', 'flyer', 'tickets', '.']
target:     ('TOP', ('VP', ('SHOW', 'show'), ('VPBAR', ('NP', 'me'), ('NP', ('NP', ('THE', 'the'), ('FLIGHTS', 'flights')), ('SBAR', ('WHNP', 'that'), ('VP', ('ACCEPT', 'accept'), ('NP', ('FREQUENT', 'frequent'), ('NPBAR', ('FLYER', 'flyer'), ('TICKETS', 'tickets')))))))), ('PUN', '.'))
predicted:  ()
P:0.0 R:0.0 F:0.0

input:  ['which', 'flights', 'depart', 'burbank', 'between', 'twelve', 'noon', 'and', 'six', 'p.m', '.']
target:     ('TOP', ('SBARQ', ('WHNP', ('WHICH', 'which'), ('FLIGHTS', 'flights')), ('VP', ('DEPART', 'depart'), ('VPBAR', ('NP', 'burbank'), ('PP', ('BETWEEN', 'between'), ('NP', ('NP', ('TWELVE', 'twelve'), ('NOON', 'noon')), ('NPBAR', ('AND', 'and'), ('NP', ('SIX', 'six'), ('P.M', 'p.m')))))))), ('PUN', '.'))
predicted:  ('TOP', ('SBARQ', ('WHNP', ('WHICH', 'which'), ('FLIGHTS', 'flights')), ('VP', ('DEPART', 'depart'), ('NP', ('NP', 'burbank'), ('NPBAR', ('PP', ('BETWEEN', 'between'), ('NP', ('TWELVE', 'twelve'), ('NOON', 'noon'))), ('NPBAR', ('AND', 'and'), ('NP', ('SIX', 'six'), ('P.M', 'p.m'))))))), ('PUN', '.'))
P:0.8571428571428571 R:0.8571428571428571 F:0.8571428571428571

input:  ['i', 'need', 'a', 'flight', 'from', 'kansas', 'city', 'to', 'newark', 'on', 'the', 'first', 'of', 'july', '.']
target:     ('TOP', ('S', ('NP', 'i'), ('VP', ('NEED', 'need'), ('NP', ('NP', ('A', 'a'), ('FLIGHT', 'flight')), ('NPBAR', ('PP', ('FROM', 'from'), ('NP', ('KANSAS', 'kansas'), ('CITY', 'city'))), ('NPBAR', ('PP', ('TO', 'to'), ('NP', 'newark')), ('PP', ('ON', 'on'), ('NP', ('NP', ('THE', 'the'), ('FIRST', 'first')), ('PP', ('OF', 'of'), ('NP', 'july'))))))))), ('PUN', '.'))
predicted:  ()
P:0.0 R:0.0 F:0.0

input:  ['what', 'flights', 'are', 'there', 'from', 'new', 'york', 'to', 'las', 'vegas', '.']
target:     ('TOP', ('SBARQ', ('WHNP', ('WHAT', 'what'), ('FLIGHTS', 'flights')), ('SQ', ('ARE', 'are'), ('SQBAR', ('NP', 'there'), ('SQBAR', ('PP', ('FROM', 'from'), ('NP', ('NEW', 'new'), ('YORK', 'york'))), ('PP', ('TO', 'to'), ('NP', ('LAS', 'las'), ('VEGAS', 'vegas'))))))), ('PUN', '.'))
predicted:  ('TOP', ('SBARQ', ('WHNP', ('WHAT', 'what'), ('FLIGHTS', 'flights')), ('SQ', ('ARE', 'are'), ('SQBAR', ('NP', 'there'), ('SQBAR', ('PP', ('FROM', 'from'), ('NP', ('NEW', 'new'), ('YORK', 'york'))), ('PP', ('TO', 'to'), ('NP', ('LAS', 'las'), ('VEGAS', 'vegas'))))))), ('PUN', '.'))
P:1.0 R:1.0 F:1.0

Coverage: 67.24%, Average F-score (parsed sentences): 0.9504475408614075, Average F-score (all sentences): 0.6390940360964636
```


