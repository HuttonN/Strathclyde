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
            return;
        } 
        
        catalogue.add(resource);
        System.out.println("Resource successfully added to the catalogue.");
    }
    
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
    
    public void searchByAuthorSurname(String surname){
        int count = 0;
        
        System.out.println("Searching for resources by author surname: " + surname);
        for (LibraryResource resource : catalogue){
            if (resource instanceof PhysicalBook){
                PhysicalBook book = (PhysicalBook) resource;
                Author author = book.getAuthor();
                
                if (author == null){
                    System.out.println("Resource has no associated author:");
                    book.printDetails();
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
    
    public void removeResourceAtPosition(int position){
        if (position<0 || position >= catalogue.size()){
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
    
    public void printAvailableBooks(){
        System.out.println("Available Books:");
        
        boolean found = false;
        
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
    
    public int getResourceCount(){
        return catalogue.size();
    }
    
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
        member.borrowBook(book);
        System.out.println("The book '" + book.getTitle() + "' has successfully been lent to Library Member ID: " + member.getId());
    }
    
    public void acceptBookReturn(PhysicalBook book, boolean recordDamage, String damageDescription){
        if (!catalogue.contains(book)){
            System.out.println("Error: The book is not in the catalogue and cannot be returned.");
            return;
        }
        
        LibraryMember member = book.getLibraryMember();
        if (member != null) {
            member.returnBook(book);
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
