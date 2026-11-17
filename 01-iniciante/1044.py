class Solution():
    def is_multiple(self):
        A,B = map(int,input().split())
        if A % B == 0 or B % A == 0:
            print("Sao Multiplos")
        else:
            print("Nao sao Multiplos")

if __name__ == "__main__":
    try:
        solut = Solution()
        solut.is_multiple()
    except ValueError:
        pass