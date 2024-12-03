1. Implement  a  class  named  **```TextMessage```**  that  holds  three  data  fields:  the  text message (a ```String```), the sender’s name, and the message’s size in KB (an integer). Write  a  constructor  that  sets  all  data  fields  to  meaningful  default  values.  Include  methods to set and get the values for each data field. 

    ```java
    import java.util.ArrayList;
    
    public class TextMessage {
        // Data fields
        private String message;
        private String senderName;
        private int messageSize;
    
        // Default constructor
        public TextMessage() {
            this.message = "Default Message";
            this.senderName = "Unknown Sender";
            this.messageSize = 1; // Default size in KB
        }

        // Getter and Setter methods
        public String getMessage() {
        return message;
    }

        public void setMessage(String message) {
        this.message = message;
    }

        public String getSenderName() {
        return senderName;
    }

        public void setSenderName(String senderName) {
        this.senderName = senderName;
    }

        public int getMessageSize() {
        return messageSize;
    }

        public void setMessageSize(int messageSize) {
        this.messageSize = messageSize;
    }
    ```

1. Implement  a  second  constructor  in  the  **```TextMessage```**  class  that accepts  three  parameters and uses their values to initialize the respective data fields.

    ```java
    // Parameterized constructor
    public TextMessage(String message, String senderName, int messageSize) {
        this.message = message;
        this.senderName = senderName;
        this.messageSize = messageSize;
    }
    ```

1. Implement a method in the **```TextMessage```** class that prints ALL the details of a **```TextMessage```** object, i.e. the values of all data fields along with some descriptive text.
    
    ```java
    // Method to print details
    public void printDetails() {
        System.out.println("Message: " + message);
        System.out.println("Sender: " + senderName);
        System.out.println("Size: " + messageSize + " KB");
    }
    ```

1. Implement a class named **```TextMessageManager```** that holds an ```ArrayList``` of **```TextMessage```** objects as a data field. Include a method to get (return) the value of the data field. Implement a method that takes a **```TextMessage```** object as a parameter and works according to the following specification:  

    If the list **already** contains the parameter **```TextMessage```** object, the method should **reject** the parameter and **print** the message **“This TextMessage object is already in your collection!”** on the screen **Otherwise**, the method should add the parameter **```TextMessage```** object to the end of the list and **print** the message **“TextMessage object added successfully to your collection!”** on the screen.

    ```java
    public class TextMessageManager {
        // Data field: List of TextMessage objects
        private ArrayList<TextMessage> messages;
    
        // Constructor
        public TextMessageManager() {
            messages = new ArrayList<>();
        }
    
        // Getter for the ArrayList
        public ArrayList<TextMessage> getMessages() {
            return messages;
        }
    
        // Method to add a TextMessage object
        public void addTextMessage(TextMessage newMessage) {
            if (messages.contains(newMessage)) {
                System.out.println("This TextMessage object is already in your collection!");
            } else {
                messages.add(newMessage);
                System.out.println("TextMessage object added successfully to your collection!");
            }
        }
    ```

1. In the **```TextMessageManager```** class, implement a method that takes two parameters: 
    - ```index```: an integer, which represents a position in the ```ArrayList```, and 
    - a **```TextMessage```** object.

    The method works according to the following specification: 
    If the list **already** contains the parameter **```TextMessage```** object, the method should **reject** the parameter and **print** the message **“This TextMessage object is already in your collection!”** on the screen. **Otherwise**, the method should add the parameter **```TextMessage```** object to position ```index``` of the list and **print** the message **“TextMessage object added successfully to your collection!”** on the screen. 
 
    ***What if the value of the ```index``` parameter is not a valid position in the ```ArrayList```? Include the appropriate error checking and error messages.***

    ```java
        // Method to add a TextMessage object at a specific index
        public void addTextMessageAtIndex(int index, TextMessage newMessage) {
            if (messages.contains(newMessage)) {
                System.out.println("This TextMessage object is already in your collection!");
            } else if (index < 0 || index > messages.size()) {
                System.out.println("Error: Invalid index!");
            } else {
                messages.add(index, newMessage);
                System.out.println("TextMessage object added successfully to your collection!");
            }
        }
    ```

1. Implement a method in the **```TextMessageManager```** class that takes no parameters and works according to the following specification: The method **returns** ```true``` if the ```ArrayList``` is empty. Otherwise, it returns ```false```. 

    ```java
        // Method to check if the list is empty
        public boolean isEmpty() {
            return messages.isEmpty();
        }
    ```


1. Implement a method in the **```TextMessageManager```** class that prints  **ALL** the details of **ALL ```TextMessage```** objects in the list. Your  implementation **must use a while loop**.  
 
    ***What if the ```ArrayList``` is empty? Include the appropriate checking and messages.***

    ```java
        // Method to print details of all TextMessage objects
        public void printAllMessages() {
            if (messages.isEmpty()) {
                System.out.println("The collection is empty.");
            } else {
                int index = 0;
                while (index < messages.size()) {
                    System.out.println("Message " + (index + 1) + ":");
                    messages.get(index).printDetails();
                    index++;
                }
            }
        }
    ```

1. Implement a method in the **```TextMessageManager```** class that takes one parameter: a search string. The method works according to the following specification: it prints **ALL** the details of **ALL ```TextMessage```** objects in the list with a sender’s name **equal** to the search string **OR** with  a size of **less than** 100 KB. Your implementation **must use a for-each loop**.

    ```java
        public void searchMessages(String searchString) {
            boolean found = false;
            for (TextMessage message : messages) {
                if (message.getSenderName().equals(searchString) || message.getMessageSize() < 100) {
                    message.printDetails();
                    found = true;
                }
            }
            if (!found) {
                System.out.println("No matching messages found.");
            }
        }
    }
    ```

Explanatory notes:

- ```TextMessage``` Class:
    * Default constructor initializes default values.
    * Parameterized constructor initializes with custom values.
    * Getter and setter methods manage the data fields.
    * ```printDetails()``` method prints all the details of a ```TextMessage```.

- ```TextMessageManager``` Class:
    * Maintains an ArrayList of TextMessage objects.
    * Methods to:
        * Add messages, ensuring duplicates are not added.
        * Add a message at a specific index with error handling.
        * Check if the list is empty.
        * Print all messages using a while loop.
        * Search messages by sender name or size using a for-each loop.