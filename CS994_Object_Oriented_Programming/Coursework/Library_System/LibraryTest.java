

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.util.ArrayList;

/**
 * Unit tests for the {@link Library} class.
 * 
 * Tests the functionality of managing the library catalogue, including adding, searching,
 * lending, returning, and removing resources.
 * 
 * @author Neil Hutton
 * @version 1.0
 */
public class LibraryTest {
        
        private Library library;
        private PhysicalBook book1;
        private PhysicalBook book2;
        private ElectronicResource eResource;
        private LibraryMember member1;
        private LibraryMember member2;

    @BeforeEach
    public void setUp() {
        library = new Library();
        Author author = new Author("Jane", "Doe", "123 Main St");
        book1 = new PhysicalBook("Book1", "123456789", author);
        book2 = new PhysicalBook("Book2", "987654321", author);
        eResource = new ElectronicResource("E-resource", true);
        member1 = new LibraryMember(101);
        member2 = new LibraryMember(102);
    }

    /**
     * Tests adding a resource to the library catalogue.
     */
    @Test
    public void testAddResource() {
        library.addResource(book1);
        assertTrue(library.containsResource(book1), "Book1 should be in the catalogue.");
        library.addResource(book1); // Attempt to add a duplicate
        assertEquals(1, library.getResourceCount(), "Duplicate resource should not be added.");
    }

    /**
     * Tests searching for a resource by title.
     */
    @Test
    public void testSearchByTitle() {
        library.addResource(book1);
        library.addResource(book2);
        library.addResource(eResource);

        library.searchByTitle("Book1"); // Should find book1
        library.searchByTitle("Book Non-Existent"); // Should find none
    }

    /**
     * Tests searching for a physical book by the author's surname.
     */
    @Test
    public void testSearchByAuthorSurname() {
        library.addResource(book1);
        library.addResource(book2);

        library.searchByAuthorSurname("Doe"); // Should find book1 and book2
        library.searchByAuthorSurname("Smith"); // Should find none
    }

    /**
     * Tests editing an author's first name for a physical book.
     */
    @Test
    public void testEditAuthorFirstName() {
        library.addResource(book1);
        library.editAuthorFirstName(book1, "John");
        assertEquals("John", book1.getAuthor().getFirstName(), "Author's first name should be updated.");
    }

    /**
     * Tests lending a physical book to a library member.
     */
    @Test
    public void testLendBook() {
        library.addResource(book1);
        library.lendBook(book1, member1);
        assertEquals(member1, book1.getLibraryMember(), "Book should be linked to the borrowing member.");
        assertTrue(member1.getBorrowedBooks().contains(book1), "Book should be in the member's borrowed list.");

        library.lendBook(book1, member2); // Attempt to lend the book again
        assertEquals(member1, book1.getLibraryMember(), "Book should remain with the original borrower.");
    }

    /**
     * Tests accepting a physical book return.
     */
    @Test
    public void testAcceptBookReturn() {
        library.addResource(book1);
        library.lendBook(book1, member1);

        library.acceptBookReturn(book1, false, null); // No damage
        assertNull(book1.getLibraryMember(), "Book should no longer be linked to a member.");
        assertFalse(member1.getBorrowedBooks().contains(book1), "Book should be removed from the member's borrowed list.");
    }

    /**
     * Tests accepting a book return with damage recorded.
     */
    @Test
    public void testAcceptBookReturnWithDamage() {
        library.addResource(book1);
        library.lendBook(book1, member1);

        library.acceptBookReturn(book1, true, "Cover torn");
        assertTrue(book1.getDamages().contains("Cover torn"), "Damage should be recorded for the book.");
    }

    /**
     * Tests removing a resource from the catalogue.
     */
    @Test
    public void testRemoveResource() {
        library.addResource(book1);
        library.removeResource(book1);
        assertFalse(library.containsResource(book1), "Book1 should be removed from the catalogue.");
    }

    /**
     * Tests removing a resource at a specific position.
     */
    @Test
    public void testRemoveResourceAtPosition() {
        library.addResource(book1);
        library.addResource(book2);

        library.removeResourceAtPosition(0);
        assertFalse(library.containsResource(book1), "Book1 should be removed from the catalogue.");
        assertTrue(library.containsResource(book2), "Book2 should remain in the catalogue.");
    }

    /**
     * Tests getting the total number of resources in the catalogue.
     */
    @Test
    public void testGetResourceCount() {
        assertEquals(0, library.getResourceCount(), "New library should have zero resources.");
        library.addResource(book1);
        library.addResource(book2);
        library.addResource(eResource);
        assertEquals(3, library.getResourceCount(), "Resource count should reflect the number of added resources.");
    }

    /**
     * Tests printing all physical books in the catalogue.
     */
    @Test
    public void testPrintPhysicalBooks() {
        library.addResource(book1);
        library.addResource(book2);
        library.printPhysicalBooks(); // Should print details of book1 and book2
    }

    /**
     * Tests printing all electronic resources in the catalogue.
     */
    @Test
    public void testPrintElectronicResources() {
        library.addResource(eResource);
        library.printElectronicResources(); // Should print details of eResource
    }
}
