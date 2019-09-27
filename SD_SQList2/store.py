import random
my_cards=[]
jia_cards=[]
yi_cards=[]
bing_cards=[]
news=[]
rest_cards=[]
cards=['A_dia','A_club','A_hea','A_spa','2_dia','2_club','2_hea','2_spa',
    '3_dia','3_club','3_hea','3_spa','4_dia','4_club','4_hea','4_spa',
    '5_dia','5_club','5_hea','5_spa','6_dia','6_club','6_hea','6_spa',
    '7_dia','7_club','7_hea','7_spa','8_dia','8_club','8_hea','8_spa',
    '8_dia','8_club','8_hea','8_spa','9_dia','9_club','9_hea','9_spa',
    '10_dia','10_club','10_hea','10_spa','J_dia','J_club','J_hea','J_spa',
    'Q_dia','Q_club','Q_hea','Q_spa','K_dia','K_club','K_hea','K_spa']
def shuffle_my(lis):
    k = 51
    new_cards=[]

    while k >= 0:
        i = random.randint(0,k)
        new_cards.append(lis[i])
        lis.pop(i)
        k-=1

    #print(new_cards)
    return new_cards

def deal_cards(lis1,lism,lisj,lisy,lisb):
    i = 4

    while i>=0:
        lism.append(lis1[0])
        lisj.append(lis1[1])
        lisy.append(lis1[2])
        lisb.append(lis1[3])
        lis1.pop(0)
        lis1.pop(0)
        lis1.pop(0)
        lis1.pop(0)
        i-=1
    #print(lis1)
    print(lism)
    print(lisj)
    print(lisy)
    print(lisb)
    #return lis1

def cards_read():
    print("Well,now you have: ",my_cards)

def player_choose_person():
    person_ask =input ("> ")
    while person_ask != "1" and person_ask != "2" and person_ask != "3":
        print("Try to choose a number from 1,2,3")
        person_ask =input ("> ")

    return person_ask

def player_choose_cards(lism):
    card_want1 = input("> ")
    lism1=' '.join(lism)#输入的str 无法与list变量使用in关键字
    while not(card_want1 in lism1):
        print("You don't have this kind of card,try another one")
        card_want1 = input("> ")
    return card_want1

def player_choose(lism,lisj,lisy,lisb):
    print("It's your turn to pick one to ask from jia or yi or bing.Oh!1,2,3 means jia yi bing")
    person_ask = player_choose_person()
    print("Then pick one card that you had")
    card_want = player_choose_cards(lism)
    counter = 0
    if person_ask == "1":
        for k in lisj:
            if card_want in k:
                print("He gives you: ",k)
                lisj.remove(k)
                lism.append(k)
                print("Now you have: ",lism,len(lism),"cards altogether")
                counter+=1
                print("Now jia has only   ",len(lisj)," cards")
        if counter == 0:
            print("Go Fish")

    elif person_ask == "2":
        for k in lisy:
            if card_want in k:
                print("He gives you: ",k)
                lisy.remove(k)
                lism.append(k)
                print("Now you have: ",lism,len(lism),"cards altogether")
                counter+=1
                print("Now yi has only ",len(lisy)," cards")
        if counter == 0:
            print("Go Fish")

    elif person_ask == "3":
        for k in lisb:
            if card_want in k:
                print("He gives you: ",k)
                lisb.remove(k)
                lism.append(k)
                print("Now you have: ",lism,len(lism),"cards altogether")
                counter+=1
                print("Now bing has only ",len(lisb)," cards")
        if counter == 0:
            print("Go Fish")
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

def computer_ask(compter_name,person1,card_point,lism,lisj,lisy,lisb):
    if compter_name == "Jia":
        lis1 = lisj
        lis2 = lisy
        lis3 = lisb
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
            for k in lis2:
                if card_point in k:
                    print(compter_name," asks and takes yi's ",k,".")
                    lis2.remove(k)
                    lis1.append(k)
                    print("Now yi have only ",len(lis2)," cards.")
                else:
                    print(compter_name," asks yi if he have ",card_point," but he go fish.")

        if int(person1) == 2:
            for k in lis3:
                if card_point in k:
                    print(compter_name," asks and takes bing's ",k,".")
                    lis3.remove(k)
                    lis1.append(k)
                    print("Now bing have only ",len(lis3)," cards.")
                else:
                    print(compter_name," asks bing if he have ",card_point," but he go fish.")


    elif compter_name == "Yi":
        lis1 = lisy
        lis2 = lisj
        lis3 = lisb
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
            for k in lis2:
                if card_point in k:
                    print(compter_name," asks and takes jia's ",k,".")
                    lis2.remove(k)
                    lis1.append(k)
                    print("Now jia have only ",len(lis2)," cards.")
                else:
                    print(compter_name," asks jia if he have ",card_point," but he go fish.")

        if int(person1) == 2:
            for k in lis3:
                if card_point in k:
                    print(compter_name," asks and takes bing's ",k,".")
                    lis3.remove(k)
                    lis1.append(k)
                    print("Now bing have only ",len(lis3)," cards.")
                else:
                    print(compter_name," asks bing if he have ",card_point," but he go fish.")

    elif compter_name == "Bing":
        lis1 = lisb
        lis2 = lisj
        lis3 = lisy
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
            for k in lis2:
                if card_point in k:
                    print(compter_name," asks and takes jia's ",k,".")
                    lis2.remove(k)
                    lis1.append(k)
                    print("Now jia have only ",len(lis2)," cards.")
                else:
                    print(compter_name," asks jia if he have ",card_point," but he go fish.")

        if int(person1) == 2:
            for k in lis3:
                if card_point in k:
                    print(compter_name," asks and takes yi's ",k,".")
                    lis3.remove(k)
                    lis1.append(k)
                    print("Now yi have only ",len(lis3)," cards.")
                else:
                    print(compter_name," asks yi if he have ",card_point," but he go fish.")










def computer_choose(lisa):
    computer_choose_person1 = random.randint(0,3)
    computer_choose_person2 = random.randint(0,3)
    k=len(lisa)#手牌数
    cards_num = random.randint(0,k)
    computer_choose_card = points_get(lisa[cards_num])
    computer_ask("Jia",computer_choose_person1,computer_choose_card,my_cards,jia_cards,yi_cards,bing_cards)





news=shuffle_my(cards)
rest_cards=deal_cards(news,my_cards,jia_cards,yi_cards,bing_cards)
num_of_cards = 32
print("Game stare now!")
cards_read()
player_choose(my_cards,jia_cards,yi_cards,bing_cards)
cards_num = random.randint(0,len(jia_cards)-1)
computer_choose_card = points_get(jia_cards[cards_num])
computer_choose_person1 = random.randint(0,3)
computer_ask("Jia",computer_choose_person1,computer_choose_card,my_cards,jia_cards,yi_cards,bing_cards)
