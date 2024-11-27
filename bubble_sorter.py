#-------------------------- BUBBLE SORT --------------------------
#                          _-----------_                         #
def sort(random_number_list):
    for i in range(1, len(random_number_list)):
        did_i_swap_numbers = False
        for f in range(0, len(random_number_list)-i):
            if random_number_list[f] > random_number_list[f+1]:
                temp_num = random_number_list[f]
                random_number_list[f] = random_number_list[f+1]
                random_number_list[f+1] = temp_num            
                did_i_swap_numbers = True
        
        if( not did_i_swap_numbers):
            break
