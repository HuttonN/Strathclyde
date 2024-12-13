# Examples of basic class design

## Example 1: Librarian Class

### Problem Description
The `Librarian` class should:
- Store the librarian's name and ID.
- Allow the librarian to:
  - Search for a book.
  - Issue a book to a member.
  - Return a book.
- To issue a book, the librarian must first find the member.

### Class Details

#### Attributes
- `name: String`  
  - Visibility: Private (`-`)  
  - Multiplicity: `1` (Exactly one value required).  

- `ID: Integer`  
  - Visibility: Private (`-`)  
  - Multiplicity: `1` (Exactly one value required).  

#### Methods
- `searchBook(name: String): Book`  
  - Purpose: Searches for a book by its name.  
  - Visibility: Public (`+`)  
  - Parameter: Name of the book (`String`).  
  - Returns: An object of type `Book`.

- `issueBook(book: Book, memberID: Integer): void`  
  - Purpose: Issues a book to a member.  
  - Visibility: Public (`+`)  
  - Parameters:  
    - `book`: An object of class `Book`.  
    - `memberID`: The ID of the member (`Integer`).  

- `returnBook(book: Book): void`  
  - Purpose: Returns a book.  
  - Visibility: Public (`+`)  
  - Parameter: An object of class `Book`.

- `findMember(memberID: Integer): Member`  
  - Purpose: Finds a member by their ID.  
  - Visibility: Private (`-`)  
  - Parameter: The ID of the member (`Integer`).  
  - Returns: An object of type `Member`.  

---

## Example 2: Player Class

### Problem Description
The `Player` class should:
- Store the player's username, nickname, cards, and score.  
- Perform the following operations:  
  - Add points.  
  - Reduce points.  
  - Lay down a card.  
  - Draw a card.

### Class Details

#### Attributes
- `username: String`  
  - Visibility: Private (`-`)  
  - Multiplicity: `1` (Exactly one value required).  

- `nickname: String`  
  - Visibility: Private (`-`)  
  - Multiplicity: `0..1` (Optional value).  

- `cards: Card[]`  
  - Visibility: Private (`-`)  
  - Multiplicity: `1..*` (At least one card required).  

- `points: Integer = 0`  
  - Visibility: Private (`-`)  
  - Multiplicity: `1` (Default value: 0).  

#### Methods
- `addPoints(points: Integer): void`  
  - Purpose: Adds points to the player's score.  
  - Visibility: Public (`+`)  
  - Parameter: Points to be added (`Integer`).  

- `reducePoints(points: Integer): void`  
  - Purpose: Reduces points from the player's score.  
  - Visibility: Public (`+`)  
  - Parameter: Points to be reduced (`Integer`).  

- `layDownCard(index: Integer): Card`  
  - Purpose: Lays down a card based on its index in the player's hand.  
  - Visibility: Public (`+`)  
  - Parameter: Index of the card (`Integer`).  
  - Returns: The card that is laid down.  

- `drawCard(card: Card): void`  
  - Purpose: Adds a new card to the player's hand.  
  - Visibility: Public (`+`)  
  - Parameter: The card to be added (`Card`).  

---

## Summary
These examples illustrate the process of defining classes with attributes, methods, and their relationships in UML diagrams. By using attributes, methods, visibility modifiers, and multiplicity, we can clearly represent the functionality and structure of each class.  
