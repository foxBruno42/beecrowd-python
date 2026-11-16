class Solution():
    def find_triangle(self,sides):
        list_sides = list(map(float, sides.split()))
        list_sides.sort()
        if((list_sides[0] + list_sides[1]) > list_sides[2]):
            print(f"Perimetro = {sum(list_sides):.1f}")
        else:
            new_sides = list(map(float, sides.split()))
            print(f"Area = {(((new_sides[0]+new_sides[1])*new_sides[2])/2):.1f}")


if __name__ == "__main__":
    try:
        solut = Solution()
        solut.find_triangle(input())
    except ValueError:
        pass