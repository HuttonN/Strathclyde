# Summary of for-each

In this section, we'll explore the mechanics of the `for-each` loop in Java, which provides a concise way to iterate over a collection. Despite its simplicity, the `for-each` loop can sometimes be confusing for beginners.

---

## Anatomy of a For-Each Loop

### Components:
1. **Type of Element**: Specifies the data type of each element in the collection.
2. **Element Name**: A variable used to refer to the current element in the iteration.
3. **Collection**: The data structure being iterated over.
4. **Loop Body**: Contains the operations to be performed on each element.

---

## Example: Iterating Over an ArrayList of File Names

### Scenario:
We have an `ArrayList` of file names (of type `String`), and we want to print each file name.

### Code Example:

```java
ArrayList<String> fileNames = new ArrayList<>(); 
fileNames.add("file1.txt"); 
fileNames.add("file2.txt"); 
fileNames.add("file3.txt");

for (String name : fileNames) { 
    System.out.println(name); 
}
```

---

### Explanation:

1. **Element Type**:
   - Each file name in the `ArrayList` is a `String`.

2. **Element Name**:
   - `name` is the variable used to refer to each file name in the loop.

3. **Collection**:
   - `fileNames` is the collection being iterated over.

4. **Loop Body**:
   - The statement `System.out.println(name)` prints the current file name to the console.

---

### Output:

```
file1.txt 
file2.txt 
file3.txt
```

---

## Key Points

1. **Collection and Element Type**:
   - Ensure the element type matches the type of objects in the collection.

2. **Conciseness**:
   - The `for-each` loop removes the need for manual indexing, making the code cleaner and less error-prone.

3. **Custom Element Name**:
   - You can use any valid variable name for the element reference (`name` in this example).

---

### Conclusion:
The `for-each` loop is an efficient and elegant way to iterate over collections in Java. By understanding its components and structure, you can use it effectively to write cleaner, more maintainable code.
