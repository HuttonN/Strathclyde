/**
 * A class that maintains information on a book.
 * This might form part of a larger application such
 * as a library system, for instance.
 *
 * @author (K.Liaskos)
 * @version (1.0)
 */
class Book
{
    // The fields.
    private String author;
    private String title;
    private int pages;
    private String refNumber;
    private int borrowed;
    private boolean courseText;

    /**
     * Set the author and title fields when this object
     * is constructed.
     */
    public Book(String bookAuthor, String bookTitle, int bookPages, boolean bookCourseText)
    {
        author = bookAuthor;
        title = bookTitle;
        pages = bookPages;
        refNumber = "";
        courseText = bookCourseText;
    }

    /**
     * Return the author name of a book object.
     */
    public String getAuthor()
    {
        return author;
    }
    
    public String getTitle()
    {
        return title;
    }
    
    public int getPages()
    {
        return pages;
    }
    
    public String getRefNumber()
    {
        return refNumber;
    }
    
    
    public int getBorrowed()
    {
        return borrowed;
    }
    
    public boolean isCourseText()
    {
        return courseText;
    }
    
    public void setRefNumber(String ref)
    {
        if(ref.length() < 3) {
            System.out.println("Error! Ref number cannot be less than 3 characters long.");
        }
        else {
            refNumber = ref;
        }
    }
    
    public void printAuthor()
    {
        System.out.println(author);
    }
    
    public void printTitle()
    {
        System.out.println(title);
    }
    
    public void printDetails()
    {
        System.out.println("Author: " + author + "," + "Title: " + title + "," + "Pages: " + pages + "," + "Times borrowed: " + borrowed);
        if(refNumber.length() == 0) {
            System.out.println("ZZZ");
        }
        else {
            System.out.println(refNumber);
        }
    }
    
    public void borrow(){
        borrowed = borrowed + 1;
    }
}
