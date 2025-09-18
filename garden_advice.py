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


season = "summer"
plant_type = "flower"

if season in advice_dict and plant_type in advice_dict[season]:
    print(advice_dict[season][plant_type])
else:
    print("No advice available for this combination.")