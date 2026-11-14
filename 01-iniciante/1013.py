class Solution():
    def find_higher(self,numbers):
        value_1, value_2, value_3 = map(int, numbers.split())
        maior = max(value_1, value_2, value_3)
        print(f"{maior} eh o maior")

if __name__ == "__main__":
    try:
        numbers = input()
        solution = Solution()
        solution.find_higher(numbers)
    except ValueError:
        print("Erro: Por favor, insira um número válido.")