class Solution():
    def cars_distance(self,miles):
        print(f"{miles*2} minutos")

if __name__ == "__main__":
    try:
        miles = int(input())
        solut = Solution()
        solut.cars_distance(miles)
    except ValueError:
        pass #para nao ter um presentation erro