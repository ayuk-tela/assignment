filtered_entry = None
while filtered_entry is None:
    try:
        entry = int(input('enter an integer between 1 - 10:'))
        if 1 <= entry <= 10:

            filtered_entry = entry
        else:
         print('invalid input....please enter between the integer 1 - 10 ')

    except ValueError:
     print('filtered entry: ', filtered_entry)
