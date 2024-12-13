
/**
 * ------------------------
 * Author class
 * ------------------------
 * 
 * Class to represent the author of a LibraryResource
 * 
 * Has the following fields:
 *  - firstName: String for the first name of the author
 *  - surname: String for the surname of the author
 *  - address: String to represent the address of the author (ADD FURTHER NOTES)
 *  
 * Has the following accessor methods:
 *  - getFirstName: method to return the first name of the author
 *  - getSurname: method to return the surname of the author
 *  - getAddress: method to return the address of the author
 *  - printDetails: method to print all the details of the author (TO BE IMPLEMENTED, PERHAPS RENAME TO printAuthorDetails)
 *  
 * Has the following mutator methods:
 *  - setFirstName: method to set the first name of the author
 *  - setSurname: method to set the surname of the author
 *  - setAddress: method to set the address of the author
 * 
 * @author (Neil Hutton)
 * @version (6 December 2024)
 */
public class Author
{
    private String firstName;
    private String surname;
    private String address;

    /**
     * Constructor for objects of class Author
     */
    public Author(String firstName, String surname, String address)
    {
        this.firstName = firstName;
        this.surname = surname;
        this.address = address;
    }

    /**
     * Accessor methods
     */
    public String getFirstName()
    {
        return firstName;
    }
    
    public String getSurname()
    {
        return surname;
    }
    
    public String getAddress()
    {
        return address;
    }
    
    /**
     * Mutator methods
     */
    public void setFirstName(String firstName)
    {
        this.firstName = firstName;
    }
    
    public void setSurname(String surname)
    {
        this.surname = surname;
    }
    
    public void setAddress(String address)
    {
        this.address = address;
    }
    
    public void printDetails(){
        System.out.println("First Name: " + firstName);
        System.out.println("Surname: " + surname);
        System.out.println("Address: " + address);
    }
}
