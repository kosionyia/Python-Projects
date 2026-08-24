
def print_models(unprinted_designs, completed_models):

    """
    This function takes two lists. The first list contains designs that
    have not been printed yet, while the second list stores designs that
    have already been printed.
    Using while loop, it continues to run as long as there are designs in the 
    unprinted list.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):

    """Display all the models that have been successfully printed
        This function takes the completed_models list as an argument and
        uses a for loop to go through each model in the list. It prints
        each completed model to the screen so the user can see which
        designs have been printed
        """ 
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

    


