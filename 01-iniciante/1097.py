class Solution():
    @staticmethod
    def sequence():
        i=1
        j=7
        while i < 10 :
            print(f"I={i} J={j}")
            print(f"I={i} J={j-1}")
            print(f"I={i} J={j-2}")
            i += 2
            j += 2

if __name__ == "__main__":
    try:
        Solution.sequence()
    except ValueError:
        pass