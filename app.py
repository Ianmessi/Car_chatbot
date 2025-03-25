from flask import Flask, render_template, request
from fuzzywuzzy import process
import re

# Dictionary of car problems with their causes and solutions
car_issues = {
    "car won't start": {
        "cause": "The battery might be dead or the starter motor could be faulty.",
        "solution": "Try jump-starting the car or replacing the battery. If the starter motor is faulty, it may need replacement."
    },
    "engine overheating": {
        "cause": "Low coolant levels, a faulty thermostat, or a broken water pump could be the cause.",
        "solution": "Check the coolant levels and top it up if necessary. If the thermostat or water pump is faulty, it might need repair or replacement."
    },
    "strange noise from the engine": {
        "cause": "This could be caused by a loose belt, worn-out brake pads, or an issue with the alternator.",
        "solution": "Inspect the belts for tightness, check the brake pads, or have the alternator checked by a professional."
    },
    "brake failure": {
        "cause": "Worn brake pads or low brake fluid could lead to brake failure.",
        "solution": "Replace the brake pads and check the brake fluid levels. If the problem persists, get the brake system inspected."
    },
    "car shaking while driving": {
        "cause": "Misaligned wheels, unbalanced tires, or suspension issues could be the cause.",
        "solution": "Get the tires balanced, check the wheel alignment, or have the suspension system inspected."
    },
    "smoking exhaust": {
        "cause": "This could indicate an engine oil leak, coolant leak, or an issue with the catalytic converter.",
        "solution": "Have the engine oil and coolant levels checked. If the catalytic converter is faulty, it may need to be replaced."
    },
    "check engine light on": {
        "cause": "Could be due to various issues including loose gas cap, faulty oxygen sensor, or catalytic converter problems.",
        "solution": "First check if the gas cap is loose. If not, use an OBD scanner to read the specific error code and address accordingly."
    },
    "rough idle": {
        "cause": "Dirty fuel injectors, spark plug issues, or vacuum leaks could cause rough idling.",
        "solution": "Clean or replace fuel injectors, check and replace spark plugs, or inspect for vacuum leaks."
    },
    "transmission slipping": {
        "cause": "Low transmission fluid, worn clutch, or transmission wear could be the cause.",
        "solution": "Check transmission fluid levels, inspect clutch wear, or have transmission checked by a professional."
    },
    "steering wheel vibration": {
        "cause": "Unbalanced tires, warped brake rotors, or suspension issues could cause vibration.",
        "solution": "Balance tires, check brake rotors, or inspect suspension components."
    },
    "poor fuel economy": {
        "cause": "Dirty air filter, underinflated tires, or faulty oxygen sensor could reduce fuel efficiency.",
        "solution": "Replace air filter, check tire pressure, or replace oxygen sensor if needed."
    },
    "hard to shift gears": {
        "cause": "Low transmission fluid, worn clutch, or transmission linkage issues.",
        "solution": "Check transmission fluid, inspect clutch, or adjust transmission linkage."
    },
    "car pulling to one side": {
        "cause": "Uneven tire pressure, misaligned wheels, or brake caliper issues.",
        "solution": "Check tire pressure, get wheel alignment, or inspect brake calipers."
    },
    "squealing brakes": {
        "cause": "Worn brake pads, glazed rotors, or brake dust buildup.",
        "solution": "Replace brake pads, resurface or replace rotors, or clean brake components."
    },
    "engine knocking": {
        "cause": "Low oil pressure, incorrect fuel octane, or engine timing issues.",
        "solution": "Check oil pressure, use correct fuel grade, or have engine timing checked."
    },
    "dead battery": {
        "cause": "Old battery, parasitic drain, or alternator issues.",
        "solution": "Replace battery, check for electrical drains, or repair alternator."
    },
    "clogged air filter": {
        "cause": "Dirt and debris buildup over time.",
        "solution": "Clean or replace the air filter regularly."
    },
    "faulty alternator": {
        "cause": "Worn brushes, bad bearings, or voltage regulator issues.",
        "solution": "Replace alternator or repair specific components."
    },
    "leaking oil": {
        "cause": "Worn gaskets, loose oil filter, or damaged oil pan.",
        "solution": "Replace gaskets, tighten oil filter, or repair oil pan."
    },
    "power steering problems": {
        "cause": "Low power steering fluid, worn pump, or leaking hoses.",
        "solution": "Check fluid levels, replace pump, or repair hoses."
    },
    "AC not working": {
        "cause": "Low refrigerant, faulty compressor, or electrical issues.",
        "solution": "Recharge refrigerant, replace compressor, or check electrical connections."
    },
    "headlights dim": {
        "cause": "Weak battery, alternator issues, or corroded connections.",
        "solution": "Check battery and alternator, clean connections, or replace bulbs."
    },
    "exhaust rattle": {
        "cause": "Loose heat shield, broken hanger, or rusted components.",
        "solution": "Tighten heat shield, replace hanger, or repair exhaust system."
    },
    "dashboard warning lights": {
        "cause": "Various system issues indicated by different warning lights.",
        "solution": "Check owner's manual for specific light meaning and address accordingly."
    },
    "car smells like gas": {
        "cause": "Fuel leak, loose gas cap, or rich fuel mixture.",
        "solution": "Check for leaks, tighten gas cap, or adjust fuel mixture."
    },
    "water leak inside car": {
        "cause": "Clogged sunroof drains, damaged weather stripping, or windshield seal issues.",
        "solution": "Clean drains, replace weather stripping, or reseal windshield."
    },
    "radio not working": {
        "cause": "Blown fuse, wiring issues, or faulty head unit.",
        "solution": "Check fuses, inspect wiring, or replace radio unit."
    },
    "window stuck": {
        "cause": "Broken regulator, motor issues, or switch problems.",
        "solution": "Replace window regulator, repair motor, or fix switch."
    },
    "door won't lock": {
        "cause": "Broken actuator, wiring issues, or key fob problems.",
        "solution": "Replace actuator, check wiring, or reprogram key fob."
    },
    "horn not working": {
        "cause": "Blown fuse, broken horn, or steering wheel contact issues.",
        "solution": "Check fuses, replace horn, or repair steering wheel contacts."
    }
}

app = Flask(__name__)

def preprocess_text(text):
    # Convert to lowercase, remove special characters, and normalize whitespace
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = ' '.join(text.split())
    return text

def find_best_match(user_input, threshold=60):
    # Find the best matching car issue using fuzzy matching
    processed_input = preprocess_text(user_input)
    issues = list(car_issues.keys())
    best_match = process.extractOne(processed_input, issues)
    
    if best_match and best_match[1] >= threshold:
        return best_match[0]
    return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    matched_issue = find_best_match(user_input)
    
    if matched_issue:
        cause = car_issues[matched_issue]["cause"]
        solution = car_issues[matched_issue]["solution"]
        return f"Cause: {cause}\nSolution: {solution}"
    else:
        return "Sorry, I don't have information on that problem. Please consult a mechanic for further assistance."

if __name__ == "__main__":
    app.run(debug=True)
