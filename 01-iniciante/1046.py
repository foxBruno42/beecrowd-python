class Solution():
    def game_time(self,time):
        hr_ini,min_ini,hr_fin,min_fin = map(int,time.split())

        # transforma tudo em minutos
        hrs_ini = (hr_ini * 60) + min_ini
        hrs_fin = (hr_fin * 60) + min_fin

        # encontra o tempo total em minutos
        total_time = hrs_fin - hrs_ini

        if total_time <= 0 :
            total_time += 1440

        print(f"O JOGO DUROU {(total_time//60)} HORA(S) E {(total_time%60)} MINUTO(S)")

if __name__ == "__main__":
    try:
        solut = Solution()
        solut.game_time(input())
    except ValueError:
        pass