
/**
 * ------------------------
 * LibraryResource class
 * ------------------------
 * 
 * Has the following accessor methods:
 *  - getTitle: returns the title of the LibraryResource
 * 
 * Has the following mutator methods:
 *  - setTitle: method to set the title of the LibraryResource
 *
 * @author (Neil Hutton)
 * @version (6 December 2024)
 */
abstract class LibraryResource
{
    private String title;

    /**
     * Constructor for objects of class LibraryResource.
     */
    public LibraryResource(String title)
    {
        this.title = title;
    }

    /**
     * ------------------------
     * Accessor methods
     * ------------------------
     */
    public String getTitle()
    {
        return title;
    }
    
    /**
     * ------------------------
     * Mutator methods
     * ------------------------
     */
    public void setTitle()
    {
        this.title = title;
    }
    
    public abstract void printDetails();
}
