class Solution():
    @staticmethod
    def positives():
        total = 0
        for i in range(5):
            number = int(input())
            if(number%2==0):
                total += 1

        print(f"{total} valores pares")

if __name__ == "__main__":
    try:
        Solution.positives()
    except ValueError:
        pass