# Processing collections (the for-each loop)

## Overview

- Collections often need to be processed element by element.
- A common use case is **iterating** over all items in a collection to perform operations on them.

---

## Adding a Method to List All Files

### Example: Writing the Method
We add a new method to list all files in the `MusicOrganiser` class:

```java
public void listAllFiles() { 
    for (String file : files) {
        System.out.println(file); 
    } 
}
```


### Explanation:
1. **`for` Loop Syntax**:
   - `for (String file : files)`:
     - **`file`**: Local variable that refers to the current file in the collection.
     - **`files`**: The `ArrayList<String>` being iterated over.
   - The colon `:` can be read as "in," indicating that we loop through all elements in `files`.
   
2. **Printing Each File**:
   - `System.out.println(file)` prints the current file to the console.

---

## Debugging the Method

### Debugging Steps:
1. **Set a Breakpoint**:
   - Click in the left-hand margin of the code editor to set a breakpoint on the line inside the loop.
   
2. **Step Through Execution**:
   - Use the debugger to step through the code.
   - Observe:
     - The local variable `file` updating with each iteration.
     - Execution returning to the top of the loop for the next element.

### Debugging Example:
- For the list of files:

"1.mp3", "2.mp3", "3.mp3"

- First iteration: `file = "1.mp3"`.
- Second iteration: `file = "2.mp3"`.
- Third iteration: `file = "3.mp3"`.
- At the end of the loop, execution realizes there are no more files and exits the method.

---

## Example Usage

### Adding and Listing Files:

```java
MusicOrganiser organiser = new MusicOrganiser(); 
organiser.addFile("1.mp3"); 
organiser.addFile("2.mp3"); 
organiser.addFile("3.mp3"); 
organiser.listAllFiles();
```

### Output:

`1.mp3 2.mp3 3.mp3`

---

## Summary

- **Iteration**:
  - Use the `for-each` loop for simple iteration over collections.
- **Debugging**:
  - Set breakpoints and step through the loop to observe variable updates.
- **Applications**:
  - Listing all elements in a collection.
  - Performing operations on each item in a collection.
