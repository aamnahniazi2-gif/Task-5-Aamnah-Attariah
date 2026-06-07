def calculate_grades():
    print("=== Decode Labs | Student Performance Classifier ===")
    print("Enter student marks (0 to 100). Type 'done' to calculate the average.\n")
    
    marks_list = []
    
    while True:
        user_input = input("Enter grade/mark: ").strip()
        
        if user_input.lower() == 'done':
            break
            
        if user_input.replace('.', '', 1).isdigit():
            score = float(user_input)
            
            if 0 <= score <= 100:
                marks_list.append(score)
            else:
                print("Score must be between 0 and 100.")
        else:
            print("Invalid score format. Please enter a valid number.")
            
    if len(marks_list) > 0:
        total_sum = sum(marks_list)
        total_count = len(marks_list)
        average_score = total_sum / total_count
        
        if average_score >= 85:
            standing = "Excellent Performance (First Class)"
        elif average_score >= 70:
            standing = "Good Performance (Second Class)"
        elif average_score >= 50:
            standing = "Satisfactory Performance (Pass)"
        else:
            standing = "Needs Improvement (Academic Probation)"
            
        print("\n-- Performance Summary --")
        print(f"Total Subjects Processed: {total_count}")
        print(f"Calculated Class Average: {average_score:.2f}%")
        print(f"Academic Standing       : {standing}")
        print("=----------------------------=")
    else:
        print("\nNo grades were processed. Program exiting cleanly.")

if __name__ == "__main__":
    calculate_grades()