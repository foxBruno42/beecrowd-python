class Solution():
    @staticmethod
    def elevate_number():
        max = int(input())
        limit = 2
        while limit <= max:
            print(f"{limit}^2 = {limit**2}")
            limit += 2

if __name__ == "__main__":
    try:
        Solution.elevate_number()
    except ValueError:
        pass