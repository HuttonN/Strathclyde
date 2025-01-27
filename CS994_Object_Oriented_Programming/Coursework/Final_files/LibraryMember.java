import java.util.List;
import java.util.ArrayList;
/**
 * Represents a library member who can borrow and return physical books.<p>
 * 
 * Each library member has a unique ID and a list of borrowed books.<p>
 * 
 * Provides methods for borrowing, returning, and viewing borrowed books.<p>
 * 
 * <b>Version 1.1 Notes:</b><br>
 * - Added the {@code getDetails} method to generate member details as a String.<br>
 * - Modified the {@code printDetails} method to use {@code getDetails} for better testability<br>
 * 
 * 
 * @author Neil Hutton
 * @version 1.1
 */
public class LibraryMember {
    private int id;
    private List<PhysicalBook> borrowedBooks;

    /**
     * Constructs a new LibraryMember with the specified ID.
     * 
     * @param id the unique ID of the library member
     */
    public LibraryMember(int id) {
        this.id = id;
        this.borrowedBooks = new ArrayList<>();
    }

    /**
     * Gets the ID of the library member.
     * 
     * @return the ID of the library member
     */
    public int getId() {
        return id;
    }
    
    /**
     * Sets the ID of the library member.
     * 
     * @param id the new ID of the library member
     */
    public void setId(int id) {
        this.id = id;
    }
    
    /**
     * Gets the list of books currently borrowed by the library member.
     * 
     * @return a copy of the list of borrowed books for immutability
     */
    public List<PhysicalBook> getBorrowedBooks() {
        return new ArrayList<>(borrowedBooks);
    }
    
    /**
     * Adds the specified book to the member's list of borrowed books.<p>
     * 
     * This method does not handle broader lending logic, such as checking whether 
     * the book is already borrowed by another member or is available in the library. Such 
     * validation is performed by the {@link Library#lendBook} method.<p>
     * 
     * This method only ensures that the book is added to the list if it is not already present.<p>
     * 
     * @param book the book to add to the borrowed books list
     */
    public void addBorrowedBook(PhysicalBook book){
        if (borrowedBooks.contains(book)){
            System.out.println("Error: Book is already borrowed by this member");
            return;
        } 
        
        borrowedBooks.add(book);
        System.out.println("Book '" + book.getTitle() + "' successfully borrowed by Member ID: " + id);
    }
    
    /**
     * Removes the specified book from the member's list of borrowed books.<p>
     * 
     * This method does not validate whether the book is being returned to the library 
     * or if it belongs to this library's catalog. Such logic is handled in the 
     * {@link Library#acceptBookReturn} method.<p>
     * 
     * This method only ensures that the book is removed from the list if it is currently present.
     * 
     * @param book the book to remove from the borrowed books list
     */
    public void removeBook(PhysicalBook book){
        if (borrowedBooks.contains(book)){
            borrowedBooks.remove(book);
            System.out.println("Book '" + book.getTitle() + "' removed from Library Member ID: " + id + "'s borrowed books.");
        } else {
            System.out.println("Error: Book '" + book.getTitle() + "' is not in Library Member ID: " + id + "'s borrowed books.");
        }
    }
    
    /**
     * Gets the number of books currently borrowed by the library member.
     * 
     * @return the number of borrowed books
     */
    public int numberOfBorrowedBooks(){
        return borrowedBooks.size();
    }
    
    /**
     * Generates a string containing the details of the library member.
     * 
     * @return a string representation of the library member's details
     */
    public String getDetails(){
        String details = "Library Member ID: " + id + "\n";
        
        if (borrowedBooks.isEmpty()) {
            details += "Borrowed Books: None";
        } else {
            details += "Borrowed Books:\n";
            for (PhysicalBook book : borrowedBooks){
                details += book.getDetails() + "\n";
            }
        }
        return details;
    }
    
    /**
     * Prints the details of the library member to the console.
     */
    public void printDetails(){
        System.out.println(getDetails());
    }
}
