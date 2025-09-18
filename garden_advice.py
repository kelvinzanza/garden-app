# garden_advice.py

# TODO: Add functions for cleaner code and reusability (to be done in Issue 2).
# TODO: Add documentation and comments (to be done in Issue 2).

# Advice dictionary to avoid hardcoding
advice_dict = {
    "summer": {
        "flower": "Water daily and provide shade in extreme heat.",
        "vegetable": "Ensure regular watering and harvest frequently."
    },
    "winter": {
        "flower": "Protect from frost and reduce watering.",
        "vegetable": "Use mulch and consider greenhouse protection."
    }
}

# Example inputs (inputs can be used later in code)
season = "summer"
plant_type = "flower"

# Get advice from dictionary
if season in advice_dict and plant_type in advice_dict[season]:
    print(advice_dict[season][plant_type])
else:
    print("No advice available for this combination.")