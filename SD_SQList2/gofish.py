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
    '9_dia','9_club','9_hea','9_spa','10_dia','10_club','10_hea','10_spa',
    'J_dia','J_club','J_hea','J_spa','Q_dia','Q_club','Q_hea','Q_spa',
    'K_dia','K_club','K_hea','K_spa']
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

def test():
    print(my_cards,len(my_cards))
    print(jia_cards,len(jia_cards))
    print(yi_cards,len(yi_cards))
    print(bing_cards,len(bing_cards))
    print(rest_cards,len(rest_cards))

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
    return lis1

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

def player_choose(lism,lisj,lisy,lisb,rest_cards_1):
    print("It's your turn to pick one to ask from jia or yi or bing.Oh!1,2,3 means jia yi bing")
    person_ask = player_choose_person()
    print("Then pick one card that you had")
    card_want = player_choose_cards(lism)
    counter = 0
    if person_ask == "1":
        for k in lisj:
            if card_want in k:
                print("He gives you: ",k)
                lism.append(k)
                lisj.remove(k)
                print("Now you have: ",lism,len(lism),"cards altogether")
                counter+=1
                print("Now jia has only   ",len(lisj)," cards")
        if counter == 0:
            print("Go Fish")
            gofish(rest_cards_1,lism)


    elif person_ask == "2":
        for k in lisy:
            if card_want in k:
                print("He gives you: ",k)
                lism.append(k)
                lisy.remove(k)
                print("Now you have: ",lism,len(lism),"cards altogether")
                counter+=1
                print("Now yi has only ",len(lisy)," cards")
        if counter == 0:
            print("Go Fish")
            gofish(rest_cards_1,lism)

    elif person_ask == "3":
        for k in lisb:
            if card_want in k:
                print("He gives you: ",k)
                lism.append(k)
                lisb.remove(k)
                print("Now you have: ",lism,len(lism),"cards altogether")
                counter+=1
                print("Now bing has only ",len(lisb)," cards")
        if counter == 0:
            print("Go Fish")
            gofish(rest_cards_1,lism)
    check_4cards_four(lism,lisj,lisy,lisb)
    return counter
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
def computer_ask_loop_toplay(compter_name,lis1,lism,card_point,rest_cards_1):
    counter=0
    for k in lism:
        if card_point in k:
            print(compter_name," asks and takes your ",k,".")
            lism.remove(k)
            lis1.append(k)#lis1 选牌方电脑手牌
            print("Now you have only ",len(lism)," cards.")
            counter+=1
    if counter ==0:
        print(compter_name," asks you if you have ",card_point," but he go fish.")
        gofish(rest_cards_1,lis1)

    return counter
def gofish(rest_cards,lis):
    k=random.randint(0,len(rest_cards)-1)
    lis.append(rest_cards[k])
    rest_cards.remove(rest_cards[k])

def computer_ask_loop_tocom(compter_name,computer_2,lis1,lis2,card_point,rest_cards_1):
    counter=0
    for k in lis2:#computer_2
        if card_point in k:
            print(compter_name," asks and takes ",computer_2,"' ",k,".")
            lis2.remove(k)
            lis1.append(k)#lis1 选牌方电脑手牌
            print("Now ",computer_2," have only ",len(lis2)," cards.")
            counter+=1
    if counter == 0:
        print(compter_name," asks ",computer_2," if he have ",card_point," but he go fish.")
        gofish(rest_cards_1,lis1)
    return counter
def computer_ask(compter_name,person1,card_point,lism,lisj,lisy,lisb,rest_cards):
    if compter_name == "Jia":
        lis1 = lisj
        lis2 = lisy
        lis3 = lisb
        if int(person1) == 0:#0 means me
            counter=computer_ask_loop_toplay(compter_name,lis1,lism,card_point,rest_cards)

        elif int(person1) == 1:
            counter=computer_ask_loop_tocom(compter_name,"yi",lis1,lis2,card_point,rest_cards)
        elif int(person1) == 2:
            counter=computer_ask_loop_tocom(compter_name,"bing",lis1,lis3,card_point,rest_cards)

    elif compter_name == "Yi":
        lis1 = lisy
        lis2 = lisj
        lis3 = lisb
        if int(person1) == 0:#0 means me
            counter=computer_ask_loop_toplay(compter_name,lis1,lism,card_point,rest_cards)
        elif int(person1) == 1:
            counter=computer_ask_loop_tocom(compter_name,"jia",lis1,lis2,card_point,rest_cards)
        elif int(person1) == 2:
            counter=computer_ask_loop_tocom(compter_name,"bing",lis1,lis3,card_point,rest_cards)


    elif compter_name == "Bing":
        lis1 = lisb
        lis2 = lisj
        lis3 = lisy
        if int(person1) == 0:#0 means me
            counter=computer_ask_loop_toplay(compter_name,lis1,lism,card_point,rest_cards)
        elif int(person1) == 1:
            counter=computer_ask_loop_tocom(compter_name,"jia",lis1,lis2,card_point,rest_cards)
        elif int(person1) == 2:
            counter=computer_ask_loop_tocom(compter_name,"yi",lis1,lis3,card_point,rest_cards)

    check_4cards_four(lism,lisj,lisy,lisb)
    return counter

def random_get(lis):
    computer_choose_person1 = random.randint(0,2)
    cards_num = random.randint(0,len(lis)-1)
    computer_choose_card = points_get(lis[cards_num])
    return computer_choose_person1,computer_choose_card

def computer_choose(lism,lisj,lisy,lisb,rest_cards_1):
    computer_choose_person1,computer_choose_card=random_get(lisj)
    counter=computer_ask("Jia",computer_choose_person1,computer_choose_card,lism,lisj,lisy,lisb,rest_cards_1)
    while counter > 0:
        computer_choose_person1,computer_choose_card=random_get(lisj)
        counter=computer_ask("Jia",computer_choose_person1,computer_choose_card,lism,lisj,lisy,lisb,rest_cards_1)

    computer_choose_person1,computer_choose_card=random_get(lisy)
    counter=computer_ask("Yi",computer_choose_person1,computer_choose_card,lism,lisj,lisy,lisb,rest_cards_1)
    while counter > 0:
        computer_choose_person1,computer_choose_card=random_get(lisy)
        counter=computer_ask("Yi",computer_choose_person1,computer_choose_card,lism,lisj,lisy,lisb,rest_cards_1)

    computer_choose_person1,computer_choose_card=random_get(lisb)
    counter=computer_ask("Bing",computer_choose_person1,computer_choose_card,lism,lisj,lisy,lisb,rest_cards_1)
    while counter > 0:
        computer_choose_person1,computer_choose_card=random_get(lisb)
        counter=computer_ask("Bing",computer_choose_person1,computer_choose_card,lism,lisj,lisy,lisb,rest_cards_1)

def check_4cards_one(name,lis):
    point=['2','3','4','5','6','7','8','9','10','A','J','Q','K']
    for i in point:
        counter = 0
        for j in lis:
            if i in j:
                counter+=1

        if counter == 4:
            for j in lis:
                if i in j:
                    lis.remove(j)
            for j in lis:
                if i in j:
                    lis.remove(j)

            print(name," have collected all the ",i," ,now ",name," have only ",len(lis)," cards.")

def check_4cards_four(lism,lisj,lisy,lisb):
    check_4cards_one("You",lism)
    check_4cards_one("Jia",lisj)
    check_4cards_one("Yi",lisy)
    check_4cards_one("Bing",lisb)

def check_cards_runout(lism,lisj,lisy,lisb):
    if len(lism)==0:
        print("Game over!")
        print("You win!")
    elif len(lisj)==0:
        print("Game over!")
        print("Jia win!")
    elif len(lisy)==0:
        print("Game over!")
        print("Yi yun!")
    elif len(lisb)==0:
        print("Game over!")
        print("Bing yin!")



news=shuffle_my(cards)
rest_cards=deal_cards(news,my_cards,jia_cards,yi_cards,bing_cards)
num_of_cards = 32
print("Game stare now!")
cards_read()
while my_cards!=0 and jia_cards!=0 and yi_cards!=0 and bing_cards!=0:
    counter = player_choose(my_cards,jia_cards,yi_cards,bing_cards,rest_cards)
    while counter > 0:
        counter = player_choose(my_cards,jia_cards,yi_cards,bing_cards,rest_cards)
    test()
    computer_choose(my_cards,jia_cards,yi_cards,bing_cards,rest_cards)
    test()
check_cards_runout(my_cards,jia_cards,yi_cards,bing_cards)
