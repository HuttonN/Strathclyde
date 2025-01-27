import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.util.ArrayList;
import java.util.List;

/**
 * Unit tests for the {@link LibraryMember} class.<p>
 * 
 * Tests the functionality of the constructor, getter, setter, and methods related to managing 
 * borrowed books, such as adding to and returning from the borrowed books list. Also tests 
 * the {@code getDetails} and {@code printDetails} methods.<p>
 * 
 * @author Neil Hutton
 * @version 1.0
 */
public class LibraryMemberTest {
    
    private LibraryMember member1;
    private PhysicalBook book1;
    private PhysicalBook book2;

    @BeforeEach
    public void setUp() {
        member1 = new LibraryMember(101);
        Author author = new Author("Jane", "Doe", "123 Main St");
        book1 = new PhysicalBook("Book Title 1", "123456789", author);
        book2 = new PhysicalBook("Book Title 2", "987654321", author);
    }

    /**
     * Tests the constructor and {@code getId} method.
     */
    @Test
    public void testConstructorAndGetId() {
        assertEquals(101, member1.getId(), "ID should match the constructor's input.");
    }
    
    /**
     * Tests the {@code setId} method.
     */
    @Test
    public void testSetId() {
        member1.setId(202);
        assertEquals(202, member1.getId(), "ID should be updated.");
    }
    
    /**
     * Tests adding a book to the list of borrowed books using {@code addBorrowedBook}.
     */
    @Test
    public void testAddBorrowedBook() {
        member1.addBorrowedBook(book1);
        assertTrue(member1.getBorrowedBooks().contains(book1), "Book should be in the list of borrowed books.");
    }
    
    /**
     * Tests adding the same book to the borrowed list twice.
     */
    @Test
    public void testAddBorrowedBookDuplicate() {
        member1.addBorrowedBook(book1);
        member1.addBorrowedBook(book1); // Attempt to add the same book again
        assertEquals(1, member1.getBorrowedBooks().size(), "Duplicate additions should not occur.");
    }

    /**
     * Tests returning a book that has been borrowed.
     */
    @Test
    public void testReturnBook() {
        member1.addBorrowedBook(book1);
        member1.removeBook(book1);
        assertFalse(member1.getBorrowedBooks().contains(book1), "Returned book should no longer be in the list.");
    }
    
    /**
     * Tests returning a book that has not been borrowed.
     */
    @Test
    public void testReturnBookNotBorrowed() {
        member1.removeBook(book1); // Attempt to return a book not in the borrowed list
        assertFalse(member1.getBorrowedBooks().contains(book1), "Unborrowed book should not be in the list.");
    }
    
    /**
     * Tests the {@code numberOfBorrowedBooks} method.
     */
    @Test
    public void testNumberOfBorrowedBooks() {
        assertEquals(0, member1.numberOfBorrowedBooks(), "New member should have zero borrowed books.");
        member1.addBorrowedBook(book1);
        member1.addBorrowedBook(book2);
        assertEquals(2, member1.numberOfBorrowedBooks(), "Borrowed books count should reflect the number of books added.");
    }
    
    /**
     * Tests the {@code getDetails} method for a member with no borrowed books.
     */
    @Test
    public void testGetDetailsNoBooks() {
        String expectedDetails = "Library Member ID: 101\nBorrowed Books: None";
        assertEquals(expectedDetails, member1.getDetails(), "Details should correctly show no borrowed books.");
    }
    
    /**
     * Tests the {@code getDetails} method for a member with borrowed books.
     */
    @Test
    public void testGetDetailsWithBooks() {
        member1.addBorrowedBook(book1);
        member1.addBorrowedBook(book2);

        String expectedDetails = "Library Member ID: 101\n" +
                                 "Borrowed Books:\n" +
                                 "Title: Book Title 1\n" +
                                 "ISBN: 123456789\n" +
                                 "Author Details:\n" +
                                 "First Name: Jane\n" +
                                 "Surname: Doe\n" +
                                 "Address: 123 Main St\n" +
                                 "Available: Yes\n" +
                                 "Damages: None\n" +
                                 "Title: Book Title 2\n" +
                                 "ISBN: 987654321\n" +
                                 "Author Details:\n" +
                                 "First Name: Jane\n" +
                                 "Surname: Doe\n" +
                                 "Address: 123 Main St\n" +
                                 "Available: Yes\n" +
                                 "Damages: None\n";

        assertEquals(expectedDetails, member1.getDetails(), "Details should include borrowed books.");
    }
}
