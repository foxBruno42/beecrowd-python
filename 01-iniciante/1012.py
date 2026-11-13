def calculate_area_triangle(sides):
    side_a, side_b, side_c = map(float, sides.split())
    print(f"TRIANGULO: {((side_a*side_c)/2):.3f}")          #a) a área do triângulo retângulo que tem A por base e C por altura.
    print(f"CIRCULO: {((3.14159 * (side_c**2))):.3f}")      #b) a área do círculo de raio C. (pi = 3.14159)
    print(f"TRAPEZIO: {(((side_a+side_b)*side_c)/2):.3f}")  #c) a área do trapézio que tem A e B por bases e C por altura.
    print(f"QUADRADO: {(side_b**2):.3f}")                   #d) a área do quadrado que tem lado B.
    print(f"RETANGULO: {(side_a * side_b):.3f}")            #e) a área do retângulo que tem lados A e B. 


if __name__ == "__main__":
    try:
        sides = input()
        calculate_area_triangle(sides)
    except ValueError:
        print("Erro: Por favor, insira um número válido.")