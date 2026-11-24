class Solution():
    @staticmethod
    def experiments():
        animals = {'C':0,'R':0,'S':0}
        pace = int(input())
        for i in range(pace):
            amount,animal = input().split()
            animals[animal] += int(amount)
        total = sum(animals.values())
        print(f"Total: {total} cobaias")
        print(f"Total de coelhos: {animals['C']}")
        print(f"Total de ratos: {animals['R']}")
        print(f"Total de sapos: {animals['S']}")
        print(f"Percentual de coelhos: {((animals['C']/total)*100):.2f} %")
        print(f"Percentual de ratos: {((animals['R']/total)*100):.2f} %")
        print(f"Percentual de sapos: {((animals['S']/total)*100):.2f} %")

if __name__ == "__main__":
    try:
        Solution.experiments()
    except ValueError:
        pass