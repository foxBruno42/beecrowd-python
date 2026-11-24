class Solution():
    @staticmethod
    def sequence_sum():
        m, n = map(int,input().split())
        while(m > 0 and n > 0):
            sum = 0
            if m > n:
                aux = m
                m = n
                n = aux
            for i in range(m,n+1):
                sum += i
                print(f"{i}",end=" ")
            
            print(f"Sum={sum}")

            m, n = map(int,input().split())

if __name__ == "__main__":
    try:
        Solution.sequence_sum()
    except ValueError:
        pass