class Solution():
    def calculate_gas(self,miles,liters):
        print(f"{(miles/liters):.3f} km/l")

if __name__ == "__main__":
    try:
        miles = int(input())
        liters = float(input())
        solut = Solution()
        solut.calculate_gas(miles,liters)
    except ValueError:
            print("Erro: Por favor, insira um número válido.")
