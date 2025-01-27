

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

/**
 * Unit tests for the {@link LibraryGuest} class.<p>
 * 
 * Tests constructor validation and the {@code getAccessDuration} method.<p>
 * 
 * @author Neil Hutton
 * @version 1.0
 */
public class LibraryGuestTest
{
    /**
     * Tests that the constructor sets the access duration correctly when a valid duration (1-3 days) is provided.
     */
    @Test
    public void testConstructorWithValidDuration(){
       LibraryGuest guest = new LibraryGuest(2);
       assertEquals(2, guest.getAccessDuration(), "Access duration should be set correctly for valid input.");
    }
    
    /**
     * Tests that the constructor throws an exception when the access duration exceeds 3 days.
     */
    @Test
    public void testConstructorWithInvalidDurationAboveRange(){
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            new LibraryGuest(4);
        });
        assertEquals("Access duration must be between 1 and 3 days.", exception.getMessage(),
            "Constructor should throw an exception for access duration above the valid range.");
    }
    
    /**
     * Tests that the constructor throws an exception when the access duration is positive but less than 1 day.
     */
    @Test
    public void testConstructorWithInvalidDurationZero(){
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            new LibraryGuest(0);
        });
        assertEquals("Access duration must be between 1 and 3 days.", exception.getMessage(),
            "Constructor should throw an exception for access duration above the valid range.");
    }
    
    /**
     * Tests that the constructor throws an exception when the access duration is negative.
     */
    @Test
    public void testConstructorWithInvalidDurationNegative(){
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            new LibraryGuest(-1);
        });
        assertEquals("Access duration must be between 1 and 3 days.", exception.getMessage(),
            "Constructor should throw an exception for access duration above the valid range.");
    }
    
    /**
     * Tests that the constructor works correctly with the minimum valid access duration (1 day).
     */
    public void testConstructorWithMinimumValidDuration(){
        LibraryGuest guest = new LibraryGuest(1);
        assertEquals(1, guest.getAccessDuration(), "Access duration should be set to 1 for minimum valid input."); 
    }
    
    /**
     * Tests that the constructor works correctly with the maximum valid access duration (3 days).
     */
    public void testConstructorWithMaximumValidDuration(){
        LibraryGuest guest = new LibraryGuest(3);
        assertEquals(3, guest.getAccessDuration(), "Access duration should be set to 3 for maximum valid input."); 
    }
}
