# Object equality - hashCode()

## Why Override `hashCode`?

- **Purpose**:
  The `hashCode` method generates a unique integer for an object, used in data structures like `HashSet` and `HashMap`.
  
- **Relation to `equals`**:
  - If two objects are equal (as defined by `equals`), they **must** have the same `hashCode`.
  - However, objects with the same `hashCode` **may** or **may not** be equal.

---

## Rules for `hashCode`

1. **Consistency with `equals`**:
   - Objects that are equal according to `equals` must have identical hash codes.
2. **Consistency**:
   - For a single object, `hashCode` must consistently return the same value during its lifetime unless its fields are modified.
3. **High Distribution**:
   - The hash codes should be well-distributed to minimize collisions in hash-based collections.

---

## Generating a `hashCode`

To ensure consistency with `equals`, the `hashCode` must use the same fields involved in the equality check.

### Example: Student Class

#### Fields Used:
- `credits`
- `name`
- `id`

#### Steps to Compute `hashCode`

1. **Start with an Initial Value**:
    ```java
    int result = 17;
    ```

2. **Incorporate Each Field**:
- Multiply `result` by a prime number and add the field's hash code or value.
    ```java
    result = 31 * result + credits; 
    result = 31 * result + (name != null ? name.hashCode() : 0); 
    result = 31 * result + (id != null ? id.hashCode() : 0);
    ```

3. **Return the Final Result**:
    ```java
    return result;
    ```

#### Full Implementation

```java
@Override public int hashCode() { 
int result = 17; // Initial value 
result = 31 * result + credits; // Add credits 
result = 31 * result + (name != null ? name.hashCode() : 0); // Add name's hashCode 
result = 31 * result + (id != null ? id.hashCode() : 0); // Add id's hashCode 
return result; // Return final hashCode 
}
```
---

## Why Prime Numbers?

- Prime numbers (e.g., 31, 37) reduce the likelihood of collisions.
- They help spread the hash codes more evenly across a range.

---

## Important Notes

1. **Match Fields in `equals` and `hashCode`**:
   - Use the same fields in both methods to maintain consistency.
   
2. **Include Null Checks**:
   - For fields like `String` or `Object`, ensure to check for `null` before calling `hashCode`.

3. **Use IDEs or Libraries**:
   - Many IDEs can auto-generate `equals` and `hashCode` implementations.
   - Libraries like Apache Commons or Guava provide utilities for these methods.

---

## Example Usage

### Code

```java
Student s1 = new Student("Alice", "123", 30); 
Student s2 = new Student("Alice", "123", 30);
HashSet<Student> set = new HashSet<>(); 
set.add(s1); 
System.out.println(set.contains(s2)); // Outputs: true
```

### Explanation
- Even though `s1` and `s2` are different instances, their consistent `equals` and `hashCode` implementations ensure they behave as expected in hash-based collections.

---

## Summary

- Always override `hashCode` if you override `equals`.
- Use the same fields in both methods to ensure consistency.
- Leverage prime numbers and well-distributed calculations for efficient hash codes.
