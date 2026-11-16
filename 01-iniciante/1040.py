class Solution():
    def grades(self,grades):
        grade_1,grade_2,grade_3,grade_4 = map(float,grades.split())
        final_grade = ((grade_1 * 2) + (grade_2 * 3) + (grade_3 * 4) + (grade_4)) / 10.0
        return final_grade

    def exame(self,avrg,new_grade):
        final = (avrg + new_grade) / 2
        print(f"Nota do exame: {new_grade:.1f}")
        if(final >= 5.0):
            print("Aluno aprovado.")
            print(f"Media final: {final:.1f}")
        else:
            print("Aluno reprovado.")

if __name__ == "__main__":
    try:
        solut = Solution()
        avrg = solut.grades(input())
        print(f"Media: {avrg:.1f}")
        if(avrg >= 7):
            print("Aluno aprovado.")
        elif(avrg < 5.0):
            print("Aluno reprovado.")
        else:
            print("Aluno em exame.")
            solut.exame(avrg,float(input()))
    except ValueError:
        pass