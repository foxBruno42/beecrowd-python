class Solution():
    @staticmethod
    def check_pass():
        md = 0
        count = 0
        while True:
            grade = float(input())
            if 0.0 <= grade <= 10.0:
                md += grade
                count += 1
                if count == 2:
                    print(f"media = {(md/2):.2f}")
                    break
            else:
                print("nota invalida")

if __name__ == "__main__":
    try:
        keep = 1
        Solution.check_pass()
        while keep != 2:
            print("novo calculo (1-sim 2-nao)")
            keep = int(input())
            if keep == 1:
                Solution.check_pass()

    except ValueError:
        pass