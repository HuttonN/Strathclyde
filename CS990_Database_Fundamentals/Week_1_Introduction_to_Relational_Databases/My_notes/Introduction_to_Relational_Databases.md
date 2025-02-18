# The Relational Data Model

This lecture covers the fundamental concepts of the relational data model, its historical development, key terminology, integrity constraints, and relational schema representation.

## Introduction to the Relational Data Model

The **relational model** was first proposed by **Edgar F. Codd** in 1970. It provides a **mathematical foundation** for databases, ensuring **data independence**, **semantic consistency**, and **minimal redundancy**.

### Key Objectives
- **Data Independence**: Users interact with the database without needing to know its internal structure.
- **Consistency and Redundancy Management**: The relational model minimizes redundancy and ensures consistency through normalization.

## Historical Background

- **System R (IBM, 1970s)**: First implementation of the relational model.
- **SQL Development**: SQL emerged as a standard query language from System R.
- **Commercial Adoption**: Products like DB2, Oracle, and SQL/DS were released in the 1980s.
- **Modern Relational Databases**: There are now both commercial and open-source relational database management systems (RDBMS).

## Core Concepts of the Relational Model

The relational model is based on **set theory and logic**. A **relation** is represented as a **two-dimensional table**.

### Terminology

Consider an estate agency with several branches. We can store inforamtion like the following:

![relation example](images/Relation_example.png)

- An **attribute** is a named column of a relation Correspondingly, a relation comprises one or more named columns representing the attributes of a particular entity type.
- Each attribute has an associated **domain** which is the set of allowable values  
- The rows of a relation are called **records**, or more formally, **tuples**. They represent individual records. The order of the rows is not important.
- The **degree** of a reltion is the number of attributes it contains, e.g. BRANCH relation has degree 6.
- The **cardinality** of a relation is the number of records it contains, e.g. BRANCH relation has cardinality 5.

### Properties of Relations

1. **Unique Relation Names**: Each relation (table) must have a unique name.
2. **Unique Attribute Names per Relation**: Attributes must be uniquely named within a relation. For example, we can have two attributes called *Name* is seperate relations, but not in the same relation.
3. **Attributes Have Fixed Domains**: Each attribute must contain values from a predefined domain. i.e. we should not allow a postcode to appear in a salary column for example
4. **Order Independence**: The order of tuples and attributes in a relation does not matter.
5. **Atomicity of Attributes**: Each cell of a relation should contain at most one value (no multi-valued attributes).
6. **Uniqueness of Tuples**: No two tuples (records) should be identical. (Database systems don't generally enforce this property)

## Keys in the Relational Model

To be able to uniquely identify each row in a relation by the value of its attributes we use **relational keys**. They consist of a chosen attribute or set of attributes from the relation in question. 

However,
- how do we decide which attribute(s) to choose as the key for a given relation?
- is there always a unique key, or do we sometimes have to select one from a number of possibilities

### **Candidate Keys**

A key is said to be *minimal* if removing any attributes would mean that it no longer provides unique identification.

When choosing a key for a relation, we may pick any minimal key. Minimal keys are therefore called *candidate keys*.

For example, $(Bno)$ is a candidate key for the $BRANCH$ relation but $(Bno, Postcode)$ isn't.

A candidate key may involve more than one attribute. In that case the key is said to be composite.

#### Properties of Candidate Keys

A candidate key, $K$, for a relation $R$ has the following properties:

* *Uniqueness:*
    - In each row of $R$, the values of $K$ uniquely identify that row.
    - In other words: no two rows of $R$ can have the same value for $K$ 
* *Irreducibility:*
    - No subset of $K$ has the uniqueness property
    - Therefore, $K$ cannot consist of fewer attributes

Note: some relations may have several candidate keys.

#### Finding Candidate Keys

An instance of a relation (i.e. a particular table or set of records) cannot be used to prove that an attribute or combination of attributes is a candidate key (nor to select an appropriate candidate key).

Consider a table *Addresses* with the following attributes:

![Address relation](images/Address_relation.png)

If in the current data, every postcode is unique, one might think that *Postcode* is a candidate key. However, in reality, multiple addresses can share the same postcode (e.g., multiple apartments in a building). Thus, future data might introduce duplicates, violating the uniqueness requirement. This means *Postcode* is not a candidate key.

The presence of duplicates may be used to show that a certain attribute or combination of attributes is not a candidate key.

To correctly identify a candidate key, we need to be aware of the meanings of the attributes in the real world, and think about whether duplicates could arise for a given choice of key

### Primary Keys

For each relation in a database, we must choose one of its candidate keys to be its *primary key*.

Note: since, by definition, a relation cannot have duplicate rows, it is always possible to uniquely identify each row. In the worst case, the entire set of attributes could serve as the primary key, but usually some smaller subset is sufficient.

Despite the above, many database systems allow relations to contain duplicates and so this theoretical property doesn't necessarily apply in practice. We are often best served by introducing an *artificial key* attribute if a natural primary key cannot be found. This could be simply a *record number*. 

### **Foreign Keys (COME BACK TO!!!)**
A **foreign key** is an attribute (or set of attributes) in one relation that refers to the primary key of another relation.

#### **Example: Staff and Department Relations**
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

## Relational Schema Representation

A relational schema defines the **structure** of a database in a formal notation:

$relation\_name(\underline{attribute1}, attribute2, \ldots, attributeN)$

* the name of the relation is followed by a list of the names of the attributes it contains
* the primary key attributes are underlined
* Foreign key attributes should be shown using some distinguishing feature such as a dashed underline

## Integrity constraints

### Entity Integrity

The entity integrity rule applies to the primary keys of relations.

***Entity Integrity Rule:***

In a relation, no attribute of a primary key can be null



### Referential Integrity

The referential integrity rule applies to foreign keys:

***Referential Integrity Rule:***
If a relation contains a foreign key, either the foreign key value must match the value of a candidate key of a record in the home relation, or the foreign key value must be wholly null.


