import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.List;
import java.util.ArrayList;

/**
 * Unit tests for the {@link PhysicalBook} class.<p>
 * 
 * Tests the functionality of the constructor, getter, setter, {@code isAvailable}, {@code addDamage}, and 
 * {@code getDetails} methods. Implicitly tests the {@code printDetails} method as it just applies {@code System.out.println} 
 * to the {@code getDetails} method.<p>
 * 
 * @author Neil Hutton
 * @version 1.0
 */
public class PhysicalBookTest
{
    private PhysicalBook book;
    private Author author;
    
     /**
     * Tests the constructor and getter methods of the PhysicalBook class.
     */
    @Test
    public void testConstructorAndGetters() {
        author = new Author("Jane", "Doe", "123 Main St");
        book = new PhysicalBook("Book Title", "123456789", author);
        assertEquals("Book Title", book.getTitle(), "Title should match the input.");
        assertEquals("123456789", book.getIsbn(), "ISBN should match the input.");
        assertEquals(author, book.getAuthor(), "Author should match the input.");
        assertTrue(book.isAvailable(), "Book should be available by default.");
        assertEquals(0, book.getDamages().size(), "The book should have no damages by default.");
    }
    
    /**
     * Tests the {@code setIsbn} method of the {@code PhysicalBook} class.
     */
    @Test
    public void testSetIsbn() {
        book = new PhysicalBook("Book Title", "123456789", null);
        book.setIsbn("987654321");
        assertEquals("987654321", book.getIsbn(), "ISBN should be updated.");
    }
    
    /**
     * Tests the {@code setAuthor} method of the {@code PhysicalBook} class.
     */
    @Test
    public void testSetAuthor() {
        book = new PhysicalBook("Book Title", "123456789", null);
        Author newAuthor = new Author("Jane", "Doe", "123 Main St");
        book.setAuthor(newAuthor);
        assertEquals(newAuthor, book.getAuthor(), "Author should be updated.");
    }
    
    /**
     * Tests the {@code addDamage} and {@code getDamages} methods of the {@code PhysicalBook} class.
     */
    @Test
    public void testAddAndGetDamages() {
        book = new PhysicalBook("Book Title", "123456789", null);
        book.addDamage("Spine tear");
        book.addDamage("Ripped page");
        List<String> damages = book.getDamages();
        assertEquals(2, damages.size(), "There should be two recorded damages.");
        assertTrue(damages.contains("Spine tear"), "Damages should include 'Spine tear'.");
        assertTrue(damages.contains("Ripped page"), "Damages should include 'Ripped page'.");
    }

    /**
     * Tests the {@code isAvailable} and {@code setLibraryMember} methods of the {@code PhysicalBook} class.
     */
    @Test
    public void testAvailability() {
        LibraryMember member = new LibraryMember(1);
        book = new PhysicalBook("Book Title", "123456789", null);
        book.setLibraryMember(member);
        assertFalse(book.isAvailable(), "Book should not be available when borrowed.");
        book.setLibraryMember(null);
        assertTrue(book.isAvailable(), "Book should be available when not borrowed.");
    }

    /**
     * Tests the {@code setDamages} method of the {@code PhysicalBook} class.
     */
    @Test
    public void testSetDamages() {
        book = new PhysicalBook("Book Title", "123456789", null);
        List<String> newDamages = new ArrayList<>();
        newDamages.add("Water damage");
        book.setDamages(newDamages);
        assertEquals(1, book.getDamages().size(), "There should be one recorded damage.");
        assertEquals("Water damage", book.getDamages().get(0), "Damages should include 'Water damage'.");
    }

    /**
     * Tests the {@code getDetails} method of the {@code PhysicalBook} class.
     */
    @Test
    public void testGetDetails() {
        author = new Author("Jane", "Doe", "123 Main St");
        book = new PhysicalBook("Book Title", "123456789", author);
        book.addDamage("Ripped page");
        String details = book.getDetails();
        String expectedDetails = 
            "Title: Book Title\n" +
            "ISBN: 123456789\n" +
            "Author Details:\n" +
            "First Name: Jane\n" +
            "Surname: Doe\n" +
            "Address: 123 Main St\n" +
            "Available: Yes\n" +
            "Damages: Ripped page";
        assertEquals(expectedDetails, details, "Generated details should match the expected format.");
    }
}
