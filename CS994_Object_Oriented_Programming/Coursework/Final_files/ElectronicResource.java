
/**
 * Represents an electronic resource in the library system.<p>
 * 
 * Extends the {@link LibraryResource} class and includes information
 * specific to electronic resources, such as whether the resource is downloadable.<p>
 * 
 * Examples of electronic resources include e-books, online articles, and journals.<p>
 * 
 * <b>Version 1.1 Notes:</b><br>
 * - Added the {@code getDetails} method to generate the resource details as a String.<br>
 * - removed {@code printDetails} method as defined by superclass<br>
 * 
 * @author Neil Hutton
 * @version 1.1
 */
public class ElectronicResource extends LibraryResource {
    private boolean downloadable;

    /**
     * Constructs a new ElectronicResource object with the specified title and downloadable status.
     * 
     * @param title the title of the electronic resource
     * @param downloadable  true if the resource is downloadable, false otherwise
     */
    public ElectronicResource(String title, boolean downloadable)
    {
        super(title);
        this.downloadable = downloadable;
    }

    /**
     * Checks whether the electronic resource is downloadable.
     * 
     * @return {@code true} if the resource is downloadable, {@code false} otherwise
     */
    public boolean isDownloadable(){
        return downloadable;
    }
    
    /**
     * Sets whether the electronic resource is downloadable.
     * 
     * @param downloadable {@code true} to mark the resource as downloadable, {@code false} otherwise
     */
    public void setDownloadable(boolean downloadable){
        this.downloadable = downloadable;
    }
    
    /**
     * Generates a string containing the details of the electronic resource.
     * 
     * @return a string representation of the electronic resource
     */
    @Override
    public String getDetails()
    {
        return "Title: " + getTitle() + "\n" +
               "Downloadable: " + (downloadable? "Yes" : "No");
    }
}
