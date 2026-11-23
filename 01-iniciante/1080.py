class Solution():
    @staticmethod
    def max_positicon():
        bigger = 0
        position = 0
        for i in range(100):
            num = int(input())
            if num > bigger:
                bigger = num
                position = i+1

        print(bigger)
        print(position)

if __name__ == "__main__":
    try:
        Solution.max_positicon()
    except ValueError:
        pass