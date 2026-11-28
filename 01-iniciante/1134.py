class Solution:
    def gas_station():
        gas = {1:0,2:0,3:0}
        opt = int(input())
        while(opt != 4):
            if(1 <= opt <= 3):
                gas[opt] += 1
            opt = int(input())

        print('MUITO OBRIGADO')
        print(f'Alcool: {gas[1]}')
        print(f'Gasolina: {gas[2]}')
        print(f'Diesel: {gas[3]}')

if __name__ == "__main__":
    try:
        Solution.gas_station()
    except ValueError:
        pass