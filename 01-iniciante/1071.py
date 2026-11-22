class Solution():
    @staticmethod
    def even_sum():
        num_a = int(input())
        num_b = int(input())
        even = 0
        if(num_a > num_b):
            aux = num_a
            num_a = num_b
            num_b = aux

        if num_a%2==0:
            num_a += 1
        else:
            num_a += 2

        for i in range(num_a,num_b,2):
            even += i

        print(even)

if __name__ == "__main__":
    try:
        Solution.even_sum()
    except ValueError:
        pass