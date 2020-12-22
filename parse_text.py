name_list = ['Test Dummy', 'Jack Flanigan', 'Alexandra Wierzbiak', 'Leslie Acevedo', 'Faith Foster',
    'Harsha Nambri', 'Wan Ruan', 'Eric Xue', 'Prakashini Govindasamy',
    'Adam Armstead', 'Thomas Janas', 'Adamaris Nunez', 'Subhi Chandrasekaran',
    'David Lasota', 'Felicia Tan', 'Jeremy Starzec', 'Rishabh Sanghavi','Izabella Lach', 'Mark Alvarez']
name_list = ['Test Dummy', 'Zain Usman', 'Yikun Lee', 'Jeff Galiotto', 'Megan Ray', 
    'Alexis Waite', 'Rahil Barar', 'Berkelee Asare', 'Sofia Takki', 'Allen Partin', 
    'Dominika Piczura', 'Amogh Bhoopalam', 'Bethany Shiang', 'Katie Huynh', 
    'Yuna Lee', 'Erisa Farimani', 'Morgan Bentel', 'Zoe Nelson', 
    'Sana Khadilkar', 'Liam Herrebout']

# Fa 18
# group 1: caleb,trisha, group 2: Stephanie, Syntyche group 3: Alex,
# group 4: Neeka,  group 5:Lindsey group 6: Will
# group 7: Brittany,Vivian, group 8:Gunjan, group 9:Anastasia, Cormac, Abu
user_id_list = {"12957398":1,"17763156":1,
        "35430517":2,"11759976":2,
        "21137288":3,
        "11870726":4,
        "15916812":5,
        "12100288":6,
        "30404855":7,"5703781":7,
        "12234472":8,
        "42895127":9,"22268900":9,"41172024":9}
# Sp 19
# group 1: stephainie,syntyche | group 2: Neeka, Laura
# group 3: Alex M., group 4: Will
# group 5: Harrison | group 6: Kinh
# group 7: Genti | group 8: Leslie | group 9 (babysitter): Hannah
user_id_list = {"35430517":1,"11759976":1, "11870726":2, "29876287":2,
        "21137288":3, "12100288":4,
        "52860821":5,"52074003":6,
        "18043566":7, "42998479":8, "22413799":9 }

def data_parse(arr, curr):

    # go through each message
    for ct, d in enumerate(arr):
        # only check if message
        name = d['text']
        if 'user_id' in d and name in name_list:


            # if no likes
            if len(d['favorited_by'])==0:
                # update spreadsheet
                curr[name] = 1

            # if likes
            else:
                for like_id in d['favorited_by']:

                    if(like_id not in user_id_list):
                        continue

                    lastIdx = 1
                    if name in curr: lastIdx = curr[name]
                    currIdx = user_id_list[like_id]+1

                    # only new item, or new value is greater
                    if currIdx>lastIdx:

                        # change last place
                        curr[name] = currIdx
