class Solution():
    def get_payment(self,money):
        cents = int((money%1)*100)
        print(f"NOTAS:")
        print(f"{int(money//100)} nota(s) de R$ 100.00")
        print(f"{int((money%100)//50)} nota(s) de R$ 50.00")
        print(f"{int(((money%100)%50)//20)} nota(s) de R$ 20.00")
        print(f"{int((((money%100)%50)%20)//10)} nota(s) de R$ 10.00")
        print(f"{int(((((money%100)%50)%20)%10)//5)} nota(s) de R$ 5.00")
        print(f"{int((((((money%100)%50)%20)%10)%5)//2)} nota(s) de R$ 2.00")
        print(f"MOEDAS:")
        print(f"{int((((((money%100)%50)%20)%10)%5)%2)} moeda(s) de R$ 1.00")
        print(f"{int((cents%100)//50)} moeda(s) de R$ 0.50")
        print(f"{int(((cents%100)%50)//25)} moeda(s) de R$ 0.25")
        print(f"{int((((cents%100)%50)%25)//10)} moeda(s) de R$ 0.10")
        print(f"{int(((((cents%100)%50)%25)%10)//5)} moeda(s) de R$ 0.05")
        print(f"{int((((((cents%100)%50)%25)%10)%5))} moeda(s) de R$ 0.01")

if __name__ == "__main__":
    try:
        solut = Solution()
        solut.get_payment(float(input()))
    except ValueError:
        pass    