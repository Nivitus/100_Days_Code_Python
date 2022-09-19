def Find_Average_Marks(marks):
    sum_of_marks = sum(marks)
    number_of_marks = len(marks)
    avg_of_marks = sum_of_marks / number_of_marks
    return avg_of_marks
    
def Compute_Grade(avg_of_marks):
    if avg_of_marks > 80:
        grade = "A"
    elif avg_of_marks >= 60:
        grade = "B"
    elif avg_of_marks >= 50:
        grade = "C"
    else:
        grade = "F"
    return grade

marks = [70, 60, 50, 75, 90]
avg_of_marks = Find_Average_Marks(marks)
print("Your Average Mark is:",avg_of_marks)

grade = Compute_Grade(avg_of_marks)
print("This is your grade:", grade)

