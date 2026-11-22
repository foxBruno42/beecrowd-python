class Solution():
    @staticmethod
    def numbers():
        number = int(input())
        for i in range(number+1):
            if(i%2==1):
                print(i)

if __name__ == "__main__":
    try:
        Solution.numbers()
    except ValueError:
        pass