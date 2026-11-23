class Solution():
    @staticmethod
    def positives():
        num_range = int(input())
        total_in = 0
        total_out = 0
        for i in range(num_range):
            check = int(input())
            if check >= 10 and check <= 20:
                total_in += 1
            else:
                total_out += 1

        print(f"{total_in} in")
        print(f"{total_out} out")

if __name__ == "__main__":
    try:
        Solution.positives()
    except ValueError:
        pass