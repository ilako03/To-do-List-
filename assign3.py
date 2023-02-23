# Iris Lako

def add_to_list(to_do_list):
    '''
    Adds items to a to-do list.
    :param to_do_list: the list to add to
    :return: None
    '''

    if (bool(to_do_list) != False): #given the list isn't empty, displays the list for the user
        print("Here is the list: ")
        for tasks in to_do_list:
            print(f"{tasks}")

    task_input = str(input("\nWhat would you like to add? \n"))

    while (task_input != ""): #continues to loop and add items to the list until user enters a newline character
        to_do_list.append(task_input) #adds items to the to-do list
        task_input = str(input("What else would you like to add to the list? (Press Enter/Return to stop) \n"))

    print("Here is the list with your new items: \n")
    for tasks in to_do_list: #prints the list with new items added
        print(f"{tasks}")

def completed_item(to_do_list):
    '''
    Mark an item from a to-do list as completed.
    :param to_do_list: the list that contains the item that was completed
    :return: None
    '''

    to_do_list_lowercase = [] #creates a new list to hold the lowercase task names for validation purposes

    print("This is the chosen list: ") #prints the chosen to-do list
    for tasks in to_do_list:
        print(f"{tasks}")
        to_do_list_lowercase.append(tasks.lower()) #turns items into lowercase and adds the items to the lowercase validation list

    task_input = str(input("Which item do you wish to mark as complete? \n"))
    task_input = task_input.lower()

    while (task_input != ""):
        task_input = task_input.lower() #makes user task input into lowercase for validation purposes
        index_tracker = 0 #index tracker that corrects list after removal

        for tasks in to_do_list_lowercase:
            if (task_input != tasks): #if task doesn't match list item, iterates to next item
                index_tracker += 1

            elif (task_input == tasks): #if task is found in the list, edits item to indeicate completedness
                to_do_list[index_tracker] = "[x]" + to_do_list[index_tracker]
                print("This is the list after marking the item as complete: ")
                for items in to_do_list:
                    print(f"{items}")

        if (index_tracker == len(to_do_list_lowercase)): #if the end of the list has been reached and item has not matched validation, displays error messahe
            print("The item was not marked. Please make sure you enter an item that appears in the list. ")

        task_input = str(input("\nChoose another item to mark as complete. [Enter/Return when done].\n"))

def create_to_do_list(list_name):
    '''
    Creates a new to-do list from a file or through user input.
    :param full_list: the list of to-do lists
    :return: None
    '''

    list = []
    list_creation = str(input("Are you creating this list from a file, or manually? \n"))
    list_creation = list_creation.lower() #makes user input lowercase for validation purposes

    if (list_creation == "file"):
        file_name = input("From which file are you creating the list? \n")
        file = open(file_name) #opens user inputted file

        for line in file: #adds each line of file into a to-do list
            to_do = line.strip()
            list.append(to_do) #adds line to a to-do list
        print("\nThank you for creating a to-do list!")

    elif (list_creation == "manually"):
        print("The list is empty.")
        add_to_list(list)
        print("\nThank you for creating a to-do list!")

    else: #displays error message if user has chosen an invalid list creation method
        print("Sorry. We can't create a list that way.")

    for items in list:
        list_name.append(items)

def edit_to_do_list(to_do_list):
    '''
    Edits items in a to-do list.
    :param to_do_list: the list to edit
    :return: None
    '''

    to_do_list_lowercase = [] #creates a list that holds the lowercase of inputs for validation purposes

    print("Here is the list you would like to edit: \n")
    for item in to_do_list: #displays list items for user so they can select an item to edit
        print(f"{item}")
        to_do_list_lowercase.append(item.lower()) #adds lowercase items to the list

    task_input = str(input("What item would you like to edit? "))
    task_input = task_input.lower() #turns user input into lowercase for validation purposes

    while (task_input != ""):
        task_input = task_input.lower() #turns user input into lowercase for validation purposes
        index_tracker = 0  #index tracker that corrects list after removal

        for tasks in to_do_list_lowercase:
            if (task_input != tasks): #if task doesn't match list item, iterates to next list item
                index_tracker += 1

            elif (task_input == tasks): #if task is found in the list, it is corrected with new user input
                to_do_list[index_tracker] = str(input("What would you like to change this item to?\n"))

        if (index_tracker == len(to_do_list_lowercase)): #if the item isn't in the list and it has reached the end of the list, displays an error message
            print("Sorry, you can't edit an item that isn't in the list. ")

        task_input = str(input("\nChoose another item to edit. [Return/Enter when done].\n"))

    for items in to_do_list:
        print(f"{items}")

def print_lists(list_name, all_lists):
    '''
    Prints all of the to-do lists, using different characters to delineate each list.
    :param all_lists: a list containing the Today, Someday, and Completed Lists
    :return: None
    '''

    for list in all_lists: #iterates through all lists
        if (bool(list) == True): #if a list isn't empty, will print it's items
            if (all_lists[0] == list): #prints formatted today list
                print("#" * 40)
                print("TO-DO TODAY:\n")

                for item in all_lists[0]:
                    print(f"    {item}")
                print("#" * 40)

            elif (all_lists[1] == list): #prints formatted someday list
                print("*" * 40)
                print("TO-DO SOMEDAY:\n")
                for item in list:
                    print(f"    {item}")
                print("*" * 40)

            elif (all_lists[2] == list): #prints formatted comepleted list
                print("x" * 40)
                print("TO-DO COMPLETED:\n")
                for item in list:
                    print(f"    {item}")
                print("x" * 40)

def prioritize_item(to_do_list):
    '''
    Mark an item in a to-do list as having either a high or low priority.
    :param to_do_list: the to-do list holding the item to be marked with a priority level
    :return: None
    '''

    to_do_list_lowercase = [] #create a list that contains lowercase item names for validation purposes

    print("This is the current list: \n")
    for item in to_do_list: #displays list items for users to choose whether to prioritize
        print(f"{item}")
        to_do_list_lowercase.append(item.lower()) #adds lowercase items to lowercase list for later validation

    task_input = str(input("What item would you like to prioritize? "))
    task_input = task_input.lower() #turns user input into lowercase for validation purposes

    while (task_input != ""):
        task_input = task_input.lower() #turns user input into lowercase for validation purposes
        index_tracker = 0 #index tracker that corrects list after removal

        for tasks in to_do_list_lowercase:
            if (task_input != tasks): #if task  isn't found, iterates to next item
                index_tracker += 1

            elif (task_input == tasks): #if task is found, prompts user for priority
                priority_level = str(input("Which level of priority? [Options: High, Low]\n"))

                if (priority_level == "high"):
                    to_do_list[index_tracker] = to_do_list[index_tracker] + "!!" #directly edits list item and adds high priority marker
                elif (priority_level == "low"):
                    to_do_list[index_tracker] = to_do_list[index_tracker] + "--" #directly edits list item and adds low priority marker

        if (index_tracker == len(to_do_list_lowercase)): #if the end of the list has been reached and item hasn't been found, displays an error message
            print("Sorry. But you can't prioritize something that isn't in the list. ")

        task_input = str(input("\nChoose another item to prioritize. [Return/Enter when done].\n"))

    print("This is your prioritized item list: ")
    for items in to_do_list: #prints list with prioritized items
        print(f"{items}")

def remove_completed(full_list):
    '''
    Removes any items that have been marked as completed in any to-do list, counting
    how many items are removed from each to-do list. It adds all of the removed items
    to the Completed list, removing the [x] from the item before adding it.
    :param full_list: a list containing the Today, Someday, and Completed Lists
    :return: a list containing how many items were removed from each list
    '''

    completed_unedited = [] #list that holds comlpeted items with their [x] marker
    completed = []

    items_removed = [0, 0] #list containing counter for items removed; index 0 represents items removed from today to-do list and index 1 represents items removed from someday to-do list

    i = 0 #index tracker to correct list index as items get removed
    full_list_index = 0

    for lists in full_list: #iterates through each list and removes completed items
        while i < len(lists):
            if (lists[i].startswith("[x]")): #looks for items with the completed items marker ('[x]')
                completed_unedited.append(lists[i]) #adds items to list
                lists.remove(lists[i]) #removes completed item from list
                i -= 1 #moves counter back one space to account for removal of item

                if (full_list_index < 2):
                    items_removed[full_list_index] = items_removed[full_list_index] + 1 #increases removed items counter
            i += 1 #iterates to next item
        full_list_index += 1 #iterates to next list index used in items_removed list

    for items in completed_unedited:
        completed.append(items[3:]) #appends items without the '[x]' marker

    return items_removed

def sort_list(to_do_list):
    '''
    Sort a to-do list, considering priority and completion when ordering.
    :param to_do_list: the to-do list to be sorted
    :return: None
    '''

    high_priority_items = []
    unprio_items = []
    low_priority_items = []
    completed_items = []

    high_priority_item_substring = "!!"
    low_priority_item_substring = "--"

    for items in to_do_list:
        if (items.startswith("[x]")):
            completed_items.append(items)

        elif (high_priority_item_substring in items):
            high_priority_items.append(items)

        elif (low_priority_item_substring in items):
            low_priority_items.append(items)

        else:
            unprio_items.append(items)

    high_priority_items = sorted(high_priority_items)
    unprio_items = sorted(unprio_items)
    low_priority_items = sorted(low_priority_items)
    completed_items = sorted(completed_items)
    list_of_sorted_items = [high_priority_items, unprio_items, low_priority_items, completed_items]

    to_do_list.clear()
    for lists in list_of_sorted_items:
        if (bool(lists) != False):
            to_do_list += lists

def validate_option(option):
    '''
    Checks if the user has entered a valid choice. If it is invalid,
    loop until it is valid or 'done'.
    :param option: the user's choice (a string)
    :return: True, if valid
             False, if done
    '''

    valid_options = ["add", "completed", "create", "done", "edit", "export", "prioritize", "remove", "sort", "view"]

    for inputs in valid_options: #iterates through valid options list to check if menu selection is correct
        if (option == "done"): #if user has selected done, stops checking valid options list and returns False, ending menu select program
            return False
            break
        elif (option == inputs):
            return True

def which_list(list_name, full_list):
    '''
    Checks the to-do list's name, and returns the corresponding list.
    :param list_name: the name of the list being looked for
    :param full_list: a list containing the Today, Someday, and Completed Lists
    :return: the Today, Someday, Complete, or All lists
             None, otherwise
    '''

    #the following lines associate each user-input word with the appropriate list index from the full list list.
    if (list_name == "today"):
        return full_list[0]

    elif (list_name == "someday"):
        return full_list[1]

    elif (list_name == "completed"):
        return full_list[2]

    elif (list_name == "all"):
        return full_list

    else:
        return None


def write_to_file(to_do_list):
    '''
    Exports a to-do list to a file.
    :param to_do_list: the list to be exported
    :return: None
    '''

    file = input("What file would you like to write to?\n")
    write_file = open(file, 'w')

    # write to file in such a way that last line doesn't include newline character
    for item in to_do_list:
        if to_do_list.index(item) == len(to_do_list) - 1:
            write_file.write(item)
        else:
            write_file.write(item + '\n')
    write_file.close()


def main():
    '''
    Runs a program for creating, modifying, and exporting to-do lists.
    :return: None
    '''

    #the following 4 lines initialize the three lists required for the program, as well as the list containing all lists
    today = []
    someday = []
    completed = []
    all_lists = [today, someday, completed]

    cont = True #bool variable for program menu selection

    user_list_creation = str(input("Choose a list to create. [Options: Today, Someday]\n"))  # prompts user to create a list
    user_list_creation = user_list_creation.lower()  # converts user string selection to lowercase for consistent validation purpose
    while (user_list_creation != "today" and user_list_creation != "someday"):  # while loop validates whether user has chosen a valid list option to create; if not, will re-prompt user until their choice is "today" or "someday"
        print("Please choose a valid option. ")
        user_list_creation = str(input("Choose a list to create. [Options: Today, Someday]\n"))
        user_list_creation = user_list_creation.lower()

    create_to_do_list(which_list(user_list_creation, all_lists)) #creates user list after they've selected a valid option


    menu_selection = str(input("What would you like TO-DO [Options: add, completed, create, done, edit, export, prioritize, remove, sort, view]\n"))  # prompts user to select a valid menu option
    menu_selection = menu_selection.lower()  # converts user string selection to lowercase for consistent validation purpose
    validate_option(menu_selection) #turns user input into lowercase for validation purposes

    if (validate_option(menu_selection) != True and validate_option(menu_selection) != False): #re-prompts user menu selection if option is not validated
        print("That input is invalid. Please try again. ")
        menu_selection = str(input("What would you like TO-DO [Options: add, completed, create, done, edit, export, prioritize, remove, sort, view]\n"))  # prompts user to select a valid menu option
        menu_selection = menu_selection.lower()  # converts user string selection to lowercase for consistent validation purpose
        validate_option(menu_selection) #turns user input into lowercase for validation purposes
    elif(validate_option(menu_selection) == False):
        cont = False #quits program if user has selected "done"

    while (cont != False): #menu selection loop; runs appropriate function associated with each menu item
        if (menu_selection == "add"):
            prompt = "What list would you like to add to? [Options: Today, Someday]\n" #appropriate propt to match menu selection
            list_choice = str(input(prompt))
            list_choice = list_choice.lower() #turns user input into lowercase for validation purposes

            while (list_choice != "today" and list_choice != "someday"):  #while loop validates whether user has chosen a valid list option to create; if not, will re-prompt user until their choice is "today" or "someday"
                print("Please choose a valid option. ")
                list_choice = str(input(prompt))
                list_choice = list_choice.lower()

            add_to_list(which_list(list_choice, all_lists))


        elif (menu_selection == "completed"):
            prompt = "Which list contains items you would like to mark as complete? [Options: Today, Someday]\n" #appropriate propt to match menu selection
            list_choice = str(input(prompt))
            list_choice = list_choice.lower() #turns user input into lowercase for validation purposes

            while (list_choice != "today" and list_choice != "someday"): # while loop validates whether user has chosen a valid list option to create; if not, will re-prompt user until their choice is "today" or "someday"
                print("Please choose a valid option. ")
                list_choice = str(input(prompt))
                list_choice = list_choice.lower()

            completed_item(which_list(list_choice, all_lists))


        elif (menu_selection == "create"):
            prompt = "Which list would you like to create? [Options: Today, Someday, Completed]\n" #appropriate propt to match menu selection
            list_choice = str(input(prompt))
            list_choice = list_choice.lower() #turns user input into lowercase for validation purposes

            while (list_choice != "today" and list_choice != "someday" and list_choice != "completed"):  # while loop validates whether user has chosen a valid list option to create; if not, will re-prompt user until their choice is "today" or "someday"
                print("Please choose a valid option. ")
                list_choice = str(input(prompt))
                list_choice = list_choice.lower() #turns user input into lowercase for validation purposes

            create_to_do_list(which_list(list_choice, all_lists))

        elif (menu_selection == "edit"):
            prompt = "Which list would you like to edit? [Options: Today, Someday]\n" #appropriate propt to match menu selection
            list_choice = str(input(prompt))
            list_choice = list_choice.lower() #turns user input into lowercase for validation purposes

            while (list_choice != "today" and list_choice != "someday"):  # while loop validates whether user has chosen a valid list option to create; if not, will re-prompt user until their choice is "today" or "someday"
                print("Please choose a valid option. ")
                list_choice = str(input(prompt))
                list_choice = list_choice.lower() #turns user input into lowercase for validation purposes

            edit_to_do_list(which_list(list_choice, all_lists))

        elif (menu_selection == "export"):
            prompt = "Which list would you like to export? [Options: Today, Someday, Completed]\n" #appropriate propt to match menu selection
            list_choice = str(input(prompt))
            list_choice = list_choice.lower() #turns user input into lowercase for validation purposes

            while (list_choice != "today" and list_choice != "someday" and list_choice != "completed"):  # while loop validates whether user has chosen a valid list option to create; if not, will re-prompt user until their choice is "today" or "someday"
                print("Please choose a valid option. ")
                list_choice = str(input(prompt))
                list_choice = list_choice.lower() #turns user input into lowercase for validation purposes

            write_to_file(which_list(list_choice, all_lists))

        elif (menu_selection == "prioritize"):
            prompt = "Which list would you like to add priorities to?\n" #appropriate propt to match menu selection
            list_choice = str(input(prompt))
            list_choice = list_choice.lower() #turns user input into lowercase for validation purposes

            while (list_choice != "today" and list_choice != "someday" and list_choice != "completed"):  # while loop validates whether user has chosen a valid list option to create; if not, will re-prompt user until their choice is "today" or "someday"
                print("Please choose a valid option. ")
                list_choice = str(input(prompt))
                list_choice = list_choice.lower() #turns user input into lowercase for validation purposes

            prioritize_item(which_list(list_choice, all_lists))
            print_lists(list_choice, all_lists)

        elif (menu_selection == "remove"):
            items_removed = [] #list in main containing # of items removed
            items_removed = remove_completed(all_lists)

            print(f"{items_removed[0]} removed from #Today# list.")
            print(f"{items_removed[1]} removed from +Someday+ list.")

        elif (menu_selection == "sort"):
            prompt = "Which list would you like to sort?\n" #appropriate propt to match menu selection
            list_choice = str(input(prompt))
            list_choice = list_choice.lower() #turns user input into lowercase for validation purposes

            while (list_choice != "today" and list_choice != "someday" and list_choice != "completed"):  # while loop validates whether user has chosen a valid list option to create; if not, will re-prompt user until their choice is "today" or "someday"
                print("Please choose a valid option. ")
                list_choice = str(input(prompt))
                list_choice = list_choice.lower() #turns user input into lowercase for validation purposes

            sort_list(which_list(list_choice, all_lists))
            print_lists(list_choice, all_lists)

        elif (menu_selection == "view"):
            prompt = "Which list would you like to view? [Options: Today, Someday, Completed, All]\n" #appropriate propt to match menu selection
            list_choice = str(input(prompt))
            list_choice = list_choice.lower() #turns user input into lowercase for validation purposes

            while (list_choice != "today" and list_choice != "someday" and list_choice != "completed" and list_choice != "all"):  # while loop validates whether user has chosen a valid list option to create; if not, will re-prompt user until their choice is "today" or "someday"
                print("Please choose a valid option. ")
                list_choice = str(input(prompt))
                list_choice = list_choice.lower() #turns user input into lowercase for validation purposes

            print_lists(list_choice, all_lists)


        menu_selection = str(input("What would you like TO-DO [Options: add, completed, create, done, edit, export, prioritize, remove, sort, view]\n"))  # prompts user to select a valid menu option
        menu_selection = menu_selection.lower()  # converts user string selection to lowercase for consistent validation purpose
        validate_option(menu_selection)

        if (validate_option(menu_selection) != True and validate_option(menu_selection) != False):
            print("That input is invalid. Please try again. ")
            menu_selection = str(input("What would you like TO-DO [Options: add, completed, create, done, edit, export, prioritize, remove, sort, view]\n"))  # prompts user to select a valid menu option
            menu_selection = menu_selection.lower()  # converts user string selection to lowercase for consistent validation purpose
            validate_option(menu_selection)
        elif (validate_option(menu_selection) == False):
            cont = False


    print("Get it done!")
    print_lists("all", all_lists)


main()
