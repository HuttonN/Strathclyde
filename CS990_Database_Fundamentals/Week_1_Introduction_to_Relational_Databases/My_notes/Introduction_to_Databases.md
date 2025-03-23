# Lecture 1 – Introduction to Databases

This lecture introduces the concept of databases, their historical development, and the foundational ideas behind modern database systems.

---

## What Is a Database?

A **database** is a *shared collection* of logically related data, **plus its description** intended to meet the **information needs** of an organization. The description is provided in a system catalogue (metadata).

Note:
* **Data** = raw facts (e.g. `"bill"`)  
* **Information** = structured data with meaning (e.g. `"Name: Bill"`)

---

## Historical Development of Data Models

### Flat Files (Pre-1970s)

![Flat File](images/Flat_File.png)

Predecessor of database where data was maintained in a flat file.

Earlier, punched cards technology was used to store data - later files. The files had no such advantage.

### Hierarchical Model (1968–1980)

![Hierarchial Data Model](images/Hierarchial_Data_Model.png)

Files are related in a parent/child manner, with each child file having at most one parent file.

### Network Model (1960–1971)

![Network Data Model](images/Network_Data_Model.png)

Files are related as owners and members, similar to the common network model except that each member file can have more than one owner.

---

## Relational Model (1970–Present)

Introduced by **Ted Codd** in 1970, the relational model is based on **set theory** and **predicate logic**.

Two terminologies:
- **Instance**: A table (relation) with rows and columns.
- **Schema**: Describes the structure (name, columns, and types).

---

## Entity-Relationship (ER) Notation

The Entity Relationship Model is a model for identifying entities (things), attributes (properties) and relationships (associations) to be represented in a database. 

It uses the following notation:

![Network Data Model](images/Network_Data_Model.png)

Consider the following example:

![Simple ER example](images/Simple_ER_example.png)

This ER diagram represents a basic shopping system where **shoppers** buy **items**.

We have Shopper and Item entities:

- **Shopper**
  - Represents a customer or buyer.
  - (Attributes not shown in diagram.)

- **Item**
  - Represents a product available for purchase.
  - Attributes:
    - `item_type` – The category/type of the item.
    - `item_price` – The price of the item.
    - `item_source` – Where the item came from (e.g., brand/vendor).

There is a single relationship - ***Buys***

- **Buys**
  - Connects `Shopper` and `Item`.
  - Implies that shoppers can buy one or more items.


## Examples of Database Applications

* Purchases from the supermarket
* Facebook/Twitter (FB 5 petabytes/day)
* Booking a holiday
* Checking your phone
* Taking out insurance
* Using the Internet
* Studying at university

---

## 🧾 Summary Table

| Concept             | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| **Database**        | A collection of logically related data + metadata                           |
| **Flat Files**      | Early data storage with no structure or relationships                       |
| **Hierarchical**    | Tree-based parent–child model                                               |
| **Network**         | Owner–member relationships, more flexible than hierarchical                 |
| **Relational Model**| Table-based, grounded in mathematics (set theory + predicate logic)         |
| **ER Notation**     | Diagrammatic representation of data using entities, attributes, relationships |

---

## 🔗 Further Reading

- Codd, E. F. (1970) *A Relational Model of Data for Large Shared Data Banks*
- [Relational model - Simple Wikipedia](https://simple.wikipedia.org/wiki/Relational_model)
- [ER Model - Peter Chen](https://www.csc.lsu.edu/~chen/)

---
