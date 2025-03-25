import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define common car issues
car_issues = {
    "overheating": "Possible causes: Low coolant, faulty radiator, or thermostat issue. Solution: Check coolant levels and radiator.",
    "engine noise": "Possible causes: Low oil, worn engine parts. Solution: Check oil level and visit a mechanic if the noise continues.",
    "battery dead": "Possible causes: Faulty alternator, old battery. Solution: Jump-start the car and check battery health.",
    "brakes not working": "Possible causes: Worn brake pads, low brake fluid. Solution: Check brake fluid level and replace brake pads if needed.",
    "car not starting": "Possible causes: Dead battery, faulty starter. Solution: Check battery charge and starter motor.",
}

def detect_issue(user_input):
    """Processes user input and finds a matching car issue."""
    doc = nlp(user_input.lower())

    for issue in car_issues:
        if issue in doc.text:
            return car_issues[issue]
    
    return "I'm not sure. Please check with a mechanic."

# Test the chatbot
if __name__ == "__main__":
    while True:
        user_input = input("Describe your car issue: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = detect_issue(user_input)
        print("Chatbot:", response)

