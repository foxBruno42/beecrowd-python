class Solution():
    @staticmethod
    def order():
        x, y = map(int,input().split())
        while(x != y):
            if x > y:
                print("Decrescente")
            else:
                print("Crescente")
                

            x, y = map(int,input().split())

if __name__ == "__main__":
    try:
        Solution.order()
    except ValueError:
        pass