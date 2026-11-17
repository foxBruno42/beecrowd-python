class Solution():
    def game_time(self,time):
        hour_ini,hour_fin = map(int,time.split())
        if(hour_ini == hour_fin):
            print("O JOGO DUROU 24 HORA(S)")
        elif(hour_ini < hour_fin):
            print(f"O JOGO DUROU {(hour_fin - hour_ini)} HORA(S)")
        else:
            print(f"O JOGO DUROU {((24-hour_ini) + hour_fin)} HORA(S)")

if __name__ == "__main__":
    try:
        solut = Solution()
        solut.game_time(input())
    except ValueError:
        pass