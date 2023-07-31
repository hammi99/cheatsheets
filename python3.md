<!--
additional sources
https://docs.python.org/3/library/functions.html
-->


# Python3

## index

+ [comments ](#comments)
+ [integers ](#integers)
+ [floats   ](#floats)
+ [strings  ](#strings)
  + [multi line strings ](#multi-line-strings)
  + [escape sequences   ](#escape-sequences)
  + [r-string](#r-string)
  + [f-string](#f-string)
    + [debugging](#debugging)
    + [alignment](#alignment)
    + [types    ](#types)
    + [notations](#notations)
    + [precision](#precision)
+ [functions](#functions)
  + [decorators](#decorators)


## comments

```python
# this is a single line comment
```


## integers

```python
10    # >> 10       (decimal literal)
0b10  # >> 2        (binary literal)
0o10  # >> 8        (octal literal)
0x10  # >> 16       (hexadecimal literal)
```


## floats

```python
3.2   # >> 3.2
3.    # >> 3.0 
.2    # >> 0.2
```


## strings

```python
"hello world"     # >> hello world
'hello world'     # >> hello world

'hello "world"'   # >> hello "world"
"hello 'world'"   # >> hello 'world'
```

### multi line strings

```python
"""
hello
world 
"""
'''
hello 
world
'''
```

### escape sequences

```python
'ABCDE\'FGH'          # >> ABCDE'FGH        (escape quote mark)
'ABCDE\\FGH'          # >> ABCDE\FGH	    (escape back slash)

'ABCDE\bFGH'          # >> ABCDFGH          (backspace)
'ABCDE\rFGH'          # >> FGHDE            (carriage return)	
'ABCDE\fFGH'          # >> ABCDE FGH        (form feed)	
'ABCDE\tFGH'          # >> ABCDE  FGH       (tab)
'ABCDE\nFGH'          # >> ABCDE            (new line)	
                      #    FGH

'\101\102\103'        # >> ABC              (octal notation)
'\x41\x42\x43'        # >> ABC              (hexadecimal notation)
'\u0041\u0042\u0043'  # >> ABC              (unicode notation)
```

### r-string 

```python
r'raw string'         # >> raw string
r'ABCDE\nFGH'         # >> ABCDE\nFGH
r'ABCDE\rFGH'         # >> ABCDE\rFGH
r'ABCDEFGH\'          # >> Error
```

### f-string 
<!-- https://peps.python.org/pep-0498/  
http://cissandbox.bentley.edu/sandbox/wp-content/uploads/2022-02-10-Documentation-on-f-strings-Updated.pdf  
f'{expression debugging : alignment comma precision type func}'
use f'{{}}' to escape curly brackets  
-->

#### debugging

```python
exp = 123

f'{exp=}'     # >> exp=123
f'{exp= }'    # >> exp= 123
f'{exp =}'    # >> exp =123
f'{exp = }'   # >> exp = 123
```

#### alignment

```python
exp = 123

f'|{exp:<5}|'  # >> |123  |
f'|{exp:>5}|'  # >> |  123|
f'|{exp:^5}|'  # >> | 123 |

f'|{exp:-<5}|'  # >> |123--|
f'|{exp:0>5}|'  # >> |00123|
f'|{exp:~^5}|'  # >> |~123~|
```

#### precision

```python
f'{exp:.3}'
```

#### notations

```python
exp = 123

f'{exp:b}'  # >> 1111011          (integer to binary)
f'{exp:o}'  # >> 173              (integer to octal)
f'{exp:d}'  # >> 123              (integer to decimal)
f'{exp:x}'  # >> 7b               (integer to hexadecimal lowercase)
f'{exp:X}'  # >> 7B               (integer to hexadecimal uppercase)

f'{exp:f}'  # >> 123.0            (number to point decimal)
f'{exp:e}'  # >> 1.230000e+02     (number to scientific)
f'{exp:%}'  # >> 12300.000000%    (number to percentage)

f'{exp:n}'  # >> 123              (number to decimal or point decimal)

f'{exp:s}'  # ERROR               (string to string)
```

```python
f'{name} is {age!r}' # >> eric is 74.12345    (!r forces python to use __repr__ instead of __str__)
```


## functions

### decorators

```python
# for a higher order function
def foo(func):
  def temp(*args,**kwargs):
    # some steps
    return func(*args,**kwargs)
  return temp

# doing this
@foo
def bar():
  pass

# is the same as doing this
def bar():
  pass
bar = foo(bar)
```


## Operator Precedence

```python
()	
**	
+x, -x, ~x	
*, /, //, %	
+, -	
<<, >>	
&	
^	 
|	
==, !=, >, >=, <, <=, is, is not, in, not in	
not	
and	
or
```
