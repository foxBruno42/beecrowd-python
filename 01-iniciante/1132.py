class Solution:
    def get_sum_mult():
        num_a = int(input())
        num_b = int(input())
        sum = 0
        if num_a > num_b:
            aux = num_a
            num_a = num_b
            num_b = aux

        for i in range(num_a,num_b+1):
            if(i%13!=0):
                sum += i

        print(sum)

if __name__ == "__main__":
    try:
        Solution.get_sum_mult()
    except ValueError:
        pass