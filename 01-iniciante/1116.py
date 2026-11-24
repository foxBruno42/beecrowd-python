class Solution():
    @staticmethod
    def calculator():
        cases = int(input())
        for i in range(cases):
            num_a,num_b = map(int,input().split())
            if num_b == 0:
                print("divisao impossivel")
            else:
                print(f"{(num_a/num_b):.1f}")


if __name__ == "__main__":
    try:
        Solution.calculator()
    except ValueError:
        pass