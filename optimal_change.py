def optimal_change(price, given):
    # determines if both items are numbers and returns error if not
    try:
        # determines amount of change needed to be returned
        change_amount = given - price
    except:
        return 'Both inputs must be a number.'
    if change_amount == 0:
        return 'No change needed.'
    if change_amount < 0:
        return 'Insuffient funds.'
    return_string = ''
    #holding/staging area to collect amounts of each denomination of change
    count_dict = {}
    value_dict = {'$100 bill': 100, '$50 bill':50, '$20 bill':20, '$10 bill':10, '$5 bill':5, '$1 bill':1, 'quarter':.25, 'dime':.1, 'nickel':.05, 'penny':.01}
    # loop that compares change_amount to each denomination and pushes the amount of each needed to count_dict
    for key in value_dict:
        while change_amount >= value_dict[key]:
            change_amount -= value_dict[key]
            change_amount = round(change_amount, 2)
            # checking whether to increment count_dict or add new entry
            if key in count_dict:
                count_dict[key] = (count_dict[key] + 1)
            else:
                count_dict[key] = 1
    # creating dynamic portion of the final return string. Determines punctuation, plurality and whether the word needs to be proceeded with 'and'            
    for item in count_dict:
        if item == list(count_dict.keys())[-1] and (len(list(count_dict)) > 1):
            return_string += ' and'
        # penny has a special case for plurality
        if item == 'penny' and count_dict[item] > 1:
            return_string += ' '+str(count_dict[item])+' pennies '
        # adds 's' to non-penny plural items 
        elif count_dict[item] > 1:
            return_string += ' '+str(count_dict[item])+' '+item+'s,'
        else:
            return_string += ' '+str(count_dict[item])+' '+item+','
 

    return (f'The optimal change for an item that costs ${price} with an amount paid of ${given} is{return_string[:-1]}.')


optimal_change('a', 'b')


