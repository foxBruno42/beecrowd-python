class Solution():
    def find_position(self,point):
        if(point >= 0 and point <= 25.000):
            print(f"Intervalo [0,25]")
        elif(point > 25.000 and point <= 50.000):
            print(f"Intervalo (25,50]")
        elif(point > 50.000 and point <= 75.000):
            print(f"Intervalo (50,75]")
        elif(point > 75.000 and point <= 100.000):
            print(f"Intervalo (75,100]")
        else:
            print("Fora de intervalo")

if __name__ == "__main__":
    try:
        solut = Solution()
        solut.find_position(float(input()))
    except ValueError:
        print("Fora de intervalo")