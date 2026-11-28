class Solution:
    def square_and_cube(self,times):
        for i in range(1,times+1):
            print(f"{i} {i**2} {i**3}")

if __name__ == "__main__":
    try:
        times = int(input())
        solut = Solution()
        solut.square_and_cube(times)
    except ValueError:
        pass