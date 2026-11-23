class Solution():
    @staticmethod
    def numbers():
        divider = int(input())
        for i in range(10001):
            if(i%divider==2):
                print(i)

if __name__ == "__main__":
    try:
        Solution.numbers()
    except ValueError:
        pass