import pymongo
from bson.objectid import ObjectId

# Підключення до MongoDB
try:
    client = pymongo.MongoClient(
        "mongodb+srv://user:user1@cluster0.obudsmi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    )
    db = client["homework"]  # Назва бази даних
    collection = db["cats"]  # Назва колекції
except pymongo.errors.ConnectionFailure:
    print("Не вдалося підключитися до сервера MongoDB. Перевірте, чи він запущений.")


# Функція для виведення всіх записів із колекції
def read_all_cats():
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        print(f"Помилка під час зчитування котів: {e}")


# Функція для виведення інформації про кота за ім'ям
def read_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print("Кіт з таким ім'ям не знайдено")
    except Exception as e:
        print(f"Помилка під час зчитування кота за ім'ям: {e}")


# Функція для оновлення віку кота за ім'ям
def update_cat_age(name, new_age):
    try:
        collection.update_one({"name": name}, {"$set": {"age": new_age}})
        print("Вік кота оновлено")
    except Exception as e:
        print(f"Помилка під час оновлення віку кота: {e}")


# Функція для додавання нової характеристики до списку features кота за ім'ям
def add_feature_to_cat(name, new_feature):
    try:
        collection.update_one({"name": name}, {"$push": {"features": new_feature}})
        print("Характеристику кота оновлено")
    except Exception as e:
        print(f"Помилка під час додавання характеристики до кота: {e}")


# Функція для видалення запису з колекції за ім'ям тварини
def delete_cat_by_name(name):
    try:
        collection.delete_one({"name": name})
        print("Кіт видалено")
    except Exception as e:
        print(f"Помилка під час видалення кота: {e}")


# Функція для видалення всіх записів із колекції
def delete_all_cats():
    try:
        collection.delete_many({})
        print("Усіх котів видалено")
    except Exception as e:
        print(f"Помилка під час видалення усіх котів: {e}")


if __name__ == "__main__":
    # Приклад використання функцій
    read_all_cats()
    read_cat_by_name("barsik")
    update_cat_age("barsik", 4)
    add_feature_to_cat("barsik", "дружелюбний")
    delete_cat_by_name("tom")
    delete_all_cats()
