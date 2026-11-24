class Solution():
    @staticmethod
    def grenais():
        league = {'games':0,'inter':0,'gremio':0,'tied':0}
        new = 1
        while new != 2:
            nal,gre = map(int,input().split())
            league['games'] += 1
            if gre == nal:
                league['tied'] += 1
            elif gre > nal:
                league['gremio'] += 1
            else:
                league['inter'] += 1

            print("Novo grenal (1-sim 2-nao)")
            new = int(input())

        print(f"{league['games']} grenais")
        print(f"Inter:{league['inter']}")
        print(f"Gremio:{league['gremio']}")
        print(f"Empates:{league['tied']}")
        if league['inter'] < league['gremio']:
            print("Gremio venceu mais")
        elif league['gremio'] < league['inter']:
            print("Inter venceu mais")
        else:
            print("Nao houve vencedor")

if __name__ == "__main__":
    try:
        Solution.grenais()
    except ValueError:
        pass