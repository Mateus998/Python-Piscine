cookbook: dict[str, dict[str, list[str] | str | int]] = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomato"],
        "meal": "lunch",
        "prep_time": 10
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomato", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}


def print_cookbook_recipes() -> None:
    for recipe in cookbook.keys():
        print(recipe)


def print_recipe_details(recipe_name: str) -> None:
    if not recipe_name:
        return
    recipe = cookbook.get(recipe_name)
    if not recipe:
        print(f"{recipe_name} is not on cookbook")
        return
    
    for key, value in recipe.items():
        print(key, end=": ")
        if isinstance(value, list):
            print(", ".join(value))
        else:
            print(value)


def delete_recipe(recipe_name: str) -> None:
    if not cookbook.pop(recipe_name, None):
        print(f"{recipe_name} is not on cookbook")


def create_recipe() -> None:
    try:
        key: str = input("Enter a name:\n")

        while key in cookbook.keys() or not key:
            key = input("Enter a valid name:\n")

        ingredients: list[str] = []

        ingredient: str = input("Enter ingredients:\n")
        
        while ingredient:
            ingredients.append(ingredient)
            ingredient = input()

        meal: str = input("Enter a meal type:\n")

        while not meal:
            meal = input("Enter a valid meal type:\n")

        prep_time: int = -1
        while prep_time == -1:
            try:
                prep_time = int(input("Enter preparation time in minutes:\n"))
                if prep_time < 0:
                    prep_time = -1
            except ValueError:
                prep_time = -1
    except (KeyboardInterrupt, EOFError):
        print("Recipe creation canceled")
        return
    
    recipe_details: dict[str, list[str] | str | int] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
    }

    # cookbook[key] = recipe_details
    cookbook.update({key: recipe_details})


def main() -> None:
    print("Welcome to Python Cookbook!")
    try:
        option: str = ''
        while option != '5':
            print("List of available options:")
            print(" 1: Add a recipe")
            print(" 2: Delete a recipe")
            print(" 3: Print a recipe")
            print(" 4: Print the cookbook")
            print(" 5: Quit")
            option = input("Select an option:\n")
            match option:
                case '1':
                    create_recipe()
                case '2':
                    delete_recipe(input("Recipe to detele:\n"))
                case '3':
                    print_recipe_details(input("Recipe to print:\n"))
                case '4':
                    print_cookbook_recipes()
                case '5':
                    break
                case _:
                    pass
    except (EOFError, KeyboardInterrupt):
        return
    

if __name__ == "__main__":
    main()