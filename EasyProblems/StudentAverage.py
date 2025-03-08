def get_student_average(student_marks: list):
    """
    Given array of students and their marks in different subjects. 
    Find maximum average of the student in the following format below. 
    Use Math.floor() to convert fractional average to integer.   
    """

    container = {} # For each student stored in format student_name : [total_marks, no of marks]
    
    for stu_mark in student_marks:
        stu_name, mark = stu_mark[0], int(stu_mark[1])
        if stu_name in container.keys():
            existing_details = container[stu_name]
            container[stu_name] = [ existing_details[0] + mark, existing_details[1] + 1 ]
        else :
            container[stu_name] = [mark, 1]
    
    max_avg = 0
    for stu in container.keys():
        details = container[stu]
        avg = details[0] // details[1]
        max_avg = avg if avg > max_avg else max_avg
    
    return max_avg

print( get_student_average([ ["Alice", "70"],[ "Bob","80"], ["Charles","75"],[ "Bob", "80"],
                            [ "Dane", "1"],[ "Dane", "2"],[ "Dane", "3"] ] ))

