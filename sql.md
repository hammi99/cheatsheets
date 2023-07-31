<!-- 
https://www.freecodecamp.org/news/learn-sql-in-10-minutes/
https://www.sqltutorial.org/sql-cheat-sheet/
https://www.programiz.com/sql/data-types
https://www.scaler.com/topics/ddl-dml-dcl/
 -->
 
# SQL - Single Query Language

## Comments

```sql
-- single line comment
```

```sql
/*
multiline 
comment.
*/
```

---
## DDL - Data Definition Language

### CREATE
```sql
CREATE DATABASE `dbName`;
```

```sql
CREATE TABLE `tableName` (
    `columnName1` INT,
    `columnName2` VARCHAR(10)
);
```

### DROP
```sql
DROP DATABASE `dbName`; -- can also be used for TABLE, VIEW, INDEX and TRIGGER
```

### TRUNCATE
```sql
TRUNCATE TABLE `tableName`;
```

### ALTER

#### RENAME
```sql
ALTER TABLE `tableName1` TO `tableName2`;

ALTER TABLE `tableName` `columnName1` TO `columnName2`;
```

#### ADD
```sql
ALTER TABLE `tableName` ADD `columnName`;
ALTER TABLE `tableName` ADD `constraint`;
```

#### DROP
```sql
ALTER TABLE `tableName` DROP `columnName`;
ALTER TABLE `tableName` DROP `constraint`;
```

---
## DML - Data Manipulation Language
### INSERT

```sql
INSERT INTO `tableName` 
	(columnName1, columnName2, columnName3)
VALUES
	(a1, a2, a3),
	(b1, b2, b3)
;
```
### UPDATE
### DELETE
### CALL
### EXPLAIN CALL
### LOCK

---
## DCL - Data Control Language

### GRANT
### REVOKE

---
## DQL - Data Query Language

### SELECT

---
## TCL - Transaction Control Language

### COMMIT
### SAVEPOINT
### ROLLBACK
### SET TRANSACTION
### SET CONSTRAINT

---
## miscellaneous

```sql
USE database;

UPDATE myTable
SET ID += 1
WHERE <Condition>;
```
