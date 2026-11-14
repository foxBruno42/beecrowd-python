class Solution():
    def dollar_bills(self,money):
        print(money)
        print(f"{money//100} nota(s) de R$ 100,00")
        print(f"{(money%100)//50} nota(s) de R$ 50,00")
        print(f"{((money%100)%50)//20} nota(s) de R$ 20,00")
        print(f"{(((money%100)%50)%20)//10} nota(s) de R$ 10,00")
        print(f"{((((money%100)%50)%20)%10)//5} nota(s) de R$ 5,00")
        print(f"{(((((money%100)%50)%20)%10)%5)//2} nota(s) de R$ 2,00")
        print(f"{(((((money%100)%50)%20)%10)%5)%2} nota(s) de R$ 1,00")

if __name__ == "__main__":
    try:
        solut = Solution()
        solut.dollar_bills(int(input()))
    except ValueError:
        pass