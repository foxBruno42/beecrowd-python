import math

class Solution():
    def distance_between_spots(self,spot1,spot2):
        x1,y1 = map(float,spot1.split())
        x2,y2 = map(float,spot2.split())
        distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        print(f"{distance:.4f}") 

if __name__ == "__main__":
    try:
        spot1 = input()
        spot2 = input()
        solut = Solution()
        solut.distance_between_spots(spot1,spot2)
    except ValueError:
        print("Erro: Por favor, insira um número válido.")