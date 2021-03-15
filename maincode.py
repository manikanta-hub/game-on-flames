print("welcome to the game of flames")
def remove_match_char(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]
                list1.remove(c)
                list2.remove(c)
                list3 = list1+["*"]+list2
                return [list3, True]

    list3 = list1 + ["*"] + list2
    return [list3, False]

if __name__ == "__main__" :
    player =input("type your name :")
    player = player.lower()
    player.replace(" ","")
    player_list = list(player)

    playermatch = input("enter your name you want to match:")
    playermatch = playermatch.lower()
    playermatch.replace(" ","")
    playermatch_list = list(playermatch)
    proceed = True

    while proceed:
        ret_list = remove_match_char(player_list, playermatch_list)
        con_list = ret_list[0]
        proceed = ret_list[1]
        star_index = con_list.index("*")
        player_list = con_list[:star_index]
        playermatch_list = con_list[star_index + 1:]
    count = len(player_list) + len(playermatch_list)
    result = ["Friends", "love","affection","marriage","Enemy","siblings"]
    while len(result)>1:
        split_index = (count % len(result)-1)
        if split_index >=0:
            right = result[split_index + 1:]
            left = result[: split_index]
            result = right+left
        else:
            result =result[:len(result)-1]
print("your Relationship status is:", result[0])