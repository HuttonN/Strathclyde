
/**
 * Represents a generic resource in the library. This is an abstract base class for specific types of 
 * resources such as physical books and electronic resources. It defines common properties and behaviors
 * shared by all library resources.<p>
 * 
 * Subclasses: {@link PhysicalBook}, {@link ElectronicResource} <p>
 * 
 * <b>Version 1.1 Notes:</b><br>
 * - Added the {@code getDetails} method. To be implemented by subclasses to generate the resource details as a String.<br>
 * - Modified the {@code printDetails} method to use {@code getDetails} for better testability.<br>
 * 
 * @author Neil Hutton
 * @version 1.1
 */
abstract class LibraryResource
{
    private String title;

    /**
     * Constructs a new LibraryResource with the specified title.
     * 
     * @param title the title of the resource
     */
    public LibraryResource(String title)
    {
        this.title = title;
    }

    /**
     * Gets the title of the library resource.
     * 
     * @return the title of the resource
     */
    public String getTitle()
    {
        return title;
    }
    
    /**
     * Sets the title of the library resource.
     * 
     * @param title the new title of the resource
     */
    public void setTitle(String title)
    {
        this.title = title;
    }
    
    /**
     * Generates a string containing the details of the library resource. Subclasses must 
     * implement this method to return specific details.
     * 
     * @return a string representation of the resource's details
     */
    public abstract String getDetails();
    
    /**
     * Prints the details of the library resource to the console. Calls the abstract 
     * {@code getDetails} method for the content
     */
    public void printDetails(){
        System.out.println(getDetails());
    }
}
