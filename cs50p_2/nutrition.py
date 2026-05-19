calorie = {
  "apples" : 130,
  "avocado" : 50,
  "banana" : 110,
  "cantaloupe" : 50,
  "grapefruit" : 60,
  "grapes" : 90,
  "honeydew" : 50,
  "kiwifruit": 90,
  "lemon" : 15,
  "lime" : 20,
  "nectarine" : 60,  
}

fruit = input("Item: ").lower()
if fruit in calorie:
    print(f"Calories: {calorie[fruit]}")