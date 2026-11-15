import math
class Solution():
    def bhaskara(self,sides):
        side_a,side_b,side_c = map(float,sides.split())
        delta = (side_b ** 2) - (4 * side_a * side_c)
        if(delta > 0 and side_a > 0):
            r1 = ((side_b * -1) + math.sqrt(delta))/(2 * side_a)
            r2 = ((side_b * -1) - math.sqrt(delta))/(2 * side_a)
            print(f"R1 = {r1:.5f}")
            print(f"R2 = {r2:.5f}")
        else:
            print("Impossivel calcular")

if __name__ == "__main__":
    try:
        solut = Solution()
        solut.bhaskara(input())
    except ValueError:
        print("Impossivel calcular")