class Solution():
    def age_calculation(self,days):
        print(f"{days//365} ano(s)")
        print(f"{(days%365)//30} mes(es)")
        print(f"{((days%365)%30)} dia(s)")
         	
if __name__ == "__main__":
    try:
        solut = Solution()
        solut.age_calculation(int(input()))
    except ValueError:
        pass