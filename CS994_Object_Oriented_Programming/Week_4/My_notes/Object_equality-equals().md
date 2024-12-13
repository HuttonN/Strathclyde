# Object equality - equals()

## Overview
Equality in Java can be categorized into two main types:
1. **Reference Equality**:
   - Two variables refer to the same object in memory.
2. **Content Equality**:
   - Two objects may be different instances but have identical data.

---

## Reference Equality

- **Definition**:
  Two variables are reference-equal if they point to the same object.

- **Implementation**:
  The `==` operator checks reference equality.
    
    ```java
    if (v1 == v2) { // True if v1 and v2 refer to the same object. }
    ```

- **Example**:

```java
String s1 = "Hello"; 
String s2 = s1; // s1 and s2 refer to the same object. 
System.out.println(s1 == s2); // Outputs: true
```

---

## Content Equality

- **Definition**:
Two objects have the same values in their fields.

- **Implementation**:
The `.equals` method is used for content equality.

- **Default Behavior**:
- The `equals` method in the `Object` class checks reference equality by default.

```java
public boolean equals(Object obj) {
    return (this == obj); 
}
```

- **Limitation**:
This default behavior does not compare the contents of the objects.

---

## Overriding `equals`

To achieve content equality, the `equals` method needs to be overridden in custom classes.

### Example: Student Class

#### Step-by-Step Implementation

1. **Keep the Same Method Signature**:
    ```java
    @Override public boolean equals(Object obj) {
    ```
    
2. **Check Reference Equality**:
    ```java
    if (this == obj) { 
        return true; // They refer to the same object. 
    }
    ```

3. **Check for Correct Type**:
    ```java
    if (!(obj instanceof Student)) { 
        return false; // The object is not a Student. 
    }
    ```
    
4. **Cast Object**:
    ```java
    Student other = (Student) obj;
    ```
    
5. **Check Field Equality**:
    ```java
    return this.name.equals(other.name) && this.id.equals(other.id) && this.credits == other.credits;
    ```
    
#### Full Implementation

```java
@Override public boolean equals(Object obj) { 
    if (this == obj) { 
        return true; // Same object reference. 
    } 
    if (!(obj instanceof Student)) { 
        return false; // Not the same type. 
    } 
    Student other = (Student) obj; 
    return this.name.equals(other.name) && this.id.equals(other.id) && this.credits == other.credits; 
}
```

---

## Key Points to Note

1. **String Comparison**:
   - Use `.equals` to compare strings for content equality:
     ```
     if (this.name.equals(other.name)) { ... }
     ```

2. **Field Selection**:
   - Not all fields may need to be compared. For example:
     - **Unique Identifiers** (e.g., ID) might suffice for equality checks.

3. **Direct Access**:
   - Fields can be accessed directly within the class without using accessors.

4. **Importance of `@Override`**:
   - Using `@Override` ensures the method correctly overrides the `equals` method in `Object`.

---

## Example Usage

### Code

```java
Student s1 = new Student("Alice", "123", 30); 
Student s2 = new Student("Alice", "123", 30);
System.out.println(s1.equals(s2)); // Outputs: true
```

### Explanation
- `s1` and `s2` are different instances but have identical content, so `equals` returns `true`.

---

## Summary

- **Reference Equality**:
  - Use `==` to check if two variables refer to the same object.

- **Content Equality**:
  - Override `equals` to compare the contents of objects.

- **Steps to Override `equals`**:
  - Check reference equality.
  - Verify the object's type.
  - Cast and compare relevant fields.

- **Custom Equality Logic**:
  - Tailor the `equals` method to suit the needs of the class.

By following these steps, you can define meaningful equality checks for your custom classes.
