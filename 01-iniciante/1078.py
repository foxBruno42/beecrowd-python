class Solution():
    @staticmethod
    def multi_table():
        number = int(input())
        for i in range(1,11):
            print(f"{i} x {number} = {number * i}")

if __name__ == "__main__":
    try:
        Solution.multi_table()
    except ValueError:
        pass