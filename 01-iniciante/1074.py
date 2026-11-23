class Solution():
    @staticmethod
    def numbers():
        num_range = int(input())
        for i in range(num_range):
            number = int(input())
            even = False
            if number%2==0:
                even = True

            if number > 0:
                print(f"{'EVEN'if even else 'ODD'} POSITIVE")
            elif(number < 0):
                print(f"{'EVEN'if even else 'ODD'} NEGATIVE")
            else:
                print("NULL")

if __name__ == "__main__":
    try:
        Solution.numbers()
    except ValueError:
        pass