# he Relational Data Model - questions

## Introduction to the Relational Data Model

&nbsp;
<details>
<summary>
1. Describe the background to the relational model
</summary>

* The **relational model** was first proposed by **Edgar F. Codd** in 1970. 
* It provides a **mathematical foundation** for databases, ensuring **data independence**, **semantic consistency**, and **minimal redundancy**.

</details>

## Key Objectives

&nbsp;
<details>
<summary>
1. State the key objectives of the relational model
</summary>

- **Data Independence**: Users’ interactions with the database must not be affected by changes to the internal view of data, particularly record orderings and access paths.
- **Consistency and Redundancy Management**: The relational model minimizes redundancy and ensures consistency through normalization.

</details>

### Historical Background

&nbsp;
<details>
<summary>
1. Describe the historical background to the relational model
</summary>

System R (IBM, 1970s) was the first implementation of the relational model. Intended as a "proof of concept", it gave rise to two major developments:
- **SQL Development**: SQL emerged as a standard query language from System R.
- **Commercial Adoption**: Products like DB2, Oracle, and SQL/DS were released in the 1980s.

</details>

## Core Concepts of the Relational Model

&nbsp;
<details>
<summary>
1. What is the relational model based on 
</summary>

The relational model is based on **set theory and logic**.

</details>

&nbsp;
<details>

<summary>
2. How is a relation represented
</summary>

A **relation** is represented as a **two-dimensional table**.

</details>

### Terminology

&nbsp;
<details>
<summary>
1. Describe, using an example, the terminology used in the relational model
</summary>

Consider an estate agency with several branches. We can store inforamtion like the following:

![relation example](images/Relation_example.png)

- An **attribute** is a named column of a relation. Correspondingly, a relation comprises one or more named columns representing the attributes of a particular entity type. The order of attributes is unimportant.
- Each attribute has an associated **domain** which is the set of allowable values  
- The rows of a relation are called **records**, or more formally, **tuples**. They represent individual records. The order of the rows is not important.
- The **degree** of a relation is the number of attributes it contains, e.g. BRANCH relation has degree 6.
- The **cardinality** of a relation is the number of records it contains, e.g. BRANCH relation has cardinality 5.

</details>

### Properties of Relations

&nbsp;
<details>
<summary>
1. State the properties of relations in the relational model
</summary>

1. **Unique Relation Names**: Each relation (table) must have a unique name.
2. **Unique Attribute Names per Relation**: Attributes must be uniquely named within a relation. For example, we can have two attributes called *Name* is seperate relations, but not in the same relation.
3. **Attributes Have Fixed Domains**: Each attribute must contain values from a predefined domain. i.e. we should not allow a postcode to appear in a salary column for example
4. **Order Independence**: The order of tuples and attributes in a relation does not matter.
5. **Atomicity of Attributes**: Each cell of a relation should contain at most one value (no multi-valued attributes).
6. **Uniqueness of Tuples**: No two tuples (records) should be identical. (Database systems don't generally enforce this property)

</details>

## Keys in the Relational Model

&nbsp;
<details>
<summary>
1. How do we uniquely identify each row in a relation
</summary>

To be able to uniquely identify each row in a relation by the value of its attributes we use **relational keys**. They consist of a chosen attribute or set of attributes from the relation in question. 

</details>

&nbsp;
<details>
<summary>
2. What questions should we consider with regard to keys
</summary>

- how do we decide which attribute(s) to choose as the key for a given relation?
- is there always a unique key, or do we sometimes have to select one from a number of possibilities

</details>

### **Candidate Keys**

&nbsp;
<details>
<summary>
1. Define a minimal key
</summary>

A key is said to be *minimal* if removing any attributes would mean that it no longer provides unique identification.

</details>

&nbsp;
<details>
<summary>
2. What are minimal keys also known as, and why
</summary>

When choosing a key for a relation, we may pick any minimal key. Minimal keys are therefore called *candidate keys*.

</details>

&nbsp;
<details>
<summary>
3. State an example and a non-example of a candidate key for the following relation

![relation example](images/Relation_example.png)

</summary>

$(Bno)$ is a candidate key for the $BRANCH$ relation but $(Bno, Postcode)$ isn't.

</details>

&nbsp;
<details>
<summary>
4. What is a composite key
</summary>

A candidate key may involve more than one attribute. In that case the key is said to be composite.

</details>

#### Properties of Candidate Keys

&nbsp;
<details>
<summary>
1. State the properties of candidate keys
</summary>

A candidate key, $K$, for a relation $R$ has the following properties:

* *Uniqueness:*
    - In each row of $R$, the values of $K$ uniquely identify that row.
    - In other words: no two rows of $R$ can have the same value for $K$ 
* *Irreducibility:*
    - No subset of $K$ has the uniqueness property
    - Therefore, $K$ cannot consist of fewer attributes

</details>

&nbsp;
<details>
<summary>
2. How many candidate keys may a relation have
</summary>

some relations may have several candidate keys.

</details>

#### Finding Candidate Keys

&nbsp;
<details>
<summary>
1. Describe an issue with finding candidate keys
</summary>

An instance of a relation (i.e. a particular table or set of records) cannot be used to prove that an attribute or combination of attributes is a candidate key (nor to select an appropriate candidate key).

Consider a table *Addresses* with the following attributes:

![Address relation](images/Address_relation.png)

If in the current data, every postcode is unique, one might think that *Postcode* is a candidate key. However, in reality, multiple addresses can share the same postcode (e.g., multiple apartments in a building). Thus, future data might introduce duplicates, violating the uniqueness requirement. This means *Postcode* is not a candidate key.

</details>

&nbsp;
<details>
<summary>
2. How can we show a certain attribute or combination of attributes is not a candidate key
</summary>

The presence of duplicates may be used to show that a certain attribute or combination of attributes is not a candidate key.

</details>

&nbsp;
<details>
<summary>
3. What needs to be done to correctly identify a candidate key
</summary>

To correctly identify a candidate key, we need to be aware of the meanings of the attributes in the real world, and think about whether duplicates could arise for a given choice of key

</details>

### Primary Keys

&nbsp;
<details>
<summary>
1. What needs to be done for each relation in a database
</summary>

For each relation in a database, we must choose one of its candidate keys to be its *primary key*.

</details>

&nbsp;
<details>
<summary>
2. Is it always possible to uniquely identify each row in a relation
</summary>

Since, by definition, a relation cannot have duplicate rows, it is always possible to uniquely identify each row. In the worst case, the entire set of attributes could serve as the primary key, but usually some smaller subset is sufficient.

</details>

&nbsp;
<details>
<summary>
3. What theoretical property do many database systems violate
</summary>

Despite the uniqueness property, many database systems allow relations to contain duplicates and so this theoretical property doesn't necessarily apply in practice.

</details>

&nbsp;
<details>
<summary>
4. What can we do if a primary key can't be found
</summary>

We are often best served by introducing an *artificial key* attribute if a natural primary key cannot be found. This could be simply a *record number*. 

</details>

### Foreign Keys

&nbsp;
<details>
<summary>
1. Define a foreign key
</summary>

A **foreign key** is an attribute (or set of attributes) in one relation that refers to the primary key of another relation.

</details>

#### Example: Staff and Department Relations

&nbsp;
<details>
<summary>
1. Describe an example
</summary>

**STAFF Table**
| Sno  | Name        | DeptNo |
|------|------------|--------|
| SG86 | David Hulse | 31     |
| SP52 | Paul Kingston | 49  |

**DEPARTMENT Table**
| DeptNo | Name               | NumRooms |
|--------|--------------------|----------|
| 31     | Computing Science  | 18       |
| 49     | Management         | 15       |

- `DeptNo` in **STAFF** is a **foreign key** referencing `DeptNo` in **DEPARTMENT**.

</details>

## Relational Schema Representation

&nbsp;
<details>
<summary>
1. Define and describe a relational schema
</summary>

A relational schema defines the **structure** of a database in a formal notation:

$relation\_name(\underline{attribute1}, attribute2, \ldots, attributeN)$

* the name of the relation is followed by a list of the names of the attributes it contains
* the primary key attribute(s) are underlined
* Foreign key attributes should be shown using some distinguishing feature such as a dashed underline

</details>

## Views

&nbsp;
<details>
<summary>
1. Define and describe a view
</summary>

A **view** is a virtual or derived relation based on one or more base tables. It is defined by a query and does not physically store data (unless materialized). Instead, it acts like a *window* into the underlying data, showing only what is specified in the view definition.

</details>

### Purpose of views

&nbsp;
<details>
<summary>
1. State the purpose of views
</summary>

- **Security**: Restrict access to sensitive data by exposing only certain attributes or rows.
- **Simplification**: Encapsulate complex joins, aggregations, or filtering logic for easier querying.
- **Data Independence**: Provide a stable interface for applications, even if the base tables change.
- **Customization**: Present data differently for different user roles.

</details>

### Example

&nbsp;
<details>
<summary>
1. Give an example of a view
</summary>

Suppose we want to allow staff to view only basic information about their own department.

```sql
CREATE VIEW StaffView AS
SELECT Sno, Name, DeptNo
FROM STAFF
WHERE DeptNo IS NOT NULL;
```

This view shows only selected columns and hides salary or personal data.

</details>

### View Representation (Schema Notation)

&nbsp;
<details>
<summary>
1. How can views be represented
</summary>

Like base relations, views can be represented using relational schema notation:

```sql
StaffView(Sno, Name, DeptNo)
```

Note: Views are not part of the base schema but derive from it.

</details>

### View Updatability

&nbsp;
<details>
<summary>
1. What conditions must a view satisfy to be updatable
</summary>

A view is updatable if it satisfies the following:
* Based on a single base relation,
* Contains no aggregation, grouping, or set operations (SUM, GROUP BY, UNION, etc.),
* Does not include DISTINCT, LIMIT, or joins,
* Contains the primary key of the base relation,
* Does not use calculated fields (e.g. salary * 1.1 AS bonus).

</details>

### Updating Views

&nbsp;
<details>
<summary>
1. Provide code to update the department number for staff with number SG86 to 42
</summary>

```sql
UPDATE StaffView
SET DeptNo = 42
WHERE Sno = 'SG86';
```

</details>

### Materialized Views

&nbsp;
<details>
<summary>
1. Describe materialized views
</summary>

Some DBMSs support materialized views, which store the result of the view query for performance reasons. These need to be refreshed to stay current.

</details>

## Integrity constraints

&nbsp;
<details>
<summary>
1. State the two principle integrity constraints of the relational data model
</summary>

* Entity Integrity Rule
* Referential Integrity

</details>

&nbsp;
<details>
<summary>
2. What do these integrity constraints depend on
</summary>

The concept of nulls

</details>

### Nulls

&nbsp;
<details>
<summary>
1. Define a null
</summary>

A null represents the value of an attribute that is currently unknown, or is now applicable for a particular record. They provide a way of dealing with incomplete or exceptional data.

</details>

&nbsp;
<details>
<summary>
2. What is a null not
</summary>

A null is not the same as a zero value, an empty string, or a string filled with spaces (all of the latter are values whereas a null means no value).

</details>

&nbsp;
<details>
<summary>
3. Describe an example
</summary>

Consider a viewing relation:

$Viewing(\underline{Pno}, \underline{Rno}, \underline{Date}, Time, Comment)$

The Comment field is to be filled in after a viewing has taken place. When the viewing is initially arranged, there is no data to store in the field. To represent this initial lack of information, we can use a null.

</details>

### Entity Integrity

&nbsp;
<details>
<summary>
1. What does the entity integrity rule apply to
</summary>

The entity integrity rule applies to the primary keys of relations.

</details>

&nbsp;
<details>
<summary>
2. State the entity integrity rule
</summary>

In a relation, no attribute of a primary key can be null

</details>

&nbsp;
<details>
<summary>
3. Explain the reasoning behind the entity integrity rule
</summary>

By definition, a primary key is a minimal superkey that is used to identify records uniquely (no subset of the primary is sufficient to provide unique identification). If we were to allow a null for any part of a primary key, we imply that not all of the attributes are needed for unique identification (contradicts the definition of the primary key).

</details>

### Referential Integrity

&nbsp;
<details>
<summary>
1. What does the referential integrity rule apply to
</summary>

The referential integrity rule applies to foreign keys.

</details>

&nbsp;
<details>
<summary>
2. State the referential integrity rule
</summary>

If a relation contains a foreign key, either the foreign key value must match the value of a candidate key of a record in the home relation, or the foreign key value must be wholly null.

</details>

&nbsp;
<details>
<summary>
3. Describe the referential integrity rule using an example
</summary>

In the Staff and Department example, the Staff relation contains a foreign key from the Department relation - the DeptNo field that relates a staff member to the department in which they work. 

![Staff and Department relations relations](images/Staff_Department_relations.png)

The Referential Integrity rule state that we should no be able to insert a staff member record for which the DeptNo field refers to a department that does not exist in the Department relation. We can however set the DeptNo field to null in the Staff relation

</details>