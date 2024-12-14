
/**
 * Write a description of class LibraryGuest here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class LibraryGuest
{
    private int accessDuration;

    /**
     * Constructor for objects of class LibraryGuest
     */
    public LibraryGuest(int accessDuration)
    {
        if (accessDuration > 3) {
            throw new IllegalArgumentException("Access duration cannot exceed 3 days.");
        }
        this.accessDuration = accessDuration;
    }

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public int getAccessDuration()
    {
        // put your code here
        return accessDuration;
    }
    
    public void printDetails(){
        System.out.println("Library Guest Access Duration: " + accessDuration + " days");
    }
}
