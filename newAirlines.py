aircrafts = {
  1: [200, "Boeing 777", 1],
  2: [175, "Airbus A350 XWB", 2],
  3: [150, "Boeing 787 Dreamliner", 3],
  4: [125, "Airbus A320 Family", 4]
}

airports = {
  1: {
    "name": "UAE - Dubai International Airport",
    "location": "Dubai, United Arab Emirates",
    # Routes Available
    2: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    3: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    4: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    5: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    6: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    }
  },
  2: {
    "name": "CHN - Guangzhou Baiyun International Airport",
    "location": "Guangdong Province, China",
    # Routes Available
    1: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    3: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    4: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    5: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    6: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    }
  },
  3: {
    "name": "GBR - London Heathrow Airport",
    "location": "London, United Kingdom",
    # Routes Available
    1: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    2: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    4: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    5: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    6: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    }
  },
  4: {
    "name": "USA - Los Angeles International Airport",
    "location": "California, USA",
    # Routes Available
    1: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    3: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    3: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    5: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    6: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    }
  },
  5: {
    "name": "PHL - Ninoy Aquino International Airport",
    "location": "Manila, Philippines",
    # Routes Available
    1: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    3: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    3: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    4: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    6: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    }
  },
  6: {
    "name": "JPN - Tokyo Haneda Airport",
    "location": "Tokyo, Japan",
    # Routes Available
    1: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    3: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    3: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    4: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    },
    5: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 500, 100, aircrafts[1]]
    }
  }
}

ticketClasses = {
  1: [1, "Economy Class"],
  2: [1.2, "Business Class"],
  3: [1.5, "First Class"]
}

def getRoute():
  global origin, destination
  print("\nHello and Welcome to Python Airlines!")
  print("\nAirports List:")
  for n in range(len(airports)):
    n += 1
    print(f"{n}. {airports[n]["name"]}")
  print("Enter 'X' to restart the system.")
  while True:
    org = input("\nChoose an Origin: ")
    if org.isdigit() and 1 <= int(org) <= len(airports):
      origin = int(org)
      print(f"Chosen {airports[origin]["name"]} as the origin airport.")
      break
    elif org == "x":
      print("Restarting...\n\n\n\n\n")
      return True
    else:
      print("Invalid input! Please try again.")
  while True:
    dtn = input("\nChoose an Destination: ")
    if dtn == org:
      print("Invalid input! Cannot choose origin as destination.")
    elif dtn.isdigit() and 1 <= int(dtn) <= len(airports):
      destination = int(dtn)
      print(f"Chosen {airports[destination]["name"]} as the origin airport.")
      break
    elif dtn == "x":
      print("Restarting...\n\n\n\n\n")
      return True
    else:
      print("Invalid input! Please try again.")

def calcSeats(x, y):
  if x == y:
    return f"❌ FULL"
  return f"{x:03d}/{y:03d}"

def getFlight():
  global flight, flightNum
  print("\nFlight Schedule:")
  print(f"+{"-"*11}+{"-"*10}+{"-"*10}+{"-"*10}+{"-"*9}+{"-"*23}+")
  print(f"| {"Flt #":^9} | {"Date":^8} | Take-off | {"Cost":^8} | {"Seats":^7} | {"Aircraft":^21} |")
  print(f"+{"-"*11}+{"-"*10}+{"-"*10}+{"-"*10}+{"-"*9}+{"-"*23}+")
  for n in range(len(airports[origin][destination])):
    n += 1
    x = airports[origin][destination][n]
    y = f"{x[2]:.2f}"
    print(f"| Flight #{n} | {x[0]} | {x[1]} | ${y:^7} | {calcSeats(x[3], x[4][0]):^7} | {x[4][1]:^21} |")
  print(f"+{"-"*11}+{"-"*10}+{"-"*10}+{"-"*10}+{"-"*9}+{"-"*23}+")
  print("Enter 'X' to restart the system.")
  while True:
    flt = input("\nChoose a Flight Schedule: ")
    if flt.isdigit() and 1 <= int(flt) <= len(airports[origin][destination][n]):
      flightNum = int(flt)
      flight = airports[origin][destination][int(flt)]
      print(f"Chosen flight schedule #{int(flt)}.")
      break
    elif flt == "x":
      print("Restarting...\n\n\n\n\n")
      return True
    else:
      print("Invalid input! Please try again.")

def getTicket():
  global ticketAmount, ticketClass, totalCost
  seatsLeft = flight[4][0] - flight[3]
  while True:
    tktAmt = input(f"\nEnter Ticket Amount ({seatsLeft} left): ")
    if tktAmt.isdigit() and 1 <= int(tktAmt) <= seatsLeft:
      ticketAmount = int(tktAmt)
      break
    elif tktAmt == "x":
      print("Restarting...\n\n\n\n\n")
      return True
    else:
      print("Invalid amount! Please try again.")
  print("\nChoose ticket class:")
  print(f"+---+{"-"*27}+{"-"*18}+{"-"*27}+")
  print(f"| # | {"Aircraft":^25} | {"Multiplier":^16} | {"Total Cost":^25} |")
  print(f"+---+{"-"*27}+{"-"*18}+{"-"*27}+")
  for n in range(len(ticketClasses)):
    n += 1
    total = f"${ticketAmount * ticketClasses[n][0] * flight[2]:.2f}"
    print(f"| {n} | {ticketClasses[n][1]:^25} | {str(ticketClasses[n][0]) + " x":^16} | {total:^25} |")
  print(f"+---+{"-"*27}+{"-"*18}+{"-"*27}+")
  print("Enter 'X' to restart the system.")
  while True:
    tktCls = input("\nChoose a Ticket Class: ")
    if tktCls.isdigit() and 1 <= int(tktCls) <= len(ticketClasses):
      ticketClass = ticketClasses[int(tktCls)]
      totalCost = ticketAmount * ticketClass[0] * flight[2]
      print(f"Chosen {ticketClass[1]} as ticket class.")
      print(f"Total cost of the tickets is ${totalCost:.2f}")
      break
    elif tktCls == "x":
      print("Restarting...\n\n\n\n\n")
      return True
    else:
      print("Invalid input! Please try again.")
      
def getPayment():
  while True:
    payment = input("\nEnter payment amount: $")
    if payment.replace(".", "", 1).isdigit() and float(payment) >= totalCost:
      print(f"Payment accepted! Change is ${float(payment) - totalCost:.2f}")
      flight[3] += ticketAmount
      break
    elif payment == "x":
      print("Restarting...\n\n\n\n\n")
      return True
    else:
      print("Invalid input! Please try again.")

def printTicketIDs():
  print("\nPrinting ticket IDs...\n")
  for n in range(ticketAmount):
    seatNum = flight[3] + n + 1
    date = f"M{flight[0][0:2]}D{flight[0][3:5]}Y{flight[0][6:8]}"
    ticketID = f"PAL-OR{origin:02d}-DT{destination:02d}-{date}-FLT{flightNum:03d}-MDL{flight[4][2]:02d}-P{seatNum:03d}"
    print(f"{ticketID:^80}")
  print("\nAdditional Information:")
  print("Seat number can be found for the last four digits of the ticket ID.")

def restartSystem():
  while True:
    restart = input("\nWould you like to order again? (Yes/No): ")
    if restart.lower() == "yes":
      print("Running the system again...\n\n\n\n\n")
      return True
    elif restart.lower() == "no":
      print("Closing the system...")
      print("Thank you for using Python Airlines!\n")
      return False
    else:
      print("Invalid input! Please try again.")

while True:
  if getRoute(): continue
  if getFlight(): continue
  if getTicket(): continue
  if getPayment(): continue
  printTicketIDs()
  if restartSystem(): continue
  else: break