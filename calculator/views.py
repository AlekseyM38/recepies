from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'burger': {
        'хлеб, ломтик': 1,
        'котлета, ломтик': 1,
        'сыр, ломтик': 2,
        'помидор, ломтик': 2,
        'лук, ломтик': 3,
    },
    # можете добавить свои рецепты ;)
}


def recipe_view(request, recipe_name):
    servings = int(request.GET.get('servings', 1))  # По умолчанию одна порция
    recipe_data = DATA.get(recipe_name, {})  # Получаем данные для указанного рецепта
    scaled_recipe = {}  # Создаем пустой словарь для масштабированного рецепта

    # Масштабируем рецепт по количеству порций
    for ingredient, amount in recipe_data.items():
        scaled_recipe[ingredient] = amount * servings

    # Передаем данные рецепта в контекст шаблона
    context = {
        'recipe': scaled_recipe
    }

    # Отображаем шаблон с контекстом
    return render(request, 'calculator/index.html', context)
