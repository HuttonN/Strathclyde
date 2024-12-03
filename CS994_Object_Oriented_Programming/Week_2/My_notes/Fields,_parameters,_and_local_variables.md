# Fields, Parameters, and Local Variables

In this video, we explore the differences between **fields**, **parameters**, and **local variables** in Java. Each is used to store data, but their roles and scope differ significantly.

---

## 1. Fields

- **Definition**:
  - Fields (also called instance variables) store data within an object.
  - They represent the state of the object.

- **Characteristics**:
  - Accessible by all methods within the object.
  - Their values vary depending on the object instance.

- **Example**: Fields in a Ticket Machine
    ```java
    private int price; // Stores the ticket price 
    private int balance; // Stores the current balance
    ```

- **Usage**:
  - Fields capture the state of the object.
  - In methods, fields can be referenced directly:
        ```java
        if (balance > 0) { 
            System.out.println("Balance is: " + balance); 
        }
        ```

---

## 2. Parameters

- **Definition**:
  - Parameters pass values to methods or objects.
  - They act as temporary placeholders for input data when a method is called.

- **Characteristics**:
  - Declared in the method signature.
  - Only accessible within the method where they are defined.

- **Example**: `amount` Parameter in `insertMoney` Method
    ```java
    public void insertMoney(int amount) { 
        if (amount > 0) { 
            balance = balance + amount; // Updates the balance field using the parameter 
        } else { 
            System.out.println("Invalid amount entered."); 
        } 
    }
    ```

- **Usage**:
  - The parameter `amount` is provided when calling `insertMoney` (e.g., `insertMoney(50)`).
  - It is only accessible within the `insertMoney` method.

---

## 3. Local Variables

- **Definition**:
  - Local variables are declared and used within a method for temporary computations.

- **Characteristics**:
  - Only exist during the execution of the method.
  - Cannot be accessed outside the method.

- **Example**: `amountToRefund` in `refundBalance` Method
    ```java
    public void refundBalance() { 
        int amountToRefund = balance; // Local variable stores the balance temporarily 
        balance = 0; // Resets the balance field 
        System.out.println("Refunded: " + amountToRefund); 
    }
    ```
 
- **Usage**:
  - Local variables are used for intermediate calculations.
  - They do not persist after the method finishes execution.

---

## Key Differences

| **Feature**        | **Fields**                          | **Parameters**                  | **Local Variables**            |
|---------------------|-------------------------------------|----------------------------------|---------------------------------|
| **Purpose**         | Capture the object's state.         | Pass data to methods or objects. | Perform temporary calculations. |
| **Scope**           | Visible to all methods in the class.| Limited to the method body.      | Limited to the method body.     |
| **Declaration**     | Declared at the class level.        | Declared in method signature.    | Declared within method body.    |
| **Lifetime**        | Exists as long as the object exists.| Exists during method execution.  | Exists during method execution. |

---

## Summary

- **Fields**:
  - Represent the state of the object.
  - Should only be used for essential variables that describe the object.

- **Parameters**:
  - Temporarily hold input data for a method.
  - Not visible outside the method they belong to.

- **Local Variables**:
  - Provide temporary storage for computations within a method.
  - Avoid using local variables as fields unless they are essential for the object's state.

By understanding these distinctions, you can write cleaner and more efficient Java code.
   