# Programming and variables

## Introduction

### Running a Python file

To run a python file from the terminal type *python3.11* followed by the name of the file. For example, to run 1.py:

```bash
python3.11 1.py
```


## Simple variables

## Basic containers

### Lists

#### Accessing List Items

* Negative Indexing
* Range of Indexes
* Range of Negative Indexes

###### Check if Item Exists

The ```in``` keyword can be used to check if an item is in a list, returning ```True``` if it is and ```False``` otherwise.


#### Changing List Items

#### Adding List Items

#### Removing List Items

#### List Methods

* append()
    * Definition and Usage: appends an element to the end of a list
    * Syntax: ```list.append(elmnt)```, where ```element``` can be of any type.
    * Example: 

        ![append() example](images/Lists/append()_example.png)

* clear()
    * Definition and Usage: removes all elements from a list
    * Syntax: ```list.clear()```
    * Example: 

        ![clear() example](images/Lists/clear()_example.png)
* copy()
    * Definition and Usage: returns a copy of the specified list
    * Syntax: ```list.copy()```
    * Example: 

        ![copy() example](images/Lists/copy()_example.png)

* count()
    * Definition and Usage: returns the number of elements with the specified value
    * Syntax: ```list.count(value)```
    * Parameter values: 
        * Required. 
        * Any type. 
        * The value to search for 
    * Example: 

        ![count() example](images/Lists/count()_example.png)

* extend()
    * Definition and Usage: adds the specified list element (or any iterable) to the end of the list
    * Syntax: ```list.extend(iterable)```
    * Parameter values: 
        * Required. 
        * Any interable (list, set, tuple, etc.)
    * Example: 

        

* index()
    * Definition and Usage: returns the position of the *first* occurence of the specified value
    * Syntax: ```list.index(elmnt)```
    * Parameter values: 
        * Required. 
        * Any type (string, number, list, etc.)
        * The element to search for
    * Example: 

        

* insert()
    * Definition and Usage: inserts the specified value at the specified position
    * Syntax: ```list.insert(pos, elmnt)```
    * Parameter values:
        * ```pos```: 
            * Required. 
            * Number specifying in which position to insert the value
        * ```elmnt```: 
            * Required. 
            * Element of any type (string, number, object, etc.)
    * Example: 

        

* pop()
    * Definition and Usage: removes the element at the specified position
    * Syntax: ```list.pop(pos)```
    * Parameter values: 
        * Optional. 
        * A number specifying the position of the element you want to remove
        * Default value is -1, which removes the last item
    * Example: 

        

* remove()
* reverse()
* sort()
    * Syntax:
        * ```python list.sort```
        

### Dictionaries

## Examples