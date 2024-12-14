import java.util.List;
import java.util.ArrayList;
/**
 * Write a description of class LibraryMember here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class LibraryMember
{
    private int id;
    private List<PhysicalBook> borrowedBooks;

    /**
     * Constructor for objects of class LibraryMember
     */
    public LibraryMember()
    {
        this.id = id;
        this.borrowedBooks = new ArrayList<>();
    }

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    
    public int getId(){
        return id;
    }
    
    public void setId(){
        this.id = id;
    }
    
    public List<PhysicalBook> getBorrowedBooks(){
        return borrowedBooks;
    }
    
    public void borrowBook(PhysicalBook book){
        if (borrowedBooks.contains(book)){
            System.out.println("Error: Book is already borrowed by this member");
        } else {
            borrowedBooks.add(book);
        }
    }
    
    public void printDetails(){
        System.out.println("Library Member ID: " + id);
        if (borrowedBooks.isEmpty()) {
            System.out.println("Borrowed Books: None");
        } else {
            System.out.println("Borrowed Books: ");
            for (PhysicalBook book : borrowedBooks){
            book.printDetails();
            }
        }
    }
    
    public int numberOfBorrowedBooks(){
        return borrowedBooks.size();
    }
}
