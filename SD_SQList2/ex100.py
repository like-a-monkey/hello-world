import random
test = input("> ")
test1 = "pengshaojie hhh"
for k in test:
    print(k)
for line in test1:
    print(line)

def filter():
    lis=['3_hea','3_spa','4_dia','4_club','4_hea','4_spa',
    '5_dia','5_club','5_hea','5_spa']
    point = '3'
    new = [k for k in lis if point in k]
    lis = [k for k in lis if not k in new]
    print(new)
    print(lis)



def computer_ask_main(compter_name,computer_2,computer_3):

    if int(person1) == 0:#0 means me
        for k in lism:
            if card_point in k:
                print(compter_name," asks and takes your ",k,".")
                lism.remove(k)
                lis1.append(k)
                print("Now you have only ",len(lism)," cards.")
            else:
                print(compter_name," asks you if you have ",card_point," so he go fish.")

    if int(person1) == 1:
        for k in lis2:#computer_2
            if card_point in k:
                print(compter_name," asks and takes ",computer_2,"' ",k,".")
                lis2.remove(k)
                lis1.append(k)
                print("Now ",computer_2," have only ",len(lis2)," cards.")
            else:
                print(compter_name," asks ",computer_2," if he have ",card_point," but he go fish.")

    if int(person1) == 2:
        for k in lis3:#computer_3
            if card_point in k:
                print(compter_name," asks and takes bing's ",k,".")
                lis3.remove(k)
                lis1.append(k)
                print("Now bing have only ",len(lis3)," cards.")
            else:
                print(compter_name," asks bing if he have ",card_point," but he go fish.")

def computer_ask_loop_toplay(compter_name,lis1,lism,card_point):
    for k in lism:
        if card_point in k:
            print(compter_name," asks and takes your ",k,".")
            lism.remove(k)
            lis1.append(k)#lis1 选牌方电脑手牌
            print("Now you have only ",len(lism)," cards.")
        else:
            print(compter_name," asks you if you have ",card_point," so he go fish.")

def computer_ask_loop_tocom(compter_name,computer_2,lis1,lis2,card_point):
    for k in lis2:#computer_2
        if card_point in k:
            print(compter_name," asks and takes ",computer_2,"' ",k,".")
            lis2.remove(k)
            lis1.append(k)#lis1 选牌方电脑手牌
            print("Now ",computer_2," have only ",len(lis2)," cards.")
        else:
            print(compter_name," asks ",computer_2," if he have ",card_point," but he go fish.")

def points_get(the_card):
    point=['2','3','4','5','6','7','8','9','10','A','J','Q','K']
    counter = 0
    for p in point:
        if p in the_card:
            cards_point = p
            break
        else:
            counter+=1

    return cards_point



def player_choose_person():
    person_ask = input("> ")
    if person_ask != "1" and person_ask != "2" and person_ask != "3":
        print("Try to choose a number from 1,2,3")
        player_choose_person()

    else:
        print("zhixingle")
        print("person_ask",person_ask)
        return person_ask
