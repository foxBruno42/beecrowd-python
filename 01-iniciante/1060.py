class Solution():
    @staticmethod
    def number() -> int:
        count = 0
        for i in range(1, 7):
            num = float(input())
            if num > 0:
                count += 1

        return count

if __name__ == "__main__":
    try:
        qtd = Solution.number()
        print(f"{qtd} valores positivos")
    except ValueError:
        pass