import java.util.List;
import java.util.ArrayList;
/**
 * Represents the library system that manages a catalogue of resources,
 * including physical books and electronic resources. 
 * 
 * Provides functionality for adding, removing, lending, and searching resources.
 * 
 * @author Neil Hutton
 * @version 1.0
 */
public class Library
{
    private List<LibraryResource> catalogue;

    /**
     * Constructs a new Library object with an empty catalogue.
     */
    public Library() {
        this.catalogue = new ArrayList<>();
    }

    /**
     * Adds a new resource to the library's catalogue.
     * 
     * @param resource the resource to add
     */
    public void addResource(LibraryResource resource) {
        if(catalogue.contains(resource)){
            System.out.println("Error: Resource already exists in the catalogue.");
            return;
        } 
        catalogue.add(resource);
        System.out.println("Resource successfully added to the catalogue.");
    }
    
    /**
     * Searches for resources in the catalogue by title (case-insensitive).
     * 
     * @param title the title to search for
     */
    public void searchByTitle(String title){
        int count = 0;
        System.out.println("Searching for resources with title: " + title);
        for (LibraryResource resource : catalogue){
            if (resource.getTitle().equalsIgnoreCase(title)){
                resource.printDetails();
                System.out.println("-------------------------------");
                count++;
            }
        }
        System.out.println("Total resources found: " + count);
    }
    
    /**
     * Searches for physical books in the catalogue by the author's surname (case-insensitive).
     * 
     * @param surname the author's surname to search for
     */
    public void searchByAuthorSurname(String surname){
        int count = 0;
        System.out.println("Searching for resources by author surname: " + surname);
        for (LibraryResource resource : catalogue){
            if (resource instanceof PhysicalBook){
                PhysicalBook book = (PhysicalBook) resource;
                Author author = book.getAuthor();
                if (author == null){
                    System.out.println("Resource titled '" + book.getTitle() + "' has no associated author.");
                    System.out.println("-------------------------------");
                    continue;
                }
                if (author.getSurname().equalsIgnoreCase(surname)){
                    book.printDetails();
                    System.out.println("-------------------------------");
                    count++;
                }
            }
        }
        System.out.println("Total resources found: " + count);
    }
    
    /**
     * Updates the author's first name for a specified physical book.
     * 
     * @param resource     the resource to update (must be a physical book)
     * @param newFirstName the new first name of the author
     */
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
    
    /**
     * Checks if a resource exists in the catalogue.
     * 
     * @param resource the resource to check
     * @return true if the resource exists, false otherwise
     */
    public boolean containsResource(LibraryResource resource){
        return catalogue.contains(resource);
    }
    
    /**
     * Prints the details of all physical books in the catalogue.
     */
    public void printPhysicalBooks()
    {
        for (LibraryResource resource : catalogue) {
            if (resource instanceof PhysicalBook){
                resource.printDetails();
            }
        }
    }
    
    /**
     * Prints the details of all electronic resources in the catalogue.
     */
    public void printElectronicResources()
    {
        for (LibraryResource resource : catalogue) {
            if (resource instanceof ElectronicResource){
                resource.printDetails();
            }
        }
    }
    
    /**
     * Removes a resource from the catalogue.
     * 
     * @param resource the resource to remove
     */
    public void removeResource(LibraryResource resource){
        if(!catalogue.contains(resource)){
            System.out.println("Error: The resource is not in the catalogue.");
            return;
        }
        if(resource instanceof PhysicalBook){
            PhysicalBook book = (PhysicalBook) resource;
            if (!book.isAvailable()){
                System.out.println("Error: The resource is currently on loan and cannot be removed.");
                return;
            }
        }
        if (resource instanceof ElectronicResource){
            System.out.println("Warning: Removing electronic resource. It will no longer be available for public access.");
        }
        
        catalogue.remove(resource);
        System.out.println("Resource successfully removed from the catalogue.");
    }
    
    /**
     * Removes a resource at a specific position in the catalogue.
     * 
     * @param position the position of the resource to remove
     */
    public void removeResourceAtPosition(int position){
        if (position < 0 || position >= catalogue.size()){
            System.out.println("Error: The specified position does not exist in the catalogue.");
            return;
        }
        LibraryResource resource = catalogue.get(position);
        if (resource instanceof PhysicalBook){
            PhysicalBook book = (PhysicalBook) resource;
            if(!book.isAvailable()){
                System.out.println("Error: The resource at position " + position + " is currently on loan and cannot be removed.");
                return;
            }
        }
        catalogue.remove(position);
        System.out.println("Resource at position " + position + " successfully removed from the catalogue.");
    }
    
    /**
     * Prints the details of all available physical books in the catalogue.
     */
    public void printAvailableBooks(){
        boolean found = false;
        System.out.println("Available Books:");
        for (LibraryResource resource : catalogue){
            if (resource instanceof PhysicalBook){
                PhysicalBook book = (PhysicalBook) resource;
                if (book.isAvailable()){
                    book.printDetails();
                    System.out.println("-------------------------------");
                    found = true;
                }
            }
        }
        if (!found){
            System.out.println("No available books found.");
        }
    }
    
    
    /**
     * Gets the total number of resources in the catalogue.
     * 
     * @return the number of resources in the catalogue
     */
    public int getResourceCount(){
        return catalogue.size();
    }
    
    /**
     * Lends a physical book to a library member.
     * 
     * @param book   the book to lend
     * @param member the member to lend the book to
     */
    public void lendBook(PhysicalBook book, LibraryMember member){
        if (!catalogue.contains(book)){
            System.out.println("Error: The book is not in the catalogue and cannot be lent.");
            return;
        }
        
        if (!book.isAvailable()){
            System.out.println("Error: The book is currently borrowed by another library member.");
            return;
        }
        
        book.setLibraryMember(member);
        member.addBorrowedBook(book);
        System.out.println("The book '" + book.getTitle() + "' has successfully been lent to Library Member ID: " + member.getId());
    }
    
    /**
     * Processes the return of a physical book.
     * Records damage if applicable.
     * 
     * @param book             the book to return
     * @param recordDamage     true if damage is to be recorded, false otherwise
     * @param damageDescription the description of the damage (if applicable)
     */
    public void acceptBookReturn(PhysicalBook book, boolean recordDamage, String damageDescription){
        if (!catalogue.contains(book)){
            System.out.println("Error: The book is not in the catalogue and cannot be returned.");
            return;
        }
        LibraryMember member = book.getLibraryMember();
        if (member != null) {
            member.removeBook(book);
            book.setLibraryMember(null);
            System.out.println("The book '" + book.getTitle() + "' has been successfully returned."); 
        } else {
            System.out.println("Warning: Book not currently borrowed so can't be returned.");
        }
        if (recordDamage && damageDescription != null && !damageDescription.isEmpty()){
            book.addDamage(damageDescription);
            System.out.println("Damage recorded for the book '" + book.getTitle() + "': " + damageDescription);
        }
    }
}
