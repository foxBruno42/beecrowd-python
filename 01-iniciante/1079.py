class Solution():
    @staticmethod
    def multiple_medium():
        number = int(input())
        for i in range(number):
            grade_1,grade_2,grade_3 = map(float,input())
            medium = ((grade_1*2.0)+(grade_2*3.0)+(grade_3*5.0))/10.0
            print(f"{medium:.1f}")

if __name__ == "__main__":
    try:
        Solution.multiple_medium()
    except ValueError:
        pass