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
      "flight1": [12,  1, 2024,  8, model1, 400, 372],
      2: [12,  6, 2024, 10, model2, 410, 317],
      3: [12, 11, 2024, 12, model3, 420, 252],
      4: [12, 16, 2024, 14, model4, 430, 234],
      5: [12, 21, 2024, 16, model1, 400, 362],
      6: [12, 26, 2024, 18, model2, 410, 305]
    },
    "airport3": {
      "duration": 12,
      "flight1": [12,  2, 2024, 20, model3,   12, 720, 287],
      2: [12,  7, 2024, 22, model4,   12, 730, 203],
      3: [12, 12, 2024, 24, model1,   12, 700, 368],
      4: [12, 17, 2024,  2, model2,   12, 710, 305],
      5: [12, 22, 2024,  4, model3,   12, 720, 255],
      6: [12, 27, 2024,  6, model4,   12, 730, 225]
    },
    "airport4": {
      "duration": 13,
      "flight1": [12,  3, 2024,  8, model1, 700, 395],
      2: [12,  8, 2024, 10, model2, 710, 322],
      3: [12, 13, 2024, 12, model3, 720, 296],
      4: [12, 18, 2024, 14, model4, 730, 214],
      5: [12, 23, 2024, 16, model1, 700, 393],
      6: [12, 28, 2024, 18, model2, 710, 337]
    },
    "airport5": {
      "duration": 2.5,
      "flight1": [12,  4, 2024, 20, model3,  2.5, 170, 267],
      2: [12,  9, 2024, 22, model4,  2.5, 180, 207],
      3: [12, 14, 2024, 24, model1,  2.5, 150, 349],
      4: [12, 19, 2024,  2, model2,  2.5, 160, 328],
      5: [12, 24, 2024,  4, model3,  2.5, 170, 253],
      6: []
    },
    "airport6": {
      "duration": 4.5,
      "flight1": [12,  5, 2024,  8, model1, 300, 362],
      2: [12, 10, 2024, 10, model2, 310, 343],
      3: [12, 15, 2024, 12, model3, 320, 270],
      4: [12, 20, 2024, 14, model4, 330, 222],
      5: [12, 25, 2024, 16, model1, 300, 366],
      6: []
    },
  },
  "airport3": {
    "name":       "GBR - London Heathrow Airport",
    "location":   "London, United Kingdom",
    # Destination airports - excluded the origin airport
    "airport1": {
      "duration": 7,
      "flight1": [12,  1, 2024, 12, model1, 500, 396],
      2: [12,  6, 2024, 14, model2, 510, 323],
      3: [12, 11, 2024, 16, model3, 520, 273],
      4: [12, 16, 2024, 18, model4, 530, 240],
      5: [12, 21, 2024, 20, model1, 500, 357],
      6: [12, 26, 2024, 22, model2, 510, 340]
    },
    "airport2": {
      "duration": 11.5,
      "flight1": [12,  2, 2024, 24, model3, 720, 246],
      2: [12,  7, 2024,  2, model4, 730, 200],
      3: [12, 12, 2024,  4, model1, 700, 352],
      4: [12, 17, 2024,  6, model2, 710, 301],
      5: [12, 22, 2024,  8, model3, 720, 260],
      6: [12, 27, 2024, 10, model4, 730, 204]
    },
    "airport4": {
      "duration": 11,
      "flight1": [12,  3, 2024, 12, model1, 700, 385],
      2: [12,  8, 2024, 14, model2, 710, 339],
      3: [12, 13, 2024, 16, model3, 720, 254],
      4: [12, 18, 2024, 18, model4, 730, 233],
      5: [12, 23, 2024, 20, model1, 700, 351],
      6: [12, 28, 2024, 22, model2, 710, 301]
    },
    "airport5": {
      "duration": 14,
      "flight1": [12,  4, 2024, 24, model3, 820, 290],
      2: [12,  9, 2024,  2, model4, 830, 208],
      3: [12, 14, 2024,  4, model1, 800, 349],
      4: [12, 19, 2024,  6, model2, 810, 333],
      5: [12, 24, 2024,  8, model3, 820, 258],
      6: [12, 29, 2024, 10, model4, 830, 224]
    },
    "airport6": {
      "duration": 11,
      "flight1": [12,  5, 2024, 12, model1, 800, 375],
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
      "flight1": [12,  1, 2024, 16, model1, 900, 380],
      2: [12,  6, 2024, 18, model2, 910, 310],
      3: [12, 11, 2024, 20, model3, 920, 270],
      4: [12, 16, 2024, 22, model4, 930, 209],
      5: [12, 21, 2024, 24, model1, 900, 348],
      6: [12, 26, 2024,  2, model2, 910, 328]
    },
    "airport2": {
      "duration": 13,
      "flight1": [12,  2, 2024,  4, model3, 720, 251],
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
    1: ["Economy Class", "ECLASS", 1],
    2: ["Business Class", "BCLASS", 1.5],
    3: ["First Class", "FCLASS", 2.5]
  }
}

def getOrigin():
  global airportList, origin
  airportList = ["airport1", "airport2", "airport3", "airport4", "airport5", "airport6"]
  # Prompt message
  print("\n✈️   Hello and Welcome to Python Ticketing Airlines! 🌍" +
        "\n\nHere we serve our travelers with the outmost..." +
        "\n⚡ Efficiency, 🛡️  Safety and 🔐 Security!" +
        "\n\n" + "=" * 100 +
        "\n\n📍 Choose an ORIGIN airport:")
  for n in range(len(airportList)):
    print(f"   {n + 1}. {sysDict[airportList[n]]["name"]}")
  while True:
    try:
      userInput = input(f"\n>> 📋 Enter choice (1-{len(airportList)}): ")
      if 1 <= int(userInput) <= len(airportList):
        origin = airportList[int(userInput) - 1]
        airportList.remove(origin)
        print(f">> 🛫 Origin Airport: {sysDict[origin]["name"]}")
        break
      print(f">> ❌ Invalid input: '{userInput}'")
    except Exception as e:
      print(f">> ❌ Error: {e}")

def getDestination():
  global destination
  print("\n" + "=" * 100 +
        "\n\n📍 Choose an ORIGIN airport:")
  for n in range(len(airportList)):
    print(f"   {n + 1}. {sysDict[airportList[n]]["name"]}")
  print("\n   Type 'X' to restart the selection.")
  while True:
    try:
      userInput = input(f"\n>> 📋 Enter choice (1-{len(airportList)}): ")
      if userInput.lower() == 'x':
        print(">> 🔄 Restarting selection...")
        return True
      elif 1 <= int(userInput) <= len(airportList):
        destination = airportList[int(userInput) - 1]
        print(f">> 🛬 Destination Airport: {sysDict[destination]["name"]}")
        return False
      print(f">> ❌ Invalid input: '{userInput}'")
    except Exception as e:
      print(f">> ❌ Error: {e}")     

def time(x):
  if x == 24.0:
    return "12:00 AM"
  elif x == 12:
    return "12:00 PM"
  hr = int(x // 1)
  mn = int((x - hr) * 60)
  if x < 12:
    return f"{hr:02d}:{mn:02d} AM"
  else:
    return f"{hr:02d}:{mn:02d} PM"

def seats(x, y):
  if x == y:
    return "❌ FULL"
  return f"{x}/{y}"

def getFlightSchedule():
  global route, flightSched
  print("\n" + "=" * 100 +
        f"\n\n               {"Airport":<44}   Location" +
        f"\nOrigin:        {sysDict[origin]["name"]:<44}   {sysDict[origin]["location"]}" +
        f"\nDestination:   {sysDict[destination]["name"]:<44}   {sysDict[destination]["location"]}" +
        f"\n\n📍 Choose a FLIGHT SCHEDULE:")
  route = sysDict[origin][destination]
  for n in range(6):
    n += 1
    sched = route[n]
    print(f"   {n}. {sched[0]:02d}/{sched[1]:02d}/{sched[2]} | {time(sched[3])} | {sched[4][1]:<21} | ${sched[5]:.2f} | {seats(sched[6], sched[4][0])}")
  print("\n   Type 'X' to restart the selection.")
  while True:
    try:
      userInput = input(f"\n>> 📋 Enter choice (1-{len(airportList)}): ")
      if userInput.lower() == 'x':
        print(">> 🔄 Restarting selection...")
        return True
      elif 1 <= int(userInput) <= len(airportList):
        flightSched = route[int(userInput)]
        print(f">> 🛬 Flight Schedule: {flightSched[0]:02d}/{flightSched[1]:02d}/{flightSched[2]} - {time(flightSched[3])}")
        return False
      print(f">> ❌ Invalid input: '{userInput}'")
    except Exception as e:
      print(f">> ❌ Error: {e}")

def getTicketAmount():
  global ticketAmount
  print("\n🛫 Flight Schedule:" +
        f"\n   > Date:      {flightSched[0]:02d}/{flightSched[1]:02d}/{flightSched[2]}" +
        f"\n   > Take-off:  {time(flightSched[3])}" +
        f"\n   > Duration:  {route["duration"]} Hours" +
        f"\n   > Aircraft:  {flightSched[4][1]}" +
        f"\n   > Price:     ${flightSched[5]:.2f}" +
        f"\n   > Seats:     {seats(flightSched[6], flightSched[4][0])}" +
        "\n\n   Type 'X' to restart the selection.")
  while True:
    try:
      seatsLeft = flightSched[4][0] - flightSched[6]
      userInput = input(f"\n>> 🛒 How many tickets would you like to buy? ({seatsLeft} left): ")
      if userInput.lower() == 'x':
        print(">> 🔄 Restarting selection...")
        return True
      elif 1 <= int(userInput) <= seatsLeft:
        ticketAmount = int(userInput)
        print(f">> 🎫 Ticket amount: {ticketAmount} Ticket/s")
        return False
      print(f">> ❌ Invalid input: '{userInput}'")
    except Exception as e:
      print(f">> ❌ Error: {e}")

def getTicketClass():
  global ticketClass, totalCost
  print(f"\n📍 Choose a TICKET CLASS:")
  for n in range(3):
    n += 1
    print(f"   {n}. {sysDict['class'][n][0]:<20} Total: ${flightSched[5] * ticketAmount * sysDict['class'][n][2]:.2f}")
  print("\n   Type 'X' to restart the selection.")
  while True:
    try:
      userInput = input(f"\n>> 📋 Enter choice (1-{len(sysDict['class'])}): ")
      if userInput.lower() == 'x':
        print(">> 🔄 Restarting selection...")
        return True
      elif 1 <= int(userInput) <= len(sysDict['class']):
        ticketClass = sysDict['class'][int(userInput)]
        totalCost = flightSched[5] * ticketAmount * ticketClass[2]
        print(f">> 🎫 Ticket Class: {ticketClass[0]}" +
              f"\n>> 💵 Total Cost:   ${totalCost:.2f}")
        return False
      print(f">> ❌ Invalid input: '{userInput}'")
    except Exception as e:
      print(f">> ❌ Error: {e}")

restart_message = "\n" + "=" * 100 + f"\n{"Restarting System...":^100}" + "\n" + "=" * 100

while True:
  getOrigin()
  if getDestination():
    print(restart_message)
    continue
  if getFlightSchedule():
    print(restart_message)
    continue
  if getTicketAmount():
    print(restart_message)
    continue
  if getTicketClass():
    print(restart_message)
    continue
