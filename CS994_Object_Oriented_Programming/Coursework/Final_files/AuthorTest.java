import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

/**
 * Unit tests for the {@link Author} class.
 * 
 * Tests the functionality of the constructor, getter, setter, and getDetails methods. Implicitly
 * tests the printDetails method as it just applies System.out.println to the getDetails method.
 *
 * @author  Neil Hutton
 * @version 1.0
 */
public class AuthorTest
{
    private Author author;
    
    @BeforeEach
    public void setUp(){
        author = new Author("Jane", "Doe", "123 Main St");
    }
    
    /**
     * Tests the constructor and getter methods of the Author class.
     */
    @Test
    public void testConstructorAndGetters() {
        assertEquals("Jane", author.getFirstName(), "First name should match the input.");
        assertEquals("Doe", author.getSurname(), "Surname should match the input.");
        assertEquals("123 Main St", author.getAddress(), "Address should match the input.");
    }

    /**
     * Tests the setFirstName method of the Author class
     */
    @Test
    public void testSetFirstName(){
        author.setFirstName("John"); 
        assertEquals("John", author.getFirstName(),"First name should be updated.");
    }
    
    /**
     * Tests the setSurname method of the Author class
     */
    @Test
    public void testSetSurname(){
        author.setSurname("Smith");
        assertEquals("Smith", author.getSurname(),"Surname should be updated.");
    }
    
    /**
     * Tests the setAddress method of the Author class
     */
    @Test
    public void testSetAddress(){
        author.setAddress("456 Main St");
        assertEquals("456 Main St", author.getAddress(),"Address should be updated.");
    }
    
    /**
     * Tests the getDetails method of the Author class
     */
    @Test
    public void testGetDetails(){
        String result = author.getDetails();
        String expected = 
            "Author Details:\n" + 
            "First Name: Jane\n" + 
            "Surname: Doe\n" + 
            "Address: 123 Main St\n" ;
        assertEquals(expected, result, "Generated details should match the expected format.");
    }
}
