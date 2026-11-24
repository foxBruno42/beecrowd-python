class Solution():
    @staticmethod
    def sequence():
        j = 60
        i=1
        while j >= 0 :
            print(f"I={i} J={j}")
            i += 3
            j -= 5

if __name__ == "__main__":
    try:
        Solution.sequence()
    except ValueError:
        pass