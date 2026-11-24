class Solution():
    @staticmethod
    def sequence():
        i=0
        j=1
        while i <= 2:
            print(f"I={i:.2g} J={j:.2g}")
            print(f"I={i:.2g} J={(j+1):.2g}")
            print(f"I={i:.2g} J={(j+2):.2g}")
            i += .2
            j += .2

if __name__ == "__main__":
    try:
        Solution.sequence()
    except ValueError:
        pass