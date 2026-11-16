class Solution():
    def payment(self, itens):
        # Definindo o dicionário (equivalente ao array associativo do PHP)
        produtos = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}
        id_prod, qtd_prod = map(int,itens.split())
        vlr = qtd_prod * produtos[id_prod]
        print(f"Total: R$ {vlr:.2f}")

if __name__ == "__main__":
    try:
        solut = Solution()
        solut.payment(input())
    except ValueError:
        pass