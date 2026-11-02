import requests

def search_trains(source: str, destination: str, date: str):
    """
    Simulates or calls an API to fetch trains between two stations.
    Replace this with a real RapidAPI IRCTC endpoint if available.
    """
    # Example placeholder logic or real API call
    # url = f"https://irctc1.p.rapidapi.com/api/v1/searchTrain?queryFrom={source}&queryTo={destination}"
    
    # Mock response for testing your LLM flow:
    sample_trains = [
        {"train_no": "12657", "name": "Mailaduthurai Express", "dep": "06:10", "arr": "11:00", "classes": ["1A", "2A", "3A", "SL"]},
        {"train_no": "12639", "name": "Brindavan Express", "dep": "07:40", "arr": "12:30", "classes": ["CC", "2S"]}
    ]
    return sample_trains