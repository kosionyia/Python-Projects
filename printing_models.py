from printing_functions import print_models, show_completed_models


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models: list[str] = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)