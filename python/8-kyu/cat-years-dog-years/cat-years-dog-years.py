def human_years_cat_years_dog_years(h):
    return [h, *([15, 15] if h == 1 else [24 + 4*(h-2), 24 + 5*(h-2)])]