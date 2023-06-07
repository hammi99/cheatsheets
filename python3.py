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
