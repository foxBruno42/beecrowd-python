class Solution():
    def simple_sort(self,numbers):
        original_list = list(map(int, numbers.split()))
        sorted_list = sorted(original_list)
        for num in sorted_list:
            print(num)

        print("")

        for num in original_list:
            print(num)

if __name__ == "__main__":
    try:
        solut = Solution()
        solut.simple_sort(input())
    except ValueError:
        pass