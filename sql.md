<!-- 
https://www.freecodecamp.org/news/learn-sql-in-10-minutes/
https://www.sqltutorial.org/sql-cheat-sheet/
https://www.programiz.com/sql/data-types
https://www.scaler.com/topics/ddl-dml-dcl/
 -->
 
# SQL - Single Query Language

## comments
> ```sql
> -- single line comment
> ```
> ```sql
> /*
> multiline 
> comment.
> */
> ```

## DDL - Data Definition Language
> ### CREATE
>> ```sql
>> CREATE DATABASE dbName;
>> ```
>> ```sql
>> CREATE TABLE tableName (
>>     columnName1 INT,
>>     columnName2 VARCHAR(10)
>> );
>> ```
>> 
> ### ALTER
> 
>> #### RENAME
>> ```sql
>> ALTER TABLE tableName1 TO tableName2
>> ```
>> ```sql
>> ALTER TABLE tableName columnName1 TO columnName2;
>> ```
>> 
>> #### ADD
>> ```sql
>> ALTER TABLE tableName ADD columnName;
>> ```
>> ```sql
>> ALTER TABLE tableName ADD constraint;
>> ```
>> 
>> #### DROP
>> ```sql
>> ALTER TABLE tableName DROP columnName;
>> ```
>> ```sql
>> ALTER TABLE tableName DROP constraint;
>> ```
>
> ### DROP
> ### TRUNCATE

## DML - Data Manipulation Language
> ### SELECT
> ### INSERT
> ### UPDATE
> ### DELETE

### DCL - Data Control Language
