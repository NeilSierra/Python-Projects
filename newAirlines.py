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
      1: ["12/01/24", "04:00 AM", 400, 100, aircrafts[1]],
      2: ["12/08/24", "08:00 AM", 400, 100, aircrafts[2]],
      3: ["12/15/24", "12:00 PM", 400, 100, aircrafts[3]]
    },
    3: {},
    4: {},
    5: {},
    6: {}
  },
  2: {
    "name": "CHN - Guangzhou Baiyun International Airport",
    "location": "Guangdong Province, China",
    # Routes Available
    1: {},
    3: {},
    4: {},
    5: {},
    6: {}
  },
  3: {
    "name": "GBR - London Heathrow Airport",
    "location": "London, United Kingdom",
    # Routes Available
    1: {},
    2: {},
    4: {},
    5: {},
    6: {}
  },
  4: {
    "name": "USA - Los Angeles International Airport",
    "location": "California, USA",
    # Routes Available
    1: {},
    2: {},
    3: {},
    5: {},
    6: {}
  },
  5: {
    "name": "PHL - Ninoy Aquino International Airport",
    "location": "Manila, Philippines",
    # Routes Available
    1: {},
    2: {},
    3: {},
    4: {},
    6: {}
  },
  6: {
    "name": "JPN - Tokyo Haneda Airport",
    "location": "Tokyo, Japan",
    # Routes Available
    1: {},
    2: {},
    3: {},
    4: {},
    5: {}
  }
}
