# Library classes, object structures with collections, and generic classes

In this video, we explore how Java libraries, collections, and generics are used to manage and manipulate groups of objects, focusing on the **ArrayList** class.

---

## Importing Libraries

- **`import`**: A keyword in Java to include libraries in our code.
- Example:
    ```java
    import java.util.ArrayList;
    ```

# Working with `java.util.ArrayList`

## Overview

- **`java.util.ArrayList`**: Part of the Java core library for managing dynamic collections.

---

## Using `ArrayList`

### Declaring an `ArrayList`

```java
private ArrayList<String> files;
```

- **`ArrayList<String>`**: A generic class.
  - **Generic Type**: `String` specifies that this `ArrayList` will hold `String` objects.

### Initializing the `ArrayList`

```java
files = new ArrayList<>();
```

- **Diamond Notation (`<>`)**: The compiler infers the generic type (`String`) based on the declaration.

---

## Key Methods in the Music Organiser

### Adding a File

```java
public void addFile(String fileName) { 
    files.add(fileName); 
}
```

- **Purpose**: Adds a file (song) to the collection.

### Getting the Number of Files

```java
public int getNumberOfFiles() { 
    return files.size(); 
}
```

- **Purpose**: Returns the number of items in the `ArrayList`.

### Listing a File by Index

```java
public String listFile(int index) { 
    return files.get(index); 
}
```

- **Purpose**: Retrieves a file at a specified index.

---

## Example Usage

### Creating an Instance

```java
MusicOrganiser organiser = new MusicOrganiser();
```

### Adding Files

```java
organiser.addFile("1.mp3"); 
organiser.addFile("2.mp3"); 
organiser.addFile("3.mp3");
```

### Getting the Number of Files

```java
int numberOfFiles = organiser.getNumberOfFiles(); // Returns 3
```

### Listing a File

```java
String file = organiser.listFile(1); // Returns "2.mp3" (indexing starts at 0)
```

---

## Inspecting the `ArrayList`

### Key Details in Inspector:
1. **ArrayList Size**:
   - Example: `3` (after adding 3 files).
2. **Internal Array (`elementData`)**:
   - Example: The internal array may have a capacity of 10, even if only 3 slots are used.
   - Automatically resizes when more space is needed.

---

## Summary

### Libraries
- Use **`import`** to include pre-built libraries like `ArrayList`.

### Collections
- **`ArrayList`** provides dynamic storage for objects.
- Automatically resizes when capacity is exceeded.

### Generics
- Specify the type of objects in the collection (e.g., `String`).

Using these tools, you can efficiently manage collections of objects, such as songs in a music organiser.
