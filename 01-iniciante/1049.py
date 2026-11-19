class Solution():
    def find_specime(self):
        bones = input()
        group = input()
        feed = input()
        if bones == "vertebrado":
            if group == "ave":
                if feed == "carnivoro":
                     print("aguia")
                else:
                     print("pomba")
            else:
                if feed == "onivoro":
                    print("homem")
                else:
                    print("vaca")
        else:
            if(group == "inseto"):
                if feed == "hematofago":
                    print("pulga")
                else:
                    print("lagarta")
            else:
                if feed == "hematofago":
                    print("sanguessuga")
                else:
                    print("minhoca")

if __name__ == "__main__":
    try:
        solut = Solution()
        solut.find_specime()
    except ValueError:
        pass