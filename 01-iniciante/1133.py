class Solution:
    def check_values():
        num_a = int(input())
        num_b = int(input())
        if num_a > num_b:
            aux = num_a
            num_a = num_b
            num_b = aux

        for i in range(num_a+1,num_b):
            if i%5==2 or i%5==3:
                print(i)

if __name__ == "__main__":
    try:
        Solution.check_values()
    except ValueError:
        pass