class Solution():
    @staticmethod
    def tax(salary):
        tax = 0
        if salary > 4500:
            tax += (salary - 4500)*(28/100)
            salary = 4500
        
        if salary > 3000:
            tax += (salary - 3000)*(18/100)
            salary = 3000

        if salary > 2000:
            tax += (salary - 2000)*(8/100)
            salary = 2000

        if tax == 0:
            print("Isento")
        else:
            print(f"R$ {tax:.2f}")

if __name__ == "__main__":
    try:
        solut = Solution()
        solut.tax(float(input()))
    except ValueError:
        pass