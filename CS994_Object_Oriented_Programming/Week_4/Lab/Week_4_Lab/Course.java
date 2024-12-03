
/**
 * Write a description of class Course here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */

import java.util.ArrayList;

public class Course
{
    // instance variables - replace the example below with your own
    private String courseID;
    private String courseName;
    private int courseFee;
    private int courseLength;
    private String department;
    private ArrayList<Module> curriculum;
    /**
     * Constructor for objects of class Course
     */
    public Course(String courseID, String courseName, int courseFee, int courseLength, String department)
    {
        this.courseID = courseID;
        this.courseName = courseName;
        this.courseFee = courseFee;
        this.courseLength = courseLength;
        this.department = department;
        this.curriculum = new ArrayList<>();
    }

    /**
     * Accessor methods
     */
    public String getCourseID() {
        return courseID;
    }
    
    public String getCourseName(){
        return courseName;
    }
    
    public int getCourseFee(){ 
        return courseFee;
    }
    
    public int getCourseLength(){
        return courseLength;
    }
    
    public String getDepartment(){
        return department;
    }
    
    public ArrayList<Module> getCurriculum(){
        return curriculum;
    }
    
    public void printCourseDetails(){
        System.out.println("Course Details:");
        System.out.println("Course ID:" + courseID);
        System.out.println("Course Name:" + courseName);
        System.out.println("Course Fee:" + courseFee);
        System.out.println("Course Length:" + courseLength);
        System.out.println("Department:" + department);
        
        if (curriculum.isEmpty()){
            System.out.println("No modules in the curriculum.");
        } else {
            System.out.println("Modules:");
        }
    }
    
    /**
     * Mutator methods
     */
    
    public void setCourseID(String courseID){
        this.courseID = courseID;
    }
    
    public void setCourseName(String courseName){
        this.courseName = courseName;
    }
    
    public void setCourseFee(int courseFee){
        this.courseFee = courseFee;
    }
    
    public void setCourseLength(int courseLength){
        this.courseLength = courseLength;
    }
    
    public void setDepartment(String department){
        this.department = department;
    }
    
    /**
     * addModule() method to add module parameter to ArrayList
     */
    
    public void addModule(Module module){
        if (module == null){
            System.out.println("Error: Module cannot be null.");
            return;
        }
        if (curriculum.contains(module)){
            System.out.println("Error: Curriculum already has Module");
            return;
        }
        curriculum.add(module);
        System.out.println("Module added successfully.");
    }
}
