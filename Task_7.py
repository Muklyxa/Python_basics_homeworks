import json

titles = []
total = []
with open("text_7.txt", "r", encoding="utf-8") as f_obj:
    lines = f_obj.readlines()
    average_profit = 0
    cnt_of_pos_prof = 0
    for i in range(len(lines)):
        string = lines[i].split()
        titles.append(string[0])
        benefit = float(string[2]) - float(string[3])
        total.append(benefit)
        if benefit > 0:
            average_profit += benefit
            cnt_of_pos_prof += 1
    average_profit /= cnt_of_pos_prof

profit_dict = dict(zip(titles, total))
average_profit_dict = {"average profit": average_profit}
result = [profit_dict, average_profit_dict]

with open("text_7_7.json", "w", encoding="utf-8") as write_f:
    json.dump(result, write_f, ensure_ascii=False, indent=4, separators=(",", ": "))
