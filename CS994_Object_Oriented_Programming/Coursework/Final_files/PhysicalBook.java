import java.util.List;
import java.util.ArrayList;
/**
 * Represents a physical book in the library system.<p>
 * 
 * Extends the {@link LibraryResource} class and includes additional information 
 * specific to physical books, such as ISBN, author, damages and borowing details. <p>
 *
 * <b>Version 1.1 Notes:</b><br>
 * - Added the {@code getDetails} method to generate the book details as a String.<br>
 * - removed {@code printDetails} method as defined by superclass.<br>
 *
 * @author Neil Hutton
 * @version 1.1
 */
public class PhysicalBook extends LibraryResource
{
    private String isbn;
    private Author author;
    private LibraryMember libraryMember;
    private List<String> damages;

    /**
     * Constructs a new PhysicalBook object with the specified title, ISBN and author.
     * 
     * @param title     the title of the book
     * @param isbn      the ISBN of the book
     * @param author    the author of the book
     */
    public PhysicalBook(String title, String isbn, Author author) {
        super(title);
        this.isbn = isbn;
        this.author = author;
        this.libraryMember = null; // Default to no borrower
        this.damages = new ArrayList<>();
    }

    /**
     * Gets the ISBN of the book.
     * 
     * @return the ISBN of the book
     */
    public String getIsbn(){
        return isbn;
    }
    
    /**
     * Sets the ISBN of the book.
     * 
     * @param the new ISBN of the book
     */
    public void setIsbn(String isbn){
        this.isbn = isbn;
    }
    
    /**
     * Gets the author of the book.
     * 
     * @return the author of the book, or null if no author is assigned
     */
    public Author getAuthor(){
        return author;
    }
    
    /**
     * Sets the author of the book.
     * 
     * @param author the new author of the book
     */
    public void setAuthor(Author author){
        this.author = author;
    }
    
    /**
     * Gets the library member who has borrowed the book.
     * 
     * @return the library member who borrowed the book, or null if the book is available
     */
    public LibraryMember getLibraryMember(){
        return libraryMember;
    }
    
    /**
     * Sets the library member who has borrowed the book.
     * 
     * @param libraryMember the library member to assign as the borrower
     */
    public void setLibraryMember (LibraryMember libraryMember){
        this.libraryMember = libraryMember;
    }
    
    /**
     * Gets the list of recorded damages for the book.
     * 
     * @return a list of damage descriptions
     */
    public List<String> getDamages(){
        return new ArrayList<>(damages);
    }
    
    /**
     * Replaces the list of damages with a new list.
     * 
     * @param damages the new list of damages
     */
    public void setDamages(List<String> damages){
        this.damages = damages;
    }
    
    /**
     * Adds a damage description to the book's damage list.
     * 
     * @param damage the damage description to add
     */
    public void addDamage(String damage){
        damages.add(damage);
    }
    
    /**
     * Determines whether the book is available for borrowing.<p>
     * 
     * This method checks if the book is currently associated with a library member. If 
     * no member has borrowed the book (i.e., the {@code libraryMember} field is {@code null}), the 
     * book is considered available.<p>
     * 
     * This method does not verify the book's existence in the library catalog or any other 
     * external conditions. Such checks are handled by the {@code Library} class.<p>
     * 
     * @return {@code true} if the book is not currently borrowed by any member; 
     *         {@code false} otherwise
     */
    public boolean isAvailable(){
        return libraryMember == null;
    }
    
    /**
     * Generates a string containing the details of the book.
     * 
     * @return a string representation of the book
     */
    @Override
    public String getDetails()
    {
        String authorDetails = (author!= null) ? author.getDetails() : "No author information available.";
        String damageDetails = damages.isEmpty() ? "None" : String.join(", ", damages);
        
        return "Title: " + getTitle() + "\n" +
               "ISBN: " + isbn + "\n" +
                authorDetails +
               "Available: " + (isAvailable() ? "Yes" : "No") + "\n" +
               "Damages: " + damageDetails;
    }
}
