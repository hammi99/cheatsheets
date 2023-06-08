# single line comment


# integers
10    # >> 10       (decimal literal)
0b10  # >> 2        (binary literal)
0o10  # >> 8        (octal literal)
0x10  # >> 16       (hexadecimal literal)


# floats
3.2   # >> 3.2
3.    # >> 3.0 
.2    # >> 0.2


# strings
"hello world"     # >> hello world
'hello world'     # >> hello world

'hello "world"'   # >> hello "world"
"hello 'world'"   # >> hello 'world'

## multi line strings
"""
hello
world 
"""
'''
hello 
world
'''

## escape sequences
'ABCDE\'FGH'	        # >> ABCDE'FGH
'ABCDE\\FGH'          # >> ABCDE\FGH	
'ABCDE\bFGH'          # >> ABCDFGH          (backspace)
'ABCDE\rFGH'	        # >> FGHDE            (carriage return)	
'ABCDE\fFGH'	        # >> ABCDE FGH        (form feed)	
'ABCDE\tFGH'	        # >> ABCDE  FGH       (tab)
'ABCDE\nFGH'   	      # >> ABCDE            (new line)	
                      #    FGH

'\101\102\103'        # >> ABC              (octal notation)
'\x41\x42\x43'        # >> ABC              (hexadecimal notation)
'\u0041\u0042\u0043'  # >> ABC              (unicode notation)

## r-string (ignores escape sequences) (error if last character is '\')
r'raw string'         # >> raw string
r'ABCDE\nFGH'         # >> ABCDE\nFGH
r'ABCDE\rFGH'         # >> ABCDE\rFGH

## https://peps.python.org/pep-0498/
# http://cissandbox.bentley.edu/sandbox/wp-content/uploads/2022-02-10-Documentation-on-f-strings-Updated.pdf
## f-string (formats string)
# f'{expression debug : alignment precision type}'
# use f'{{}}' to escape curly brackets


### debugging
exp = 123
f'{exp=}'     # >> exp=123
f'{exp= }'    # >> exp= 123
f'{exp =}'    # >> exp =123
f'{exp = }'   # >> exp = 123

### alignment
f'|{exp:<5}|'  # >> |123  |
f'|{exp:>5}|'  # >> |  123|
f'|{exp:^5}|'  # >> | 123 |

### types: ensure that the expession is of a specific type
f'{exp:d}'  # >> 123              (integer)
f'{exp:f}'  # >> 123.0            (float)
f'{exp:n}'  # >> 123              (number)
f'{exp:s}'  #                     (string)

### notations: represent the expression in a specific notation
f'{exp:b}'  # >> 1111011          (integer to binary)
f'{exp:o}'  # >> 173              (integer to octal)
f'{exp:x}'  # >> 7b               (integer to hexadecimal lowercase)
f'{exp:X}'  # >> 7B               (integer to hexadecimal uppercase)

f'{exp:e}'  # >> 1.230000e+02     (number to scientific)
f'{exp:%}'  # >> 12300.000000%    (number to percentage)

### precision: 
f'{exp:.3}'

f'{name} is {age!r}' # >> eric is 74.12345    (!r forces python to use __repr__ instead of __str__)


# decorators

def foo(func):
  def temp(*args,**kwargs):
    # some steps
    return func(*args,**kwargs)
  return temp

## doing this
@foo
def bar():
  pass

## is the same as
def bar():
  pass
bar = foo(bar)
