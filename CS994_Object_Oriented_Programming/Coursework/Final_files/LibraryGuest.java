
/**
 * Represents a library guest who has temporary access to library resources. Guests can only access resources while 
 * physically present in the library and have a limited access duration of up to 3 days.<p>
 * 
 * This class is not tied to borrowing physical books or accessing electronic resources outside the library premises.<p>
 * 
 * <b>Version 1.1 Notes:</b><br>
 * - Modified the constructor to throw an error if an integer less than 1 is input for 
 *   the accessDuration. Stops zero or a negative number being accepted.<br>
 *   
 * @author Neil Hutton
 * @version 1.1
 */
public class LibraryGuest
{
    private int accessDuration;

    /**
     * Constructs a new LibraryGuest object with the specified access duration.
     * 
     * @param accessDuration the number of days the guest is allowed access (maximum 3 days, minimum 3 days)
     * @throws IllegalArgumentException if the access duration is less than 1 day or greater than 3 days
     */
    public LibraryGuest(int accessDuration)
    {
        if (accessDuration < 1 || accessDuration > 3) {
            throw new IllegalArgumentException("Access duration must be between 1 and 3 days.");
        }
        this.accessDuration = accessDuration;
    }

    /**
     * Gets the access duration of the library guest.
     * 
     * @return the number of days the guest has access to the library
     */
    public int getAccessDuration()
    {
        return accessDuration;
    }
}
