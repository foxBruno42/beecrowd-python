class Solution():
    @staticmethod
    def sequence():
        i=1
        while i < 10 :
            print(f"I={i} J=7")
            print(f"I={i} J=6")
            print(f"I={i} J=5")
            i += 2

if __name__ == "__main__":
    try:
        Solution.sequence()
    except ValueError:
        pass