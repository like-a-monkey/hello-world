while jia_cards == 0 or yi_cards == 0 or bing_cards == 0 or my_cards == 0:
    cards=['A_dia','A_club','A_hea','A_spa','2_dia','2_club','2_hea','2_spa',
    '3_dia','3_club','3_hea','3_spa','4_dia','4_club','4_hea','4_spa',
    '5_dia','5_club','5_hea','5_spa','6_dia','6_club','6_hea','6_spa',
    '7_dia','7_club','7_hea','7_spa','8_dia','8_club','8_hea','8_spa',
    '8_dia','8_club','8_hea','8_spa','9_dia','9_club','9_hea','9_spa',
    '10_dia','10_club','10_hea','10_spa','J_dia','J_club','J_hea','J_spa',
    'Q_dia','Q_club','Q_hea','Q_spa','K_dia','K_club','K_hea','K_spa']
    def shuffle(lis):
        k = 52
        while k >= 0:

            i = random(0,k)
            new_cards=[]
            new_cards.append(lis.[i])
            k-=1
        print(new_cards)
shuffle(cards)
