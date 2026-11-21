from datetime import datetime
class Solution():
    @staticmethod
    def days_hours() -> int:
        day_1 = input()
        time_1 = input()
        day_2 = input()
        time_2 = input()
        day_ini = day_1.split()[1] 
        time_ini = time_1.replace(" ", "")
        day_end = day_2.split()[1]
        time_end = time_2.replace(" ", "")
        ini_date_complete = f"2026-04-{day_ini.zfill(2)} {time_ini}"
        final_date_complete = f"2026-04-{day_end.zfill(2)} {time_end}"
        total_time = datetime.strptime(final_date_complete, "%Y-%m-%d %H:%M:%S") - datetime.strptime(ini_date_complete, "%Y-%m-%d %H:%M:%S")
        days = total_time.days
        secs = total_time.seconds
        horas = secs // 3600
        minutos = (secs % 3600) // 60
        segundos = secs % 60
        print(f"{days} dia(s)")
        print(f"{horas} hora(s)")
        print(f"{minutos} minuto(s)")
        print(f"{segundos} segundo(s)")

if __name__ == "__main__":
    try:
        Solution.days_hours()
    except ValueError:
        pass