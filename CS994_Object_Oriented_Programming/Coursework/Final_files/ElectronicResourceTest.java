import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

/**
 * Unit tests for the {@link ElectronicResource} class.<p>
 * 
 * Tests the functionality of the constructor, getter, setter, and {@code getDetails} methods. Implicitly 
 * tests the {@code printDetails} method as it just applies {@code System.out.println} to the {@code getDetails} method.<p>
 * 
 * @author  Neil Hutton
 * @version 1.0
 */
public class ElectronicResourceTest
{
    /**
     * Tests the constructor and getter methods of the {@code ElectronicResource} class.
     */
    @Test
    public void testConstructorAndGetters() {
        ElectronicResource resource = new ElectronicResource("E-Book Title", true);
        assertEquals("E-Book Title", resource.getTitle(), "Title should match the input.");
        assertTrue(resource.isDownloadable(), "Downloadable status should match the input.");
    }

    /**
     * Tests the {@code isDownloadable} method of the {@code ElectronicResource} class.
     */
    @Test
    public void testIsDownloadable() {
        ElectronicResource downloadableResource = new ElectronicResource("Downloadable Resource", true);
        ElectronicResource nonDownloadableResource = new ElectronicResource("Non-Downloadable Resource", false);

        assertTrue(downloadableResource.isDownloadable(), "isDownloadable should return true for a downloadable resource.");
        assertFalse(nonDownloadableResource.isDownloadable(), "isDownloadable should return false for a non-downloadable resource.");
    }

    /**
     * Tests the {@code setDownloadable} method of the {@code ElectronicResource} class.
     */
    @Test
    public void testSetDownloadable() {
        ElectronicResource resource = new ElectronicResource("E-Book Title", true);
        resource.setDownloadable(false);
        assertFalse(resource.isDownloadable(), "Downloadable status should be updated to false.");
        resource.setDownloadable(true);
        assertTrue(resource.isDownloadable(), "Downloadable status should be updated to true.");
    }

    /**
     * Tests the {@code getDetails} method of the {@code ElectronicResource} class.
     */
    @Test
    public void testGetDetails() {
        ElectronicResource resource = new ElectronicResource("E-Book Title", true);
        String result = resource.getDetails();
        String expected = 
            "Title: E-Book Title\n" +
            "Downloadable: Yes";
        assertEquals(expected, result, "Generated details should match the expected format.");
    }
}
