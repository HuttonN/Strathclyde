# Local Variables

In this video, we explore the concept of **local variables** in Java, which are used for temporary storage within methods.

---

## What are Local Variables?

- **Definition**:
  - Local variables are variables declared within a method.
  - They are used for temporary storage during method computations.

- **Key Characteristics**:
  - Exist only within the scope of the method where they are declared.
  - Can only be accessed by code inside that method.
  - Do not require access modifiers (e.g., `public`, `private`) since they are inherently restricted to the method.

---

## Example: `refundBalance` Method

The `refundBalance` method uses a **local variable** to temporarily store the value of the ticket machine’s balance.

### Code:

```java
public void refundBalance() { 
    int amountToRefund = balance; // Local variable to hold balance 
    balance = 0; // Reset the balance field 
    System.out.println("Refunded: " + amountToRefund); }
```


### Explanation:
1. **Local Variable: `amountToRefund`**:
   - Declared inside the method.
   - Temporarily holds the value of `balance`.
   - Exists only during the execution of this method.
   - Inaccessible to other methods or code outside this method.

2. **Field: `balance`**:
   - A class-level field accessible to all methods in the class.
   - Represents the state of the object.
   - Modified by the `refundBalance` method to reset the balance to 0.

---

## Differences Between Fields and Local Variables

| **Feature**          | **Fields**                           | **Local Variables**                 |
|-----------------------|---------------------------------------|--------------------------------------|
| **Scope**             | Visible to all methods in the class. | Limited to the method in which they are declared. |
| **Purpose**           | Capture the object's state.          | Temporary storage for method computations. |
| **Declaration**       | Requires access modifiers (`public`, `private`, etc.). | No access modifiers needed. |
| **Lifetime**          | Exists as long as the object exists. | Exists only during method execution. |

---

## Best Practices for Using Variables

1. **Use Local Variables for Temporary Storage**:
   - Declare variables as local if they are only needed for a specific computation within a method.
   - Avoid declaring temporary variables as fields.

2. **Use Fields Sparingly**:
   - Fields should represent the object's state and only be used when necessary.

3. **Avoid Overusing Fields**:
   - Declaring too many fields can lead to unnecessary complexity and reduced clarity.

---

## Summary

- **Local Variables**:
  - Used for temporary computations within methods.
  - Limited in scope and lifetime to the method in which they are declared.

- **Fields**:
  - Represent the object's state and are accessible across methods in the class.

- **Best Practices**:
  - Use fields for capturing the object's state.
  - Use local variables for temporary data to keep your code clean and efficient.

By distinguishing between fields and local variables and following best practices, you can write clear, maintainable Java code.
