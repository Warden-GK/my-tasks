def list_attendant (the_list, whaat_to_do):
    the_new_list  = the_list.split(",")
    def one(): 
        print(the_new_list)
    def two():
        lenth_of_list = len(the_new_list)
        print(lenth_of_list)
    def three():
        is_this_item_on_the_list = input ('choose an item:')
        if (is_this_item_on_the_list in the_new_list):
            print ('Yes!')
        else:
            print('No!')
    def four():
        the_inp_for_times = input ('choose an item from thee list, and it will chack how mny times it is on the list:')
        how_many_times = the_new_list.count(the_inp_for_times)
        print (how_many_times)
    def five():
        the_inp_to_remove = input ('choose an item that you want to remove from the list:')
        the_new_list.remove(the_inp_to_remove)
        print(the_inp_to_remove, 'removed successfully from the list')
        print ('this is the new list:', the_new_list)
    def six():
        the_inp_to_add = input ('choose an item that you want to add to the list:')
        the_new_list.append(the_inp_to_add)
        print(the_inp_to_add, 'added successfully from the list')
        print ('this is the new list:', the_new_list)
    def seven():
        for word in the_new_list:
            if not(word.isalpha()):
                print(word)    
    def eight():
        list_witout_duplicates = list(dict.fromkeys(the_new_list))
    #    print(list_witout_duplicates)
    def nine():
        return('j')
    if (the_action == '1'):
        one()
    elif (the_action == '2'):
        two()
    elif (the_action == '3'):
        three()        
    elif (the_action == '4'):
        four()
    elif (the_action == '5'):
        five()
    elif (the_action == '6'):
        six()
    elif (the_action == '7'):
        seven()   
    elif (the_action == '8'):
        eight()
    elif (the_action == '9'):
        nine()       
the_input =  input ("write a shopping list seprate with cumes without spaces:")
i = 0
while (i < 10):
    the_action = input ("chose a number betwen 1 to 9:")
    if ('9' == the_action):
        break
    else:    
        list_attendant(the_input, the_action)

