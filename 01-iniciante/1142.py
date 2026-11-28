class Solution:
    def pum_prog():
        ending = int(input())*4
        for i in range(1,ending+1):
            if(i%4==0):
                print('PUM')
            else:
                print(f"{i}",end=" ")

if __name__ == "__main__":
    try:
        Solution.pum_prog()
    except ValueError:
        pass