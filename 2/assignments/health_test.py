
class SchoolClass:
    def __init__(self,school_class_name:str,student_ages:list,students_heights:list,students_weigths:list,students_number)->None:
        self.school_class_name = school_class_name
        self.student_ages = student_ages
        self.students_heights = students_heights
        self.students_weigths = students_weigths
        self.students_number=students_number


    def calculate_students_information(self):
        # calculate age avg        
        ages_avg=sum(self.student_ages)/self.students_number
        # ages_avg=sum(self.student_ages)/len(self.student_ages)

        # calculate weigth avg       
        weights_avg=sum(self.students_weigths)/self.students_number
        # weights_avg=sum(self.students_weigths)/len(self.students_weigths)
        
        # calculate heigth avg        
        heights_avg=sum(self.students_heights)/self.students_number
        # heights_avg=sum(self.students_heights)/len(self.students_heights)

        return ages_avg,weights_avg,heights_avg


    def compare_school_class(self,class_obj):
        self_info=self.calculate_students_information()
        obj_info=class_obj.calculate_students_information()
        # compare ages first
        if self_info[2] > obj_info[2]:
            return self.school_class_name
        elif self_info[2] < obj_info[2]:
            return class_obj.school_class_name

        else:
            if self_info[1] > obj_info[1]:
                return self.school_class_name
            elif self_info[1] < obj_info[1]:
                return class_obj.school_class_name
            else:
                return "Same"



def main():
    
    A_students_number=int(input())
    A_student_ages=list(map(int,input().split()))
    A_student_heights=list(map(int,input().split()))
    A_student_weights=list(map(int,input().split()))

    a=SchoolClass("A",A_student_ages,A_student_heights,A_student_weights,A_students_number)
    a_info=a.calculate_students_information()


    B_student_numbers=int(input())
    B_student_ages=list(map(int,input().split()))
    B_student_heights=list(map(int,input().split()))
    B_student_weights=list(map(int,input().split()))

    b=SchoolClass("B",B_student_ages,B_student_heights,B_student_weights,B_student_numbers)
    b_info=b.calculate_students_information()

    # now show result of data
    print(f"{a_info[0]}\n{a_info[2]}\n{a_info[1]}")
    print(f"{b_info[0]}\n{b_info[2]}\n{b_info[1]}")
    print(a.compare_school_class(b))


if __name__ == "__main__":
    main()




