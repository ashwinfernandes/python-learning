from contents import recipes


def my_deepcopy(d: dict) -> dict:
    """Copies a dictionary, creating copies of the `list` or
    `dict` values

    The function will crash with a AttributeError if the values of the
    dictionary aren't lists or dictionaries

    :param d: The dictionary to copy
    :return: A copy of `d`, with the values being copies of the original
        values.
    """
    new_dict = {}
    for key, values in d.items():
        # Use the if else block to raise an AttributeError with a
        # custom exception message when the type is neither
        # a list nor a dict
        # if type(values) == list or type(values) == dict:
            new_dict[key] = values.copy()
        # else:
        #     raise AttributeError(f"Expected a list or dictionary value. Found {type(values)}")
    return new_dict

recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
