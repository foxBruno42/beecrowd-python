class Solution():
    def rise_salary(self,salary):
        if(salary <= 400.00):
            percentage = 15
        elif(salary <= 800.00):
            percentage = 12
        elif(salary <= 1200.00):
            percentage = 10
        elif(salary <= 2000.00):
            percentage = 7
        else:
            percentage = 4

        add = salary * (percentage / 100)
        print(f"Novo salario: {(salary+add):.2f}")
        print(f"Reajuste ganho: {(add):.2f}")
        print(f"Em percentual: {percentage} %")


if __name__ == "__main__":
    try:
        solut = Solution()
        solut.rise_salary(float(input()))
    except ValueError:
        pass