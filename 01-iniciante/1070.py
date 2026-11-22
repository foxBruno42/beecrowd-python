class Solution():
    @staticmethod
    def numbers():
        number = int(input())
        if number%2==0:
            number += 1
        for i in range(number,number+12,2):
            print(i)

if __name__ == "__main__":
    try:
        Solution.numbers()
    except ValueError:
        pass