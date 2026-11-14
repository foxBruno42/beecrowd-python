class Solution():
    def time_converter(self,time):
        print(f"{time//3600}:{((time%3600)//60)}:{(time%60)%60}")

if __name__ == "__main__":
    try:
        solut = Solution()
        solut.time_converter(int(input()))
    except ValueError():
        pass