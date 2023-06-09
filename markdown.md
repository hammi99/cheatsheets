<!-- 
things to confirm ~~~what is this?~~~


links:
https://www.w3schools.io/file/markdown-introduction/  
https://www.markdowntutorial.com/
https://www.markdownguide.org/cheat-sheet/
https://github.github.com/gfm/
 -->

# Github flavoured Markdown

## index

* [comments](#comments)
* [text formatting](#text-formatting)
* [line break](#line-break)
* [code block](#code-block)
* [blockquotes](#blockquotes)
* [headings](#headings)
* [lists](#lists)
  * [ordered](#ordered)
  * [unordered](#unordered)
* [tables](#tables)
* [links](#links)
* [images](#images)
* [horizontal rule](#horizontal-rule)

## comments
```markdown
<!-- inside comment -->
```


## text formatting
```markdown
regular text
**bold text**
_italic text_
*italic text*
~strikethrough text~
`code element`
```


## line break
```markdown
line1 \ 
line2
```
```markdown
line1<space><space>
line2
```

## code block
~~~markdown
```python
print('line 1')
print('line 2') 
```
~~~
```markdown
~~~javascript
console.log('line 1');
console.log('line 2');
~~~
```

## blockquotes
```markdown
> block text
>> nested text
```


## headings
```markdown
#       heading1
##      heading2
###     heading3
####    heading4
#####   heading5
######  heading6
```
```markdown
heading1
=
heading2
-
```


## lists

### ordered
```markdown
1. item 1
2. item 2
```
### unordered
```markdown
* item 1
* item 2
 * nested item
* item 3
```
```markdown
- item 1
+ item 1
* item 1
```


## tables
```markdown
|col1     |col2     |col3
|-        |-        |-
|data00   |data01   |data02
|data10   |data11   |data12
```


## links
```markdown
[Link text](url)
[Link text](url "title")
[Link text][refrence]

[refrence]: url
[refrence]: url "title"
```


## images
```markdown
![alt text](url)
![alt text](url "title")
![alt text][refrence]

[refrence]: url
[refrence]: url "title"
```

## horizontal rule
```markdown
***
---
___
```
