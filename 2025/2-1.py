#AoC Day 2 Part 1

#total_ids_to_check = "22-44"
total_ids_to_check = "9226466333-9226692707,55432-96230,4151-6365,686836-836582,519296-634281,355894-471980,971626-1037744,25107-44804,15139904-15163735,155452-255998,2093-4136,829776608-829880425,4444385616-4444502989,2208288-2231858,261-399,66-119,91876508-91956018,2828255673-2828317078,312330-341840,6464-10967,5489467-5621638,1-18,426-834,3434321102-3434378477,4865070-4972019,54475091-54592515,147-257,48664376-48836792,45-61,1183-1877,24-43"

total_ids_to_check_split = total_ids_to_check.split(",")

duplicate_values = 0

for entry in total_ids_to_check_split:

    #Create the bottom and top values
    entry_min = int(entry.split("-")[0])
    entry_max = int(entry.split("-")[1])
    
    #Create the new array to loop through
    entry_array = list(range(entry_min,entry_max + 1))
    
    #Loop through each individual set of ids to check for values made of repeated digits
    for number in entry_array:

        number_string = str(number)

        #Skip odd length values as odd numbers can't be made of repeating values
        if len(number_string) % 2 == 1:
            continue
        
        ###Determine if the number string is made up of duplicate values
        #Create a character array of the number string
        number_string_character_array = list(number_string)

        #Compare the first character index with the middle character index and increase each iteration
        #Initialize while loop variables
        x = 0
        initial_index_number = 0
        comparison_equidistant_number = len(number_string_character_array)//2

        while x < len(number_string_character_array)//2:

            if number_string_character_array[initial_index_number] == number_string_character_array[comparison_equidistant_number]:
                initial_index_number += 1
                comparison_equidistant_number += 1
                x += 1
                is_made_of_duplicate_numbers_status = True
            else:
                is_made_of_duplicate_numbers_status = False
                break
        
        #Add if the number to be evaluated is made of duplicate numbers
        if is_made_of_duplicate_numbers_status == True:
            duplicate_values += number

print(f"Total of duplicate values is: {duplicate_values}")