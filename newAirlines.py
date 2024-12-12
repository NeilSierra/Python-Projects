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

def getFlight():
  print("\nFlight Schedule:")
  for n in range(len(airports[origin][destination])):
    n += 1
    print(f"{n} {airports[origin][destination][n]}")

while True:
  if getRoute(): continue