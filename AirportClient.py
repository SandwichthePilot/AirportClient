try:
    from telnetlib3 import theNULL
except ImportError:
    from telnetlib import theNULL

import pyttsx3

def text_to_speech(text):
    try:
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()

        # Set properties (optional)
        engine.setProperty("rate", 200)  # Speed of speech (words per minute)
        engine.setProperty("volume", 0.9)  # Volume level (0.0 to 1.0)

        # Convert the text to speech
        engine.say(text)

        # Wait for the speech to finish
        engine.runAndWait()

        # Return success flag
        return True
    except Exception as e:
        print(f"Exception in text_to_speech: {e}")
        return False

text_to_speech("AirportClient, version 1 dot 9 dot 6 loaded")
print("Thank you for using AirportClient, version 1.9.6 loaded")

def get_callsign():
    while True:
        text_to_speech("Calling aircraft, please define your callsign")
        callsign_input = input("ATC:" " Calling aircraft, please define your callsign: ")
        # Check if the input contains any non-empty text
        if callsign_input.strip():
            return callsign_input
        print("ATC: Unable to recognize callsign. Please try again.")

def get_position():
    while True:
        text_to_speech("Please report takeoff / landing")
        position_input = input("ATC: Takeoff/Landing: ")
        if position_input.strip():
            return position_input
        print("ATC: Unable to recognize request")

def get_aircraft():
    while True:
        text_to_speech("Please report aircraft type")
        aircraft_input = input("ATC: Please report aircraft type: ")
        if aircraft_input.strip():
            return aircraft_input
        print("ATC: Unable to regognize aircraft type. Please try again")
        

def get_gate():
    while True:
        text_to_speech("What will be your gate for today?")
        gate_input = input("ATC: What will be your gate for today: ")
        if gate_input.strip():
            return gate_input
        print("ATC: Are sure about that gate? Can not be recognized, try again!")

def get_type():
    while True:
        text_to_speech("What will be your aircrafts purpose today?")
        type_input = input("ATC: What is your aircraft purpose: ")
        if type_input.strip():
            return type_input
        print("ATC: Aircraft purpose is not recognized, try again!")

def get_location():
    while True:
        text_to_speech("Enter the I C A O code for the airport you are requesting")
        location_input = input("ATC: Enter the ICAO code for the airport you are requesting: ")
        if location_input.strip():
            return location_input
        print("ATC: Please confirm you entered the correct ICAO for the airport, try again!")

def get_flight():
    while True:
        text_to_speech("Please report your full flight plan")
        flight_input = input("ATC: Please report your full flight plan: ")
        if flight_input.strip():
            return flight_input
        print("ATC: Please review your flight plan to ensure it was correct, try again!")

def get_confirmation():
    while True:
        text_to_speech("Please, confirm all is correct")
        confirmation_input = input("Confirm all is correct: ")
        if confirmation_input.lower() != "no":
            return confirmation_input
        break
 
# possible
aircraft_callsign = get_callsign()
# (almost anything) ex: AC1089
position = get_position()
#landing/takeoff
aircraft = get_aircraft()
# (almost anything) ex: B787
gate = get_gate()
# (almost anything) ex: 1
type = get_type()
# Cargo/Passenger/Recreation/Undefined
location = get_location()
# (almost anything) ex: IRFD
flight = get_flight()
# (almost anything) ex: ITKO,IRFD
confirm = get_confirmation()
# Yes or no

def process_input(user_input, callsign):
    # Check if the callsign is present in the user input
    if callsign.lower() in user_input.lower():
        if "taxi" in user_input.lower():
            taxi
        elif "takeoff" in user_input.lower():
            return f"ATC: {callsign}, cleared for takeoff from runway {runway}"
        elif "requesting landing" in user_input.lower():
            return f"ATC: {callsign}, clear to land runway {runway}"
        elif "ils" in user_input.lower():
            return f"ATC: {callsign}, is clear to ils runway {runway}"         
        else:
            return f"ATC: {callsign}, I didn't understand your request. Please provide more details."
    else:
        return f"ATC: Unable to recognize callsign {callsign}. Please provide more details."
    
def taxi(user_input, callsign):
        if location == "IRFD" and gate == "1" and position == "takeoff":
            # If taking off at IRFD, provide taxi instructions to the runway
                text_to_speech("Taxi to runway 36 left via Gate one to Alpha three, Alpha three to Bravo, Bravo to Bravo one, Bravo one to Runway 36 left")
                print(f"ATC: {callsign}, Taxi to runway 36L, via Gate 1 to A3, A3 to B, B to B1, B1 to Runway 36L")
        elif location == "IRFD" and gate == "1" and position == "landing":
                text_to_speech("Taxi to gate one, right when able, cross 36 left to bravo, bravo to alpha 3, alpha 3 to gate 1")
                print(f"ATC: {callsign}, Taxi to gate 1, right when able, cross 36L to B, B to A3, A3 to gate 1")  
       
# Main loop to interact with the ATC
while True:
    user_input = input("Me: ")

    # Break the loop if the user says "bye"
    if user_input.lower() == "bye":
        print("ATC: Goodbye! Have a safe flight.")
        break

    # Get the ATC's response based on the user input and callsign
    response = process_input(user_input, aircraft_callsign)
    print(response)

    text_to_speech(response)