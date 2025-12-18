def cal_marks(total_marks,percentage):
    marks=total_marks*(percentage/100)
    return marks
total_marks=float(input("Enter total marks: "))
percentage=float(input("Enter percentage to calculate marks: "))
print("Calculated Marks:",cal_marks(total_marks,percentage))