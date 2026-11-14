class Solution:
    def calculating_gas(self,hours,speed):
        print(f"{((hours*speed)/12.0):.3f}")

if __name__ == "__main__":
    try:
        hours = int(input())
        speed = int(input())
        solut = Solution()
        solut.calculating_gas(hours,speed)
    except ValueError:
        pass #without print on error, just to avoid presentation error