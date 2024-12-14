
/**
 * Write a description of class ElectronicResource here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class ElectronicResource extends LibraryResource
{
    private boolean downloadable;

    /**
     * Constructor for objects of class ElectronicResource
     */
    public ElectronicResource(String title, boolean downloadable)
    {
        super(title);
        this.downloadable = downloadable;
    }

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    
    public boolean isDownloadable(){
        return downloadable;
    }
    
    public void setDownloadable(boolean downloadable){
        this.downloadable = downloadable;
    }
    
    @Override
    public void printDetails()
    {
        System.out.println("Title: " + getTitle());
        System.out.println("Downloadable: " + (downloadable? "Yes" : "No"));
    }
}
