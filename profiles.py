from .db import personal_data_collection, notes_collection

def get_values(_id):
    return {
        "_id": _id,
        "general": {
            "name": "",
            "age": 30,
            "weight": 60,
            "height": 165,
            "activity_level": "Moderately Active",
            "gender": "Male"
    },
    "goals": ['Muscle Gain'],
    "nutrition": {
        "calories": 2000,
        "protein": 140,
        "fat": 20,
        "carbs": 100
    },

}