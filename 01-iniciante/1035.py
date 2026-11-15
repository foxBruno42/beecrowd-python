class Solution():
    def verify_tokens(self,tokens):
        val_a,val_b,val_c,val_d = map(int,(tokens.split()))
        if((val_b > val_c) and (val_d > val_a) and ((val_c + val_d) > (val_a + val_b)) and val_c > 0 and val_d > 0 and (val_a%2==0)):
            print("Valores aceitos")
        else:
            print("Valores nao aceitos")

if __name__ == "__main__":
    try:
        solut = Solution()
        solut.verify_tokens(input())
    except ValueError:
        print("Valores nao aceitos")