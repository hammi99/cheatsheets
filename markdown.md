<!-- 
https://www.w3schools.io/file/markdown-introduction/  
https://www.markdowntutorial.com/
https://www.markdownguide.org/cheat-sheet/
https://github.github.com/gfm/
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
 -->

# Github flavoured Markdown

## index

* [comments       ](#comments)
* [emphasis       ](#emphasis)
* [line break     ](#line-break)
* [code block     ](#code-block)
* [blockquotes    ](#blockquotes)
* [headings       ](#headings)
* [lists          ](#lists)
  * [unordered     ](#unordered)
  * [ordered       ](#ordered)
* [task lists     ](#task-list)
* [tables         ](#tables)
* [links          ](#links)
* [images         ](#images)
* [footnote       ](#footnote)
* [horizontal rule](#horizontal-rule)


## comments

> ```markdown
> <!-- inside comment -->
> ```


## emphasis

> ```markdown
> regular text
>
> *italic text*
> **bold text**
>
> _italic text_
> __bold text__
>
> ~~strikethrough text~~
>
> `code element`
> ```


## line break

> ```markdown
> line1 \ 
> line2
> ```
>
> ```markdown
> line1(space)(space)
> line2
> ```


## code block

> `````markdown
> ```python
> print('line 1')
> print('line 2') 
> ```
>
> ````markdown
> ```python
> print('use different number of ticks to nest code blocks')
> ```
> ````
> `````
>
> ```markdown
> ~~~javascript
> console.log('line 1');
> console.log('line 2');
> ~~~
> ```


## blockquotes

> ```markdown
>> block text
>>> nested text
> ```


## headings

> ```markdown
> #       heading1
> ##      heading2
> ###     heading3
> ####    heading4
> #####   heading5
> ######  heading6
> ```
>
> ```markdown
> heading1
> =
> heading2
> -
> ```


## lists

> ### unordered
>
>> ```markdown
>> + item 1
>> + item 2
>>  + nested item
>> ```
>>
>> ```markdown
>> + item 1
>> - item 1
>> * item 1
>> ```
>>
>
> ### ordered
>
>> ```markdown
>> 1. item 1
>> 2. item 2
>> ```
>>


## task list

> ```markdown
> + [ ] task 1
> + [X] completed task 
>   + [ ] nested task
> ```
>
> ```markdown
> + [ ] task1
> - [ ] task1
> * [ ] task1
> ```


## tables

> ```markdown
> | column A     | column B        | column A   
> | ------------ |:---------------:| -------------:
> | left aligned | centere aligned | right-aligned 
> | aaa          | bbb             | ccc         
> ```


## links

> ```markdown
> [text](url)
> [text](url "title")
> [text][refrence]
>
> [refrence]: url
> [refrence]: url "title"
> ```


## images

> ```markdown
> ![text](url)
> ![text](url "title")
> ![text][refrence]
>
> [refrence]: url
> [refrence]: url "title"
> ```


## footnote

> ```markdown
> Here's a sentence with a footnote. [^1]
>
> [^1]: This is the footnote.
> ```


## horizontal rule

> ```markdown
> ***
> ---
> ___
> ```