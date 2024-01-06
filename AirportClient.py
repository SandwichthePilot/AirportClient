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

def get_runway():
    while True:
        text_to_speech("please report your runway")
        runway_input = input("ATC: please report runway: ")
        if runway_input.strip():
            return runway_input
        print("ATC: Unable to regognize runway. Please try again")        

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
        text_to_speech("Enter the I C A O or eye at a code for the airport you are requesting")
        location_input = input("ATC: Enter the ICAO or IATA code for the airport you are requesting: ")
        if location_input.strip():
            return location_input
        print("ATC: Please confirm you entered the correct ICAO or IATA code for the airport, try again!")

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
runway = get_runway()
# runway 18L
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
            takeoff
        elif "landing" in user_input.lower():
            landing
        elif "ils" in user_input.lower():
            return f"ATC: {callsign}, is clear to ils runway {runway} direct {waypoint}"
        elif "pushback" in user_input.lower() and "start" in user_input.lower():
            pushback        
        else:
            return f"ATC: {callsign}, I didn't understand your request. Please provide more details."
    else:
        return f"ATC: Unable to recognize callsign {callsign}. Please provide more details."
    
def area():
    # Rockford
    if location == "IRFD" or "RFD":
        set; location("ChicagoRock")
    if location == "IMLR" or "MEL":
        set; location("ChicagoMel")
    if location == "IGAR" or "ABG":
        set; location("ChicagoAFB")
    if location == "ITRC" or "TRN":
        set; location("ChicagoTrain")
    if location == "IBLT" or "BOL":
        set; location("ChicagoBolt")
    # Tokyo
    if location == "ITKO" or "HND":
        set; location("TokyoInt")
    if location == "IDCS" or "SAB":
        set; location("TokyoOut")
    # Izolirani
    if location == "ISCM" or "SCT":
        set; location("NorsomAFB")
    if location == "IZOL" or "IZO":
        set; location("NorsomInt")
    if location == "IJAF" or "NJF":
        set; location("NorsomAl")
    # Grindavik
    if location == "IGRV" or "GVK":
        set; location("Keflavik")
    # Cyprus
    if location == "ILAR" or "LCA":
        set; location("LazarusLar")
    if location == "IBAR" or "BRR":
        set; location("LazarusBeach")
    if location == "IHEN" or "HEN":
        set; location("LazarusHen")
    if location == "IPAP" or "PFO":
        set; location("LazarusPap")
    # Skopelos
    if location == "ISKP" or "SKO":
        set; location("Skopelos")
    # Perth
    if location == "ILKL" or "LUA":
        set; location("PerthMount")
    if location == "IPPH" or "PER":
        set; location("PerthInt")
    # Saint Barthelemy
    if location == "IBTH" or "SBH":
        set; location("Sotaf")
    if location == "IUFO" or "UFO":
        set; location("UFO")
    # Sauthemptona
    if location == "ISAU" or "SAU":
        set; location("Brighton")
    # Carrier
    if location == "HMSQE" or "IDK":
        set; location("CarrierQueen")
    if location == "USSGRF" or "IDK":
        set; location("CarrierGRF")

def get_island():
    if location == "ChicagoRock" or "ChicagoMel" or "ChicagoAFB" or "ChicagoTrain" or "ChicagoBolt":
        set; island("Chicago")    
    if location == "TokyoInt" or "TokyoOut":
        set; island("Tokyo")
    if location == "NorsomAFB" or "NorsomInt" or "NorsomAl":
        set; island("Norsom")
    if location == "Keflavik":
        set; island("Keflavik")
    if location == "lazaruslar" or "LazarusBeach" or "LazarusHen" or "LazarusPap":
        set; island("Lazarus")
    if location == "Skopelos":
        set; island("Skopelos")
    if location == "PerthMount" or "PerthInt":
        set; island("Perth")
    if location == "Sotaf" or "UFO":
        set; island("Sotaf")
    if location == "Brighton":
        set; island("Brighton")

def airport():
    if location == "ChicagoRock":
        set_airport = "Greater Rockford"
        set_availible_airport = "Mellor"
        set_island = "Chicago"
    if location == "ChicagoMel":
        set_airport = "Mellor"
        set_availible_airport = "Greater Rockford"
        set_island = "Chicago"
    if location == "ChicagoAFB":
        set_airport = "Air Base Gary"
        set_availible_airport = "N/A"
        set_island = "Chicago"
    if location == "ChicagoTrain":
        set_airport = "Training Centre"
        set_availible_airport = "Mellor"
        set_island = "Chicago"
    if location == "ChicagoBolt":
        set_airport = "Boltic Airfield"
        set_availible_airport = "Mellor" or "Greater Rockford"
        set_island = "Chicago"
    if location == "TokyoInt":
        set_airport = "Tokyo International"
        set_availible_airport = "Saba"
        set_island = "Tokyo"    
    if location == "TokyoOut":
        set_airport = "Saba"
        set_availible_airport = "Tokyo International"
        set_island = "Tokyo"
    if location == "NorsomAFB":
        set_airport = "RAF Scampton"
        set_availible_airport = "N/A"
        set_island = "Norsom"
    if location == "NorsomInt":
        set_airport = "Izolirani"
        set_availible_airport = "Al Najaf"
        set_island = "Norsom"
    if location == "NorsomAl":
        set_airport = "Al Najaf"
        set_availible_airport = "Izolirani"
        set_island = "Norsom"
    if location == "Keflavik":
        set_airport = "Grindavik"
        set_availible_airport = "N/A"
        set_island = "Keflavik"
    if location == "LazarusLar":
        set_airport = "Larnaca International"
        set_availible_airport = "Paphos"
        set_island = "Lazarus"
    if location == "LazarusBeach":
        set_airport = "Barra"
        set_availible_airport = "Henstridge"
        set_island = "Lazarus"
    if location == "LazarusHen":
        set_airport = "Henstridge"
        set_availible_airport = "Paphos" or "Larnaca"
        set_island = "Lazarus"
    if location == "LazarusPap":
        set_airport = "Paphos"
        set_availible_airport = "Larnaca"
        set_island = "Lazarus"
    if location == "Skopelos":
        set_airport = "Skopelos"
        set_availible_airport = "N/A"
        set_island = "Skopelos"
    if location == "PerthMount":
        set_airport = "Lukla"
        set_availible_airport = "Perth International"
        set_island = "Perth"
    if location == "PerthInt":
        set_airport = "Perth International"
        set_availible_airport = "N/A"
        set_island = "Perth"
    if location == "Sotaf":
        set_airport = "Saint Barthelemy"
        set_availible_airport = "N/A"
        set_island = "Sotaf"
    if location == "UFO":
        set_airport = "UFO Airbase"
        set_availible_airport = "Saint Barthelemy"
        set_island = "Sotaf"
    if location == "Brighton":
        set_airport = "Sauthemptona"
        set_availible_airport = "N/A"
        set_island = "Brighton"
    if location == "CarrierQueen":
        set_airport = "HMS Queen Elizabeth"
        set_availible_airport = "N/A"
        set_island = "N/A"
    if location == "CarrierGRF":
        set_airport = "USS Gerald R. Ford"
        set_availible_airport = "N/A"
        set_island = "N/A"
    
def vor():
    if island == "Chicago":
        set_availible_vor = "TRAINING CENTRE","ROCKFORD","MELLOR","PEARSON"

def vortac():
    if location == "IRFD" or "IGAR" or "IMLR" or "ITRC" or "IBLT" or "ICRG" or "Chicago":
        set_availible_vortac = "KENNEDY","ROCKET","BLADES","LOGAN", 

def waypoint():
    if location == "IRFD" or "IGAR" or "IMLR" or "ITRC" or "IBLT" or "ICRG" or "Chicago":
        set_availible_waypoints = "ENDER","SETHR","JAMSI","RESTS","EASTN","PARTS","BEANS","WAREZ","HELPR","CRACK","INTER","DEATH","SAVES","STOOD"



def takeoff(user_input, callsign):
    if runway == "36l" and location == "IRFD":

def landing(user_input, callsign):
    if runway == "36l" and location == "IRFD":

def pushback(user_input, callsign):
        if gate == "1" or "2" or "3" or "4" or "5" and location == "IRFD" and runway == "36l" or "18l":
            text_to_speech(f"ATC: {callsign}, you are clear for push an start at {gate}, tail right")
            print(f"ATC: {callsign} clear for push and start {gate}, tail right")

def taxi(user_input, callsign):
        if location == "IRFD" and gate == "1" and position == "takeoff":
            # If taking off at IRFD, provide taxi instructions to the runway
                text_to_speech("Taxi to runway 36 left via Gate one to Alpha three, Alpha three to Bravo, Bravo to Bravo one, Bravo one to Runway 36 left")
                print(f"ATC: {callsign}, Taxi to runway 36L, via Gate 1 to A3, A3 to B, B to B1, B1 to Runway 36L")
        elif location == "IRFD" and gate == "1" and position == "landing":
                text_to_speech("Taxi to gate one, right when able, cross 36 left to bravo, bravo to alpha 3, alpha 3 to gate 1")
                print(f"ATC: {callsign}, Taxi to gate 1, right when able, cross 36L to B, B to A3, A3 to gate 1")
        elif location == "IRFD" and gate == "2":
       
# Main loop to interact with the ATC
while True:
    user_input = input("Me: ")

    # Break the loop if the user says "bye"
    if user_input.lower() == "bye" or "exit" or "g'day" or "good day":
        print(f"ATC: Goodnight have a safe flight.")
        break

    # Get the ATC's response based on the user input and callsign
    response = process_input(user_input, aircraft_callsign)
    print(response)

    text_to_speech(response)

# Extras
island = get_island()   
