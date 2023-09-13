import csv

def greet():
    print("Welcome to Exercise Recommendator by Anar Otgonbaatar")

def get_type(what = "", dict = {}):
    cur_type = ""
    print(f"Choose your {what}:")
    while cur_type not in dict.values():
        for key, level in dict.items():
            print(f"{key}: {level}")
        level_key = int(input("Input: "))
        if level_key in dict:
            cur_type = dict[level_key]
            print(f"Your {what}: {cur_type}\n")
        else: 
            print("Invalid input. Try Again.")
    return cur_type

def prep_csv():
    csv_file_path = "exercises.csv"
    exercises_dict = {}

    with open(csv_file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            exercise_name = row["Exercise Name"]
            exercises_dict[exercise_name] = {
                "Muscle Group": row["Muscle Group"],
                "Equipment Type": row["Equipment Type"],
                "Type": row["Type"]
            }
    
    return exercises_dict

def recommend(dict, muscle, equipment, type):
    print(f"Recommending {equipment} {type} exercises for your {muscle}:")
    recommended_exercises = []

    for name, attributes in dict.items():
        if (
        attributes["Muscle Group"].lower() == muscle.lower()
        and attributes["Equipment Type"].lower() == equipment.lower()
        and attributes["Type"].lower() == type.lower()
        ):
            recommended_exercises.append(name)
            
    if recommended_exercises:
        i = 1
        for exercise in recommended_exercises:
            print(f"{i}: {exercise}")   # List out the recommended exercises to terminal
            i += 1
        print("End of recommendation.\n")
    else: print("Sorry, there is no exercises based on your preferences yet.")
    


def initialize():
    exercise_dict = prep_csv()

    equipment_types = {1: "Free Weight", 2: "Machine", 3: "Body Weight"}
    exercise_types = {1: "Isolation", 2: "Compound", 3: "Cardio"}
    muscle_groups = {1: "Calves", 2: "Chest", 3: "Delts", 4: "Traps", 5: "Lats", 6: "Abs", 7: "Back", 8: "Glutes", 9: "Quads", 10: "Hamstrings",  11: "Triceps", 12: "Biceps", 13: "Forearms"}

    cur_eqmpt_type = ""
    cur_exercise_type = ""
    cur_muscle_group = ""

    # Get user's preferences
    cur_muscle_group = get_type("muscle group", muscle_groups)
    cur_exercise_type = get_type("exercise type", exercise_types)
    cur_eqmpt_type = get_type("equipment type", equipment_types)

    recommend(exercise_dict, cur_muscle_group, cur_eqmpt_type, cur_exercise_type)

    again = input("Go again? y/n: ")
    if again == 'y':
        initialize()
    else: print('Thanks for using Exercise Recommendator!\n')

greet()
initialize()