aircrafts = {
  1: [200, "Boeing 777"],
  2: [175, "Airbus A350 XWB"],
  3: [150, "Boeing 787 Dreamliner"],
  4: [125, "Airbus A320 Family"]
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
      print("Restarting...")
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
      print("Restarting...")
      return True
    else:
      print("Invalid input! Please try again.")

def calcSeats(x, y):
  if x == y:
    return f"❌ FULL"
  return f"{x:03d}/{y:03d}"

def getFlight():
  global flight
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
      flight = int(flt)
      print(f"Chosen flight schedule #{flight}.")
      break
    elif flt == "x":
      print("Restarting...")
      return True
    else:
      print("Invalid input! Please try again.")

while True:
  if getRoute(): continue
  if getFlight(): continue