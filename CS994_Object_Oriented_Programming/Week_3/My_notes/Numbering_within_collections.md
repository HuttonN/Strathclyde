# Numbering in Collections

## Overview

- Java collections, such as `ArrayList`, always use **0-based indexing**.
- The first element is at index `0`, the second at `1`, and so on.

---

## Working with Indexes in `ArrayList`

### Example: Adding Files
When you add files to an `ArrayList`, they are stored in the order they are added:

```java
organiser.addFile("1.mp3"); 
organiser.addFile("2.mp3"); 
organiser.addFile("3.mp3");
```

The internal indexing will look like this:
- `Index 0`: "1.mp3"
- `Index 1`: "2.mp3"
- `Index 2`: "3.mp3"

### Retrieving Files by Index
To retrieve a file, specify its **index**:

```java
String file = organiser.listFile(1); // Returns "2.mp3"
```

---

## Removing Files

### Example: Removing a File
To remove a file, specify its **index**:

```java
organiser.removeFile(2); // Removes "3.mp3" (at index 2)
```


Key checks in the method:
1. The index must be **greater than or equal to 0**.
2. The index must be **less than the total number of files**.

### Handling Invalid Index
If an invalid index is provided (e.g., `3` when only 3 files exist), no error is thrown, but no action is taken:

```java
organiser.removeFile(3); // No action is taken, no error is thrown
```

---

## Maintaining Order in Collections

### Example: Removing a Middle File
When a file in the middle of the list is removed, the order of the remaining elements is maintained:

```java
organiser.removeFile(1); // Removes "2.mp3" (at index 1)
```

The new indexing becomes:
- `Index 0`: "1.mp3"
- `Index 1`: "3.mp3"

### Adding Files Back
You can re-add files to the `ArrayList`:

```java
organiser.addFile("2.mp3");
```


The file is added to the end of the list.

---

## Summary

- **0-based Indexing**: Collections in Java start indexing at `0`.
- **Order Maintenance**: Removing or adding files preserves the logical order of elements.
- **Boundary Checks**: Methods like `removeFile` ensure the index is within valid bounds to prevent runtime errors.
