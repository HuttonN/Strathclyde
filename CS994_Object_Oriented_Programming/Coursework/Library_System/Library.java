import java.util.List;
import java.util.ArrayList;
/**
 * Write a description of class Library here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Library
{
    private List<LibraryResource> catalogue;

    /**
     * Constructor for objects of class Library
     */
    public Library()
    {
        this.catalogue = new ArrayList<>();
    }

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    
    public void addResource(LibraryResource resource){
        if(catalogue.contains(resource)){
            System.out.println("Error: Resource already exists in the catalogue.");
        } else {
            catalogue.add(resource);
        }
    }
    
    public void editAuthorFirstName(LibraryResource resource, String newFirstName){
        if (!catalogue.contains(resource)){
            System.out.println("Error: The resource is not in the catalogue.");
            return;
        }
        
        if (resource instanceof PhysicalBook){
            PhysicalBook book = (PhysicalBook) resource;
            Author author = book.getAuthor();
            if (author == null) {
                System.out.println("Error: The resource does not have an associated author");
                return;
            }
            author.setFirstName(newFirstName);
            System.out.println("Author's first name updated successfully.");
        }
    }
    
    public boolean containsResource(LibraryResource resource){
        return catalogue.contains(resource);
    }
    
    public void printPhysicalBooks()
    {
        for (LibraryResource resource : catalogue) {
            if (resource instanceof PhysicalBook){
                resource.printDetails();
            }
        }
    }
    
    public void printElectronicResources()
    {
        for (LibraryResource resource : catalogue) {
            if (resource instanceof ElectronicResource){
                resource.printDetails();
            }
        }
    }
}
