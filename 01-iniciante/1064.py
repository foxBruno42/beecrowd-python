class Solution():
    @staticmethod
    def positives():
        total = 0
        total_sum = 0
        for i in range(6):
            number = float(input())
            if(number > 0):
                total_sum += number
                total += 1

        print(f"{total} valores positivos")
        print(f"{(total_sum/total):.1f}")

if __name__ == "__main__":
    try:
        Solution.positives()
    except ValueError:
        pass