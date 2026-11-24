class Solution():
    @staticmethod
    def check_pass():
        pwd = input()
        accepted = False
        while not accepted:
            if pwd != '2002':
                print("Senha Invalida")
            else:
                print("Acesso Permitido")
                break
               
            pwd = input()

if __name__ == "__main__":
    try:
        Solution.check_pass()
    except ValueError:
        pass