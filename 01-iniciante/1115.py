class Solution():
    def find_coordenates(self,dots):
        dot_x,dot_y = map(int,dots.split())
        while dot_x != 0 and dot_y != 0 :
            if(dot_x >= 0.0 and dot_y >= 0.0):
                print("primeiro")
            elif(dot_x >= 0.0 and dot_y < 0.0):
                print("quarto")
            elif(dot_x < 0.0 and dot_y < 0.0):
                print("terceiro")
            elif(dot_x < 0.0 and dot_y > 0.0):
                print("segundo")

            dot_x,dot_y = map(int,input().split())
            
if __name__ == "__main__":
    try:
        solut = Solution()
        solut.find_coordenates(input())
    except ValueError:
        pass