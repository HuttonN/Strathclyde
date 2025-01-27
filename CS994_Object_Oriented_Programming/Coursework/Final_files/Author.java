
/**
 * Represents an author of a library resource.<p>
 * 
 * Includes the author's first name, surname, and address. Provides methods to access and update the author's details.<p>
 * 
 * This class is used in conjunction with {@link LibraryResource} to provide
 * additional metadata about resources.<p>
 * 
 * <b>Version 1.1 Notes:</b><br>
 * - Added the {@code getDetails} method to generate the author details as a String.<br>
 * - Modified the {@code printDetails} method to use {@code getDetails} for better testability.<br>
 * 
 * @author Neil Hutton
 * @version 1.1
 */
public class Author {
    private String firstName;
    private String surname;
    private String address;

    /**
     * Constructs a new Author object with the specified first name, surname, and address.
     * 
     * @param firstName the first name of the author
     * @param surname   the surname of the author
     * @param address   the address of the author
     */
    public Author(String firstName, String surname, String address) {
        this.firstName = firstName;
        this.surname = surname;
        this.address = address;
    }

    /**
     * Gets the first name of the author.
     * 
     * @return the first name of the author
     */
    public String getFirstName() {
        return firstName;
    }
    
    /**
     * Sets the first name of the author.
     * 
     * @param firstName the new first name of the author
     */
    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }
    
    /**
     * Gets the surname of the author.
     * 
     * @return the surname of the author
     */
    public String getSurname() {
        return surname;
    }
    
    /**
     * Sets the surname of the author.
     * 
     * @param surname the new surname of the author
     */
    public void setSurname(String surname) {
        this.surname = surname;
    }
    
    /**
     * Gets the address of the author.
     * 
     * @return the address of the author
     */
    public String getAddress() {
        return address;
    }
    
    /**
     * Sets the address of the author.
     * 
     * @param address the new address of the author
     */
    public void setAddress(String address) {
        this.address = address;
    }
    
    /**
     * Generates a string containing all details of the author.
     * 
     * @return a string with the author's details
     */
    public String getDetails() {
        return "Author Details:\n" +
               "First Name: " + firstName + "\n" +
               "Surname: " + surname + "\n" +
               "Address: " + address + "\n";
    }
    
    /**
     * Prints all details of the author to the console
     */
    public void printDetails() {
        System.out.println(getDetails());
    }
}
