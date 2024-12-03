# Processing collections indefinitely (the while loop)

## Overview
- Indefinite iteration refers to loops where the number of iterations is not predetermined.
- Example: Searching for a file in a collection using a `while` loop.
  - The loop may terminate immediately upon finding the file or traverse the entire collection.

---

## Adding a Search Method

### Method Definition
We add a method to check whether a song exists in the `MusicOrganiser` collection:

```java
public boolean containsSong(String song) { 
    boolean searching = true; // Initially searching 
    int index = 0; // Start from the beginning of the list
    
    // Continue searching while still searching and index is within bounds
    while (searching && index < files.size()) {
        String fileName = files.get(index); // Get the current file name
        if (fileName.equals(song)) { // Check if the file matches the search string
            searching = false; // Stop searching if found
        }
        index++; // Move to the next index
    }

    // Return true if the file was found (not searching anymore), otherwise false
    return !searching;
}
```

---

### Explanation
1. **Variables**:
   - `searching`: Boolean flag indicating whether the search is ongoing.
   - `index`: Tracks the current position in the collection.

2. **Loop**:
   - `while (searching && index < files.size())`: 
     - Ensures the loop stops if the file is found (`searching = false`) or all files have been checked (`index >= files.size()`).

3. **Condition**:
   - `fileName.equals(song)`: Compares the current file with the target song using the `String.equals` method.

4. **Return**:
   - `return !searching`: Returns `true` if the search ended successfully, otherwise `false`.

---

## Example Usage

### Adding Files and Searching

```java
MusicOrganiser organiser = new MusicOrganiser(); 
organiser.addFile("1.mp3"); 
organiser.addFile("2.mp3"); 
organiser.addFile("3.mp3");

// Check if files exist 
boolean result1 = organiser.containsSong("2.mp3"); // Returns true 
boolean result2 = organiser.containsSong("4.mp3"); // Returns false
```


---

## Debugging the Method

### Step-by-Step Execution
1. **Setup**:
   - Add files: `1.mp3`, `2.mp3`, `3.mp3`.
   - Search for: `"2.mp3"`.

2. **Iteration**:
   - **Iteration 1**:
     - `index = 0`, `fileName = "1.mp3"`, `searching = true`.
   - **Iteration 2**:
     - `index = 1`, `fileName = "2.mp3"`, `searching = false`.
   - **Exit Loop**:
     - Search stops as the file is found.

3. **Result**:
   - `!searching` evaluates to `true`, indicating the file was found.

---

## Fixing Edge Cases

### Case: Search Beyond Array Bounds
Initial implementation:
- Fails to stop searching when `index >= files.size()`.

**Fix**:
Add a boundary check:

```java
while (searching && index < files.size()) {
```


### Testing Edge Cases
1. **Empty Collection**:
   - Search for any file returns `false`.
2. **Valid File**:
   - Search for `"2.mp3"` in `["1.mp3", "2.mp3", "3.mp3"]` returns `true`.
3. **Invalid File**:
   - Search for `"4.mp3"` in `["1.mp3", "2.mp3", "3.mp3"]` returns `false`.

---

## Summary

### Key Points
- Use a `while` loop for indefinite iteration.
- Combine boolean flags with boundary checks to avoid errors.
- Ensure edge cases (e.g., empty collections, missing files) are handled.

### Applications
- Efficiently search collections or perform operations without knowing the exact number of iterations in advance.
