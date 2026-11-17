class Solution():
    def discovery_triangle(self,sides):
        # side.split()  << Divide a string nos espaços
        # float        << Tipo para o qual converter
        # map          << Aplica o float em cada elemento da lista
        # sorted       << Ordena os elementos
        # reverse=True << Garante a ordem decrescente (A >= B >= C)
        side_a, side_b, side_c = sorted(map(float, sides.split()), reverse=True)
        A = side_a ** 2
        B = side_b ** 2
        C = side_c ** 2
        if(side_a >= (side_b + side_c)):
            print("NAO FORMA TRIANGULO")
        elif(A == (B + C)):
            print("TRIANGULO RETANGULO")
        elif(A > (B + C)):
            print("TRIANGULO OBTUSANGULO")
        elif(A < (B + C)):
            print("TRIANGULO ACUTANGULO")

        if(side_a == side_b == side_c):
            print("TRIANGULO EQUILATERO")
        elif(side_a == side_b or side_b == side_c or side_a == side_c):
            print("TRIANGULO ISOSCELES")

if __name__ == "__main__":
    try:
        solut = Solution()
        solut.discovery_triangle(input())
    except ValueError:
        pass