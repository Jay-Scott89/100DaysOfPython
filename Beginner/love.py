def calculate_love_score(name1, name2):
    check1 = "TRUE"
    check2 = "LOVE"
    check1_total = 0
    check2_total = 0
    
    for i in name1.upper():
        for j in check1:
            if i == j:
                check1_total += 1
        for k in check2:
            if i == k:
                check2_total += 1
    
    for i in name2.upper():
        for j in check1:
            if i == j:
                check1_total += 1
        for k in check2:
            if i == k:
                check2_total += 1
    
    print(f"{check1_total}{check2_total}")
    
calculate_love_score("ANGELA YU", "JACK BAUER")
        