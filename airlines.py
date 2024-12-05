# Total airports list
airportList = ["airport1", "airport2", "airport3", "airport4", "airport5", "airport6"]

# Airplane capacity and model names 
model1 = [396, "Boeing 777"]
model2 = [350, "Airbus A350 XWB"]
model3 = [296, "Boeing 787 Dreamliner"]
model4 = [244, "Airbus A320 Family"]

# System dictionary - dictionary for all processes
sysDict = {
  "airport1": {
    "name":       "UAE - Dubai International Airport",
    "location":   "Dubai, United Arab Emirates",
    # Destination airports - excluded the origin airport
    "airport2": {
      "duration": 7.5,
      1: [12,  1, 2024,  4, model1, 400, 359],
      2: [12,  6, 2024,  6, model2, 410, 336],
      3: [12, 11, 2024,  8, model3, 420, 252],
      4: [12, 16, 2024, 10, model4, 430, 228],
      5: [12, 21, 2024, 12, model1, 400, 385],
      6: [12, 26, 2024, 14, model2, 410, 318]
    },
    "airport3": {
      "duration": 8,
      1: [12,  2, 2024, 16, model3, 520, 295],
      2: [12,  7, 2024, 18, model4, 530, 206],
      3: [12, 12, 2024, 20, model1, 500, 356],
      4: [12, 17, 2024, 22, model2, 510, 311],
      5: [12, 22, 2024, 24, model3, 520, 268],
      6: [12, 27, 2024,  2, model4, 530, 219]
    },
    "airport4": {
      "duration": 15,
      1: [12,  2, 2024, 16, model3, 520, 295],
      2: [12,  7, 2024, 18, model4, 530, 206],
      3: [12, 12, 2024, 20, model1, 500, 356],
      4: [12, 17, 2024, 22, model2, 510, 311],
      5: [12, 22, 2024, 24, model3, 520, 268],
      6: [12, 27, 2024,  2, model4, 530, 219]
    },
    "airport5": {
      "duration": 8.5,
      1: [12,  4, 2024, 16, model3, 420, 278],
      2: [12,  9, 2024, 18, model4, 430, 209],
      3: [12, 14, 2024, 20, model1, 400, 361],
      4: [12, 19, 2024, 22, model2, 410, 326],
      5: [12, 24, 2024, 24, model3, 420, 247],
      6: [12, 29, 2024,  2, model4, 430, 242]
    },
    "airport6": {
      "duration": 9.5,
      1: [12,  5, 2024,  4, model1, 600, 371],
      2: [12, 10, 2024,  6, model2, 610, 300],
      3: [12, 15, 2024,  8, model3, 620, 291],
      4: [12, 20, 2024, 10, model4, 630, 230],
      5: [12, 25, 2024, 12, model1, 600, 348],
      6: [12, 30, 2024, 14, model2, 610, 348]
    },
  },
  "airport2": {
    "name":       "CHN - Guangzhou Baiyun International Airport",
    "location":   "Guangdong Province, China",
    # Destination airports - excluded the origin airport
    "airport1": {
      "duration": 8,
      1: [12,  1, 2024,  8, model1, 400, 372],
      2: [12,  6, 2024, 10, model2, 410, 317],
      3: [12, 11, 2024, 12, model3, 420, 252],
      4: [12, 16, 2024, 14, model4, 430, 234],
      5: [12, 21, 2024, 16, model1, 400, 362],
      6: [12, 26, 2024, 18, model2, 410, 305]
    },
    "airport3": {
      "duration": 12,
      1: [12,  2, 2024, 20, model3, 720, 287],
      2: [12,  7, 2024, 22, model4, 730, 203],
      3: [12, 12, 2024, 24, model1, 700, 368],
      4: [12, 17, 2024,  2, model2, 710, 305],
      5: [12, 22, 2024,  4, model3, 720, 255],
      6: [12, 27, 2024,  6, model4, 730, 225]
    },
    "airport4": {
      "duration": 13,
      1: [12,  3, 2024,  8, model1, 700, 395],
      2: [12,  8, 2024, 10, model2, 710, 322],
      3: [12, 13, 2024, 12, model3, 720, 296],
      4: [12, 18, 2024, 14, model4, 730, 214],
      5: [12, 23, 2024, 16, model1, 700, 393],
      6: [12, 28, 2024, 18, model2, 710, 337]
    },
    "airport5": {
      "duration": 2.5,
      1: [12,  4, 2024, 20, model3, 170, 267],
      2: [12,  9, 2024, 22, model4, 180, 207],
      3: [12, 14, 2024, 24, model1, 150, 349],
      4: [12, 19, 2024,  2, model2, 160, 328],
      5: [12, 24, 2024,  4, model3, 170, 253],
      6: [12, 29, 2024, 10, model4, 830, 224]
    },
    "airport6": {
      "duration": 4.5,
      1: [12,  5, 2024,  8, model1, 300, 362],
      2: [12, 10, 2024, 10, model2, 310, 343],
      3: [12, 15, 2024, 12, model3, 320, 270],
      4: [12, 20, 2024, 14, model4, 330, 222],
      5: [12, 25, 2024, 16, model1, 300, 366],
      6: [12, 30, 2024, 22, model2, 810, 312]
    },
  },
  "airport3": {
    "name":       "GBR - London Heathrow Airport",
    "location":   "London, United Kingdom",
    # Destination airports - excluded the origin airport
    "airport1": {
      "duration": 7,
      1: [12,  1, 2024, 12, model1, 500, 396],
      2: [12,  6, 2024, 14, model2, 510, 323],
      3: [12, 11, 2024, 16, model3, 520, 273],
      4: [12, 16, 2024, 18, model4, 530, 240],
      5: [12, 21, 2024, 20, model1, 500, 357],
      6: [12, 26, 2024, 22, model2, 510, 340]
    },
    "airport2": {
      "duration": 11.5,
      1: [12,  2, 2024, 24, model3, 720, 246],
      2: [12,  7, 2024,  2, model4, 730, 200],
      3: [12, 12, 2024,  4, model1, 700, 352],
      4: [12, 17, 2024,  6, model2, 710, 301],
      5: [12, 22, 2024,  8, model3, 720, 260],
      6: [12, 27, 2024, 10, model4, 730, 204]
    },
    "airport4": {
      "duration": 11,
      1: [12,  3, 2024, 12, model1, 700, 385],
      2: [12,  8, 2024, 14, model2, 710, 339],
      3: [12, 13, 2024, 16, model3, 720, 254],
      4: [12, 18, 2024, 18, model4, 730, 233],
      5: [12, 23, 2024, 20, model1, 700, 351],
      6: [12, 28, 2024, 22, model2, 710, 301]
    },
    "airport5": {
      "duration": 14,
      1: [12,  4, 2024, 24, model3, 820, 290],
      2: [12,  9, 2024,  2, model4, 830, 208],
      3: [12, 14, 2024,  4, model1, 800, 349],
      4: [12, 19, 2024,  6, model2, 810, 333],
      5: [12, 24, 2024,  8, model3, 820, 258],
      6: [12, 29, 2024, 10, model4, 830, 224]
    },
    "airport6": {
      "duration": 11,
      1: [12,  5, 2024, 12, model1, 800, 375],
      2: [12, 10, 2024, 14, model2, 810, 300],
      3: [12, 15, 2024, 16, model3, 820, 283],
      4: [12, 20, 2024, 18, model4, 830, 220],
      5: [12, 25, 2024, 20, model1, 800, 392],
      6: [12, 30, 2024, 22, model2, 810, 312]
    },
  },
  "airport4": {
    "name":       "USA - Los Angeles International Airport",
    "location":   "California, USA",
    # Destination airports - excluded the origin airport
    "airport1": {
      "duration": 15,
      1: [12,  1, 2024, 16, model1, 900, 380],
      2: [12,  6, 2024, 18, model2, 910, 310],
      3: [12, 11, 2024, 20, model3, 920, 270],
      4: [12, 16, 2024, 22, model4, 930, 209],
      5: [12, 21, 2024, 24, model1, 900, 348],
      6: [12, 26, 2024,  2, model2, 910, 328]
    },
    "airport2": {
      "duration": 13,
      1: [12,  2, 2024,  4, model3, 720, 251],
      2: [12,  7, 2024,  6, model4, 730, 204],
      3: [12, 12, 2024,  8, model1, 700, 358],
      4: [12, 17, 2024, 10, model2, 710, 318],
      5: [12, 22, 2024, 12, model3, 720, 278],
      6: [12, 27, 2024, 14, model4, 730, 205]
    },
    "airport3": {
      "duration": 10.5,
      1: [12,  3, 2024, 16, model1, 600, 369],
      2: [12,  8, 2024, 18, model2, 610, 335],
      3: [12, 13, 2024, 20, model3, 620, 255],
      4: [12, 18, 2024, 22, model4, 630, 241],
      5: [12, 23, 2024, 24, model1, 600, 360],
      6: [12, 28, 2024,  2, model2, 610, 333]
    },
    "airport5": {
      "duration": 15,
      1: [12,  4, 2024,  4, model3, 620, 271],
      2: [12,  9, 2024,  6, model4, 630, 217],
      3: [12, 14, 2024,  8, model1, 600, 357],
      4: [12, 19, 2024, 10, model2, 610, 312],
      5: [12, 24, 2024, 12, model3, 620, 263],
      6: [12, 29, 2024, 14, model4, 630, 231]
    },
    "airport6": {
      "duration": 11,
      1: [12,  5, 2024, 16, model1, 800, 357],
      2: [12, 10, 2024, 18, model2, 810, 346],
      3: [12, 15, 2024, 20, model3, 820, 265],
      4: [12, 20, 2024, 22, model4, 830, 206],
      5: [12, 25, 2024, 24, model1, 800, 373],
      6: [12, 30, 2024,  2, model2, 810, 349]
    },
  },
  "airport5": {
    "name":       "PHL - Ninoy Aquino International Airport",
    "location":   "Manila, Philippines",
    # Destination airports - excluded the origin airport
    "airport1": {
      "duration": 8.5,
      1: [12,  1, 2024, 20, model1, 400, 357],
      2: [12,  6, 2024, 22, model2, 410, 315],
      3: [12, 11, 2024, 24, model3, 420, 286],
      4: [12, 16, 2024,  2, model4, 430, 219],
      5: [12, 21, 2024,  4, model1, 400, 368],
      6: [12, 26, 2024,  6, model2, 410, 317]
    },
    "airport2": {
      "duration": 2.5,
      1: [12,  2, 2024,  8, model3, 170, 277],
      2: [12,  7, 2024, 10, model4, 180, 236],
      3: [12, 12, 2024, 12, model1, 150, 370],
      4: [12, 17, 2024, 14, model2, 160, 309],
      5: [12, 22, 2024, 16, model3, 170, 289],
      6: [12, 27, 2024, 18, model4, 180, 233]
    },
    "airport3": {
      "duration": 14,
      1: [12,  3, 2024, 20, model1, 800, 377],
      2: [12,  8, 2024, 22, model2, 810, 304],
      3: [12, 13, 2024, 24, model3, 820, 262],
      4: [12, 18, 2024,  2, model4, 830, 195],
      5: [12, 23, 2024,  4, model1, 800, 369],
      6: [12, 28, 2024,  6, model2, 810, 324]
    },
    "airport4": {
      "duration": 12,
      1: [12,  4, 2024,  8, model3, 820, 274],
      2: [12,  9, 2024, 10, model4, 830, 243],
      3: [12, 14, 2024, 12, model1, 800, 349],
      4: [12, 19, 2024, 14, model2, 810, 323],
      5: [12, 24, 2024, 16, model3, 820, 276],
      6: [12, 29, 2024, 18, model4, 830, 199]
    },
    "airport6": {
      "duration": 4.5,
      1: [12,  5, 2024, 20, model1, 300, 391],
      2: [12, 10, 2024, 22, model2, 310, 344],
      3: [12, 15, 2024, 24, model3, 320, 283],
      4: [12, 20, 2024,  2, model4, 330, 242],
      5: [12, 25, 2024,  4, model1, 300, 394],
      6: [12, 30, 2024,  6, model2, 310, 332]
    },
  },
  "airport6": {
    "name":       "JPN - Tokyo Haneda Airport",
    "location":   "Tokyo, Japan",
    # Destination airports - excluded the origin airport
    "airport1": {
      "duration": 10,
      1: [12,  1, 2024, 24, model1, 600, 365],
      2: [12,  6, 2024,  2, model2, 610, 303],
      3: [12, 11, 2024,  4, model3, 620, 253],
      4: [12, 16, 2024,  6, model4, 630, 196],
      5: [12, 21, 2024,  8, model1, 600, 361],
      6: [12, 26, 2024, 10, model2, 610, 349]
    },
    "airport2": {
      "duration": 4.5,
      1: [12,  2, 2024, 12, model3, 320, 255],
      2: [12,  7, 2024, 14, model4, 330, 241],
      3: [12, 12, 2024, 16, model1, 300, 396],
      4: [12, 17, 2024, 18, model2, 310, 312],
      5: [12, 22, 2024, 20, model3, 320, 267],
      6: [12, 27, 2024, 22, model4, 330, 223]
    },
    "airport3": {
      "duration": 12,
      1: [12,  3, 2024, 24, model1, 800, 351],
      2: [12,  8, 2024,  2, model2, 810, 321],
      3: [12, 13, 2024,  4, model3, 820, 247],
      4: [12, 18, 2024,  6, model4, 830, 242],
      5: [12, 23, 2024,  8, model1, 800, 367],
      6: [12, 28, 2024, 10, model2, 810, 345]
    },
    "airport4": {
      "duration": 10.5,
      1: [12,  4, 2024, 12, model3, 720, 283],
      2: [12,  9, 2024, 14, model4, 730, 234],
      3: [12, 14, 2024, 16, model1, 700, 352],
      4: [12, 19, 2024, 18, model2, 710, 333],
      5: [12, 24, 2024, 20, model3, 720, 283],
      6: [12, 29, 2024, 22, model4, 730, 212]
    },
    "airport5": {
      "duration": 0,
      1: [12,  5, 2024, 24, model1, 300, 380],
      2: [12, 10, 2024,  2, model2, 310, 346],
      3: [12, 15, 2024,  4, model3, 320, 246],
      4: [12, 20, 2024,  6, model4, 330, 241],
      5: [12, 25, 2024,  8, model1, 300, 364],
      6: [12, 30, 2024, 10, model2, 310, 349]
    }
  },
  "class": {
    1: ["Economy Class",  "ECLASS",   1],
    2: ["Business Class", "BCLASS", 1.5],
    3: ["First Class",    "FCLASS", 2.5]
  }
}

# Function for getting the chosen route
def getRoute():
  global origin, destination, route
  # Welcome and prompt message
  print("\n\n\n✈️  Hello and Welcome to Python Ticketing Airlines!🌍" +
        f"\n{"_" * 70}" +
        "\n\n📍 Here are the available airports:")
  # Prints all the choices
  for n in range(len(airportList)):
    print(f"   {n + 1}. {sysDict[airportList[n]]["name"]}")
  # Prompt for restarting the system
  print("\n   Type 'X' to restart the selection.")
  # Loop for user input
  while True:
    # Error handling for user input
    try:
      # Request for user input
      inputORG = input(f"\n>> 📋 Choose an ORIGIN airport (1-{len(airportList)}): ")
      # Check if input is in range of choices
      if 1 <= int(inputORG) <= len(airportList):
        # Store the input in a variable
        origin = airportList[int(inputORG) - 1]
        # Feedback message
        print(f">> 🛫 Origin Airport: {sysDict[origin]["name"]}")
        break
      else:
        # Error when the input is not in range of choices
        print(">> ❌ Invalid Input! Please enter a number in range of choices!")
    except Exception as e:
      # Restarts the program
      if inputORG.lower() == "x": return True
      # Error when the input is not a number
      print(f">> ❌ Invalid Input: {e}")
  # Loop for user input
  while True:
    # Error handling for user input
    try:
      # Request for user input
      inputDST = input(f"\n>> 📋 Choose a DESTINATION airport (1-{len(airportList)}): ")
      # Check if input is in range of choices
      if inputDST == inputORG:
        print(">> ❌ Invalid Input! Cannot select origin as destination!")
      elif 1 <= int(inputDST) <= len(airportList):
        # Store the input in a variable
        destination = airportList[int(inputDST) - 1]
        # Feedback message
        print(f">> 🛬 Destination Airport: {sysDict[destination]["name"]}")
        break
      else:
        # Error when the input is not in range of choices
        print(">> ❌ Invalid Input! Please enter a number in range of choices!")
    except Exception as e:
      # Restarts the program
      if inputDST.lower() == "x": return True
      # Error when the input is not a number
      print(f">> ❌ Invalid Input: {e}")
  # Set the route variable for future uses
  route = sysDict[origin][destination]
  duration = "⌛ Flight Duration: ~ " + str(route["duration"]) + " Hours"
  print(f"\n   +------------------------------------------------------+" +
        f"\n   | {"🗺️  Flight Route:":^53} |" +
        f"\n   +------+-----------------------------------------------+" +
        f"\n   | {"From":^4} | {sysDict[origin]["name"]:<45} |" +
        f"\n   |      | {sysDict[origin]["location"]:<45} |" +
        f"\n   +------+-----------------------------------------------+" +
        f"\n   | {"To":^4} | {sysDict[destination]["name"]:<45} |" +
        f"\n   |      | {sysDict[destination]["location"]:<45} |" +
        f"\n   +------+-----------------------------------------------+" +
        f"\n   | {duration:^51} |" +
        f"\n   +------------------------------------------------------+" +
        f"\n{"_" * 70}")

# Function to compute for the date of the flight
calcDate = lambda x : f"{x[0]:02d}/{x[1]:02d}/{x[2]}"

# Function to compute for the take-off time of the flight schedule
def calcTime(x):
  # Converts number into time
  if x[3] == 24:
    return f"12:00 AM"
  elif x[3] == 12:
    return f"12:00 PM"
  hr = x[3] // 1
  mn = (x[3] - hr) * 60
  hr = f"{int(hr):02d}"
  mn = f"{int(mn):02d}"
  if x[3] > 12:
    return f"{hr}:{mn} PM"
  elif x[3] < 12:
    return f"{hr}:{mn} AM"

# Function to compute for the flight schedule seats
def calcSeats(x):
  if x[6] == x[4][0]: return "❌ FULL"
  else: return f"{x[6]}/{x[4][0]}"
  
# Fucntion to get the chosen flight schedule
def getSchedule():
  global schedule
  # Prompt message
  print(f"\n   🛫 Flight Schedules:\n")
  # Prints all choices
  for n in range(len(route) - 1):
    n += 1
    sched = route[n]
    cost = f"Cost: ${sched[5]:.2f}"
    print(f"    {n}.   {calcDate(sched)} - {calcTime(sched)}    {sched[4][1]:^24}" +
          f"\n         {cost:^21}    {calcSeats(sched):^24}\n")
  # Prompt for restarting the system
  print("   Type 'X' to restart the selection.")
  # Loop for user input
  while True:
    # Error handling for user input
    try:
      # Request for user input
      inputFlightSchedule = input(f"\n>> 📋 Choose a FLIGHT SCHEDULE (1-{len(route) - 1}): ")
      # Check if input is in range of choices
      if 1 <= int(inputFlightSchedule) <= len(route) - 1:
        # Sets the schedule from the input
        schedule = route[int(inputFlightSchedule)]
        # Checks if the chosen schedule is full or not
        if schedule[6] == schedule[4][0]:
          # Error when the schedule is full
          print(">> ❌ Invalid Input! Chosen flight schedule is full!")
          continue
        else:
          # Feedback message of the chosen flight schedule
          print(f">> 🛫 Flight Schedule: {calcDate(schedule)} - {calcTime(schedule)}" +
                f"\n{"_" * 70}")
          break
    except Exception as e:
      # Restarts the program
      if inputFlightSchedule.lower() == "x": return True
      # Error when the input is not a number
      print(f">> ❌ Invalid Input: {e}")

# Function the get the ticket class and the amount
def getTicket():
  global ticketClass, ticketAmount
  # Prompt message
  print("\n   📍 Choose a TICKET CLASS:\n")
  # Prints all choices
  for n in range(len(sysDict["class"])):
    n += 1
    ticketClass = sysDict["class"][n]
    print(f"   {n}. {ticketClass[0]} ({ticketClass[2]}x)" +
          f"\n      Cost per Ticket: ${schedule[5] * ticketClass[2]:.2f}\n")
  # Prompt for restarting the system
  print("   Type 'X' to restart the selection.")
  # Error handling for user input
  while True:
    try:
      # Request for user input
      inputTicketClass = input(f"\n>> 📋 Choose a TICKET CLASS (1-{len(ticketClass)}): ")
      # Check if input is in range of choices
      if 1 <= int(inputTicketClass) <= len(ticketClass):
        # Sets the ticket class from the input
        ticketClass = sysDict["class"][int(inputTicketClass)]
        # Feedback message of the chosen ticket class
        print(f">> 🎫 Ticket Class: {ticketClass[0]}")
        break
    except Exception as e:
      # Restarts the program
      if inputTicketClass.lower() == "x": return True
      # Error when the input is not a number
      print(f">> ❌ Invalid Input: {e}")
  seatsLeft = schedule[4][0] - schedule[6]
  # Error handling for user input
  while True:
    try:
      # Request for user input
      inputTicketAmount = input(f"\n>> 📋 Enter TICKET AMOUNT ({seatsLeft} left): ")
      # Check if input is in range of choices
      if 1 <= int(inputTicketAmount) <= seatsLeft:
        # Sets the ticket amount from the input
        ticketAmount = int(inputTicketAmount)
        # Feedback message of the chosen ticket class
        print(f">> 🎫 Ticket Amount: {ticketAmount}" +
              f"\n{"_" * 70}")
        break
    except Exception as e:
      # Restarts the program
      if inputTicketAmount.lower() == "x": return True
      # Error when the input is not a number
      print(f">> ❌ Invalid Input: {e}")

# Function to get payment from the user
def getPayment():
  totalCost = ticketClass[2] * ticketAmount * schedule[5]
  print("\n🎫 Ticket Details:" +
        f"\n   - Ticket Cost:     ${schedule[5]:.2f}"
        f"\n   - Ticket Class:    {ticketClass[0]}" +
        f"\n   - Ticket Amount:   {ticketAmount}" +
        f"\n   - Total Cost:      ${totalCost:.2f}" +
        f"\n{"_" * 70}")
   # Error handling for user input
  while True:
    try:
      # Request for user input
      inputPaymentAmount = input(f"\n>> 💵 Enter PAYMENT AMOUNT: $")
      # Check if input is greater than total cost
      if float(inputPaymentAmount) >= totalCost:
        # Sets the payment amount from the input
        paymentAmount = float(inputPaymentAmount)
        # Feedback message of the chosen ticket class
        print(f">> 🎫 Change Amount: {paymentAmount - totalCost}" +
              f"\n{"_" * 70}")
        break
    except Exception as e:
      # Restarts the program
      if inputPaymentAmount.lower() == "x": return True
      # Error when the input is not a number
      print(f">> ❌ Invalid Input: {e}")

while True:
  if getRoute(): continue
  if getSchedule(): continue
  if getTicket(): continue
  if getPayment(): continue