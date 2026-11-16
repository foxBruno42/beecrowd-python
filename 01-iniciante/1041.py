class Solution():
    def find_coordenates(self,dots):
        dot_x,dot_y = map(float,dots.split())
        if(dot_x == 0.0 and dot_y ==  0.0):
            print("Origem")
        elif(dot_x == 0.0):
            print("Eixo Y")
        elif(dot_y == 0.0):
            print("Eixo X")
        elif(dot_x >= 0.0 and dot_y >= 0.0):
            print("Q1")
        elif(dot_x >= 0.0 and dot_y < 0.0):
            print("Q4")
        elif(dot_x < 0.0 and dot_y < 0.0):
            print("Q3")
        elif(dot_x < 0.0 and dot_y > 0.0):
            print("Q2")
            
if __name__ == "__main__":
    try:
        solut = Solution()
        solut.find_coordenates(input())
    except ValueError:
        pass