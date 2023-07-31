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
ALTER TABLE `tableName1` RENAME TO `tableName2`;

ALTER TABLE `tableName` `columnName1` TO `columnName2`;
```

#### ADD
```sql
ALTER TABLE `tableName` ADD (
    `columnName1` INT,
    `columnName2` VARCHAR(10)
);
```

#### DROP
```sql
ALTER TABLE `tableName` DROP `columnName`;
```

---
## DML - Data Manipulation Language
### INSERT

```sql
INSERT INTO `tableName` 
	(`columnName1`, `columnName2`, `columnName3`)
VALUES
	(<value>, <value>, <value>),
	(<value>, <value>, <value>)
;
```
### UPDATE

```sql
UPDATE `tableName` 
SET 
	`columnName1` = <value>, 
	`columnName2` = <value>
WHERE
	<condition>
;
```
### DELETE
### CALL
### EXPLAIN CALL
### LOCK

---
## DCL - Data Control Language

### USE
```sql
USE `dbName`;
```
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
