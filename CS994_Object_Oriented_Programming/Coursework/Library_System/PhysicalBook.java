import java.util.List;
import java.util.ArrayList;
/**
 * Write a description of class PhysicalBook here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class PhysicalBook extends LibraryResource
{
    // instance variables - replace the example below with your own
    private String isbn;
    private Author author;
    private LibraryMember libraryMember;
    private List<String> damages;

    /**
     * Constructor for objects of class PhysicalBook
     */
    public PhysicalBook(String title, String isbn, Author author)
    {
        // initialise instance variables
        super(title);
        this.isbn = isbn;
        this.author = author;
        this.libraryMember = null;
        this.damages = new ArrayList<>();
    }

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    
    public String getIsbn(){
        return isbn;
    }
    
    public void setIsbn(String isbn){
        this.isbn = isbn;
    }
    
    public Author getAuthor(){
        return author;
    }
    
    public void setAuthor(Author author){
        this.author = author;
    }
    
    public LibraryMember getLibraryMember(){
        return libraryMember;
    }
    
    public void setLibraryMember (LibraryMember libraryMember){
        this.libraryMember = libraryMember;
    }
    
    public List<String> getDamages(){
        return damages;
    }
    
    public void setDamages(List<String> damages){
        this.damages = damages;
    }
    
    public void addDamage(String damage){
        damages.add(damage);
    }
    
    public boolean isAvailable(){
        return libraryMember == null;
    }
    
    @Override
    public void printDetails()
    {
        System.out.println("Title: " + getTitle());
        System.out.println("ISBN: " + isbn);
        if (author!=null){
            author.printDetails();
        } else {
            System.out.println("No author information available");
        }
        System.out.println("Available: " + (isAvailable()? "Yes": "No"));
        System.out.println("Damages: " + damages);
    }
}
