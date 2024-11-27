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
      "flight1": [12,  1, 2024,  4, model1, 400, 359],
      "flight2": [12,  6, 2024,  6, model2, 410, 336],
      "flight3": [12, 11, 2024,  8, model3, 420, 252],
      "flight4": [12, 16, 2024, 10, model4, 430, 228],
      "flight5": [12, 21, 2024, 12, model1, 400, 385],
      "flight6": [12, 26, 2024, 14, model2, 410, 318]
    },
    "airport3": {
      "duration": 8,
      "flight1": [12,  2, 2024, 16, model3, 520, 295],
      "flight2": [12,  7, 2024, 18, model4, 530, 206],
      "flight3": [12, 12, 2024, 20, model1, 500, 356],
      "flight4": [12, 17, 2024, 22, model2, 510, 311],
      "flight5": [12, 22, 2024, 24, model3, 520, 268],
      "flight6": [12, 27, 2024,  2, model4, 530, 219]
    },
    "airport4": {
      "duration": 15,
      "flight1": [12,  2, 2024, 16, model3, 520, 295],
      "flight2": [12,  7, 2024, 18, model4, 530, 206],
      "flight3": [12, 12, 2024, 20, model1, 500, 356],
      "flight4": [12, 17, 2024, 22, model2, 510, 311],
      "flight5": [12, 22, 2024, 24, model3, 520, 268],
      "flight6": [12, 27, 2024,  2, model4, 530, 219]
    },
    "airport5": {
      "duration": 8.5,
      "flight1": [12,  4, 2024, 16, model3, 420, 278],
      "flight2": [12,  9, 2024, 18, model4, 430, 209],
      "flight3": [12, 14, 2024, 20, model1, 400, 361],
      "flight4": [12, 19, 2024, 22, model2, 410, 326],
      "flight5": [12, 24, 2024, 24, model3, 420, 247],
      "flight6": [12, 29, 2024,  2, model4, 430, 242]
    },
    "airport6": {
      "duration": 9.5,
      "flight1": [12,  5, 2024,  4, model1, 600, 371],
      "flight2": [12, 10, 2024,  6, model2, 610, 300],
      "flight3": [12, 15, 2024,  8, model3, 620, 291],
      "flight4": [12, 20, 2024, 10, model4, 630, 230],
      "flight5": [12, 25, 2024, 12, model1, 600, 348],
      "flight6": [12, 30, 2024, 14, model2, 610, 348]
    },
  },
  "airport2": {
    "name":       "CHN - Guangzhou Baiyun International Airport",
    "location":   "Guangdong Province, China",
    # Destination airports - excluded the origin airport
    "airport1": {
      "duration": 8,
      "flight1": [12,  1, 2024,  8, model1, 400, 372],
      "flight2": [12,  6, 2024, 10, model2, 410, 317],
      "flight3": [12, 11, 2024, 12, model3, 420, 252],
      "flight4": [12, 16, 2024, 14, model4, 430, 234],
      "flight5": [12, 21, 2024, 16, model1, 400, 362],
      "flight6": [12, 26, 2024, 18, model2, 410, 305]
    },
    "airport3": {
      "duration": 12,
      "flight1": [12,  2, 2024, 20, model3,   12, 720, 287],
      "flight2": [12,  7, 2024, 22, model4,   12, 730, 203],
      "flight3": [12, 12, 2024, 24, model1,   12, 700, 368],
      "flight4": [12, 17, 2024,  2, model2,   12, 710, 305],
      "flight5": [12, 22, 2024,  4, model3,   12, 720, 255],
      "flight6": [12, 27, 2024,  6, model4,   12, 730, 225]
    },
    "airport4": {
      "duration": 13,
      "flight1": [12,  3, 2024,  8, model1, 700, 395],
      "flight2": [12,  8, 2024, 10, model2, 710, 322],
      "flight3": [12, 13, 2024, 12, model3, 720, 296],
      "flight4": [12, 18, 2024, 14, model4, 730, 214],
      "flight5": [12, 23, 2024, 16, model1, 700, 393],
      "flight6": [12, 28, 2024, 18, model2, 710, 337]
    },
    "airport5": {
      "duration": 2.5,
      "flight1": [12,  4, 2024, 20, model3,  2.5, 170, 267],
      "flight2": [12,  9, 2024, 22, model4,  2.5, 180, 207],
      "flight3": [12, 14, 2024, 24, model1,  2.5, 150, 349],
      "flight4": [12, 19, 2024,  2, model2,  2.5, 160, 328],
      "flight5": [12, 24, 2024,  4, model3,  2.5, 170, 253],
      "flight6": []
    },
    "airport6": {
      "duration": 4.5,
      "flight1": [12,  5, 2024,  8, model1, 300, 362],
      "flight2": [12, 10, 2024, 10, model2, 310, 343],
      "flight3": [12, 15, 2024, 12, model3, 320, 270],
      "flight4": [12, 20, 2024, 14, model4, 330, 222],
      "flight5": [12, 25, 2024, 16, model1, 300, 366],
      "flight6": []
    },
  },
  "airport3": {
    "name":       "GBR - London Heathrow Airport",
    "location":   "London, United Kingdom",
    # Destination airports - excluded the origin airport
    "airport1": {
      "duration": 7,
      "flight1": [12,  1, 2024, 12, model1, 500, 396],
      "flight2": [12,  6, 2024, 14, model2, 510, 323],
      "flight3": [12, 11, 2024, 16, model3, 520, 273],
      "flight4": [12, 16, 2024, 18, model4, 530, 240],
      "flight5": [12, 21, 2024, 20, model1, 500, 357],
      "flight6": [12, 26, 2024, 22, model2, 510, 340]
    },
    "airport2": {
      "duration": 11.5,
      "flight1": [12,  2, 2024, 24, model3, 720, 246],
      "flight2": [12,  7, 2024,  2, model4, 730, 200],
      "flight3": [12, 12, 2024,  4, model1, 700, 352],
      "flight4": [12, 17, 2024,  6, model2, 710, 301],
      "flight5": [12, 22, 2024,  8, model3, 720, 260],
      "flight6": [12, 27, 2024, 10, model4, 730, 204]
    },
    "airport4": {
      "duration": 11,
      "flight1": [12,  3, 2024, 12, model1, 700, 385],
      "flight2": [12,  8, 2024, 14, model2, 710, 339],
      "flight3": [12, 13, 2024, 16, model3, 720, 254],
      "flight4": [12, 18, 2024, 18, model4, 730, 233],
      "flight5": [12, 23, 2024, 20, model1, 700, 351],
      "flight6": [12, 28, 2024, 22, model2, 710, 301]
    },
    "airport5": {
      "duration": 14,
      "flight1": [12,  4, 2024, 24, model3, 820, 290],
      "flight2": [12,  9, 2024,  2, model4, 830, 208],
      "flight3": [12, 14, 2024,  4, model1, 800, 349],
      "flight4": [12, 19, 2024,  6, model2, 810, 333],
      "flight5": [12, 24, 2024,  8, model3, 820, 258],
      "flight6": [12, 29, 2024, 10, model4, 830, 224]
    },
    "airport6": {
      "duration": 11,
      "flight1": [12,  5, 2024, 12, model1, 800, 375],
      "flight2": [12, 10, 2024, 14, model2, 810, 300],
      "flight3": [12, 15, 2024, 16, model3, 820, 283],
      "flight4": [12, 20, 2024, 18, model4, 830, 220],
      "flight5": [12, 25, 2024, 20, model1, 800, 392],
      "flight6": [12, 30, 2024, 22, model2, 810, 312]
    },
  },
  "airport4": {
    "name":       "USA - Los Angeles International Airport",
    "location":   "California, USA",
    # Destination airports - excluded the origin airport
    "airport1": {
      "duration": 15,
      "flight1": [12,  1, 2024, 16, model1, 900, 380],
      "flight2": [12,  6, 2024, 18, model2, 910, 310],
      "flight3": [12, 11, 2024, 20, model3, 920, 270],
      "flight4": [12, 16, 2024, 22, model4, 930, 209],
      "flight5": [12, 21, 2024, 24, model1, 900, 348],
      "flight6": [12, 26, 2024,  2, model2, 910, 328]
    },
    "airport2": {
      "duration": 13,
      "flight1": [12,  2, 2024,  4, model3, 720, 251],
      "flight2": [12,  7, 2024,  6, model4, 730, 204],
      "flight3": [12, 12, 2024,  8, model1, 700, 358],
      "flight4": [12, 17, 2024, 10, model2, 710, 318],
      "flight5": [12, 22, 2024, 12, model3, 720, 278],
      "flight6": [12, 27, 2024, 14, model4, 730, 205]
    },
    "airport3": {
      "duration": 10.5,
      "flight1": [12,  3, 2024, 16, model1, 600, 369],
      "flight2": [12,  8, 2024, 18, model2, 610, 335],
      "flight3": [12, 13, 2024, 20, model3, 620, 255],
      "flight4": [12, 18, 2024, 22, model4, 630, 241],
      "flight5": [12, 23, 2024, 24, model1, 600, 360],
      "flight6": [12, 28, 2024,  2, model2, 610, 333]
    },
    "airport5": {
      "duration": 15,
      "flight1": [12,  4, 2024,  4, model3, 620, 271],
      "flight2": [12,  9, 2024,  6, model4, 630, 217],
      "flight3": [12, 14, 2024,  8, model1, 600, 357],
      "flight4": [12, 19, 2024, 10, model2, 610, 312],
      "flight5": [12, 24, 2024, 12, model3, 620, 263],
      "flight6": [12, 29, 2024, 14, model4, 630, 231]
    },
    "airport6": {
      "duration": 11,
      "flight1": [12,  5, 2024, 16, model1, 800, 357],
      "flight2": [12, 10, 2024, 18, model2, 810, 346],
      "flight3": [12, 15, 2024, 20, model3, 820, 265],
      "flight4": [12, 20, 2024, 22, model4, 830, 206],
      "flight5": [12, 25, 2024, 24, model1, 800, 373],
      "flight6": [12, 30, 2024,  2, model2, 810, 349]
    },
  },
  "airport5": {
    "name":       "PHL - Ninoy Aquino International Airport",
    "location":   "Manila, Philippines",
    # Destination airports - excluded the origin airport
    "airport1": {
      "duration": 8.5,
      "flight1": [12,  1, 2024, 20, model1, 400, 357],
      "flight2": [12,  6, 2024, 22, model2, 410, 315],
      "flight3": [12, 11, 2024, 24, model3, 420, 286],
      "flight4": [12, 16, 2024,  2, model4, 430, 219],
      "flight5": [12, 21, 2024,  4, model1, 400, 368],
      "flight6": [12, 26, 2024,  6, model2, 410, 317]
    },
    "airport2": {
      "duration": 2.5,
      "flight1": [12,  2, 2024,  8, model3, 170, 277],
      "flight2": [12,  7, 2024, 10, model4, 180, 236],
      "flight3": [12, 12, 2024, 12, model1, 150, 370],
      "flight4": [12, 17, 2024, 14, model2, 160, 309],
      "flight5": [12, 22, 2024, 16, model3, 170, 289],
      "flight6": [12, 27, 2024, 18, model4, 180, 233]
    },
    "airport3": {
      "duration": 14,
      "flight1": [12,  3, 2024, 20, model1, 800, 377],
      "flight2": [12,  8, 2024, 22, model2, 810, 304],
      "flight3": [12, 13, 2024, 24, model3, 820, 262],
      "flight4": [12, 18, 2024,  2, model4, 830, 195],
      "flight5": [12, 23, 2024,  4, model1, 800, 369],
      "flight6": [12, 28, 2024,  6, model2, 810, 324]
    },
    "airport4": {
      "duration": 12,
      "flight1": [12,  4, 2024,  8, model3, 820, 274],
      "flight2": [12,  9, 2024, 10, model4, 830, 243],
      "flight3": [12, 14, 2024, 12, model1, 800, 349],
      "flight4": [12, 19, 2024, 14, model2, 810, 323],
      "flight5": [12, 24, 2024, 16, model3, 820, 276],
      "flight6": [12, 29, 2024, 18, model4, 830, 199]
    },
    "airport6": {
      "duration": 4.5,
      "flight1": [12,  5, 2024, 20, model1, 300, 391],
      "flight2": [12, 10, 2024, 22, model2, 310, 344],
      "flight3": [12, 15, 2024, 24, model3, 320, 283],
      "flight4": [12, 20, 2024,  2, model4, 330, 242],
      "flight5": [12, 25, 2024,  4, model1, 300, 394],
      "flight6": [12, 30, 2024,  6, model2, 310, 332]
    },
  },
  "airport6": {
    "name":       "JPN - Tokyo Haneda Airport",
    "location":   "Tokyo, Japan",
    # Destination airports - excluded the origin airport
    "airport1": {
      "duration": 10,
      "flight1": [12,  1, 2024, 24, model1, 600, 365],
      "flight2": [12,  6, 2024,  2, model2, 610, 303],
      "flight3": [12, 11, 2024,  4, model3, 620, 253],
      "flight4": [12, 16, 2024,  6, model4, 630, 196],
      "flight5": [12, 21, 2024,  8, model1, 600, 361],
      "flight6": [12, 26, 2024, 10, model2, 610, 349]
    },
    "airport2": {
      "duration": 4.5,
      "flight1": [12,  2, 2024, 12, model3, 320, 255],
      "flight2": [12,  7, 2024, 14, model4, 330, 241],
      "flight3": [12, 12, 2024, 16, model1, 300, 396],
      "flight4": [12, 17, 2024, 18, model2, 310, 312],
      "flight5": [12, 22, 2024, 20, model3, 320, 267],
      "flight6": [12, 27, 2024, 22, model4, 330, 223]
    },
    "airport3": {
      "duration": 12,
      "flight1": [12,  3, 2024, 24, model1, 800, 351],
      "flight2": [12,  8, 2024,  2, model2, 810, 321],
      "flight3": [12, 13, 2024,  4, model3, 820, 247],
      "flight4": [12, 18, 2024,  6, model4, 830, 242],
      "flight5": [12, 23, 2024,  8, model1, 800, 367],
      "flight6": [12, 28, 2024, 10, model2, 810, 345]
    },
    "airport4": {
      "duration": 10.5,
      "flight1": [12,  4, 2024, 12, model3, 720, 283],
      "flight2": [12,  9, 2024, 14, model4, 730, 234],
      "flight3": [12, 14, 2024, 16, model1, 700, 352],
      "flight4": [12, 19, 2024, 18, model2, 710, 333],
      "flight5": [12, 24, 2024, 20, model3, 720, 283],
      "flight6": [12, 29, 2024, 22, model4, 730, 212]
    },
    "airport5": {
      "duration": 0,
      "flight1": [12,  5, 2024, 24, model1, 300, 380],
      "flight2": [12, 10, 2024,  2, model2, 310, 346],
      "flight3": [12, 15, 2024,  4, model3, 320, 246],
      "flight4": [12, 20, 2024,  6, model4, 330, 241],
      "flight5": [12, 25, 2024,  8, model1, 300, 364],
      "flight6": [12, 30, 2024, 10, model2, 310, 349]
    }
  }
}


print(f"{sysDict["airport1"]["name"]}")