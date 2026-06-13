def get_human_age(cat_age: int, dog_age: int) -> list:

    list_of_years = [0, 0]
    if cat_age < 15:
        list_of_years[0] = 0
    elif 15 <= cat_age < 24:
        list_of_years[0] = 1
    elif 24 <= cat_age < 28:
        list_of_years[0] = 2
    elif 28 <= cat_age < 32:
        list_of_years[0] = 3
    elif cat_age > 32:
        list_of_years[0] = (cat_age - 32) // 4 + 4

    if dog_age < 15:
        list_of_years[1] = 0
    elif 15 <= dog_age < 24:
        list_of_years[1] = 1
    elif 24 <= dog_age < 30:
        list_of_years[1] = 2
    elif 30 <= dog_age < 34:
        list_of_years[1] = 3
    elif dog_age > 34:
        list_of_years[1] = (dog_age - 34) // 5 + 4

    return list_of_years
