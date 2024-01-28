def month_to_season(numMonth):
    if numMonth >= 3 and  numMonth <= 5: return "Весна"
    elif numMonth >= 6 and  numMonth <= 8: return "Лето"
    elif numMonth >= 9 and  numMonth <= 11: return "Осень"
    elif numMonth == 12 or  (numMonth >= 1 and numMonth <= 2): return "Зима"
    else: return  "Неккоректно введены данные"

month = 3
print(month_to_season(month))



    
