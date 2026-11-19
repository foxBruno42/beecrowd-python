class Solution:
    def find_place(self):
        ddd = int(input())
        places = {
            61: "Brasilia",
            71: "Salvador",
            11: "Sao Paulo",
            21: "Rio de Janeiro",
            32: "Juiz de Fora",
            19: "Campinas",
            27: "Vitoria",
            31: "Belo Horizonte",
        }
        # Se o ddd não existir nas chaves, retorna "DDD nao cadastrado"
        print(places.get(ddd, "DDD nao cadastrado"))


if __name__ == "__main__":
    try:
        solut = Solution()
        solut.find_place()
    except (ValueError, EOFError):
        pass