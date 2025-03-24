print("Hello and welcome to the Loan System!" +
      "\n\nGuidlines for taking a Loan:" +
      "\n1. User's monthly salary should exceed ₱30000.00" +
      "\n2. Requested loan amount should not exceed 10 times the user salary" +
      "\n3. Loan interest is 10%")

def loanSystem():
    userSalary = float(input("\nEnter user monthly salary: ₱").strip().replace(",",""))
    if userSalary < 30000:
        print("| Invalid salary amount! Monthly salary should exceed ₱30000.00!")
        exit()
    
    loanLimit = userSalary * 10

    loanAmount = float(input(f"\nEnter loan amount (should not exceed ₱{loanLimit:.02f}): ₱").strip().replace(",",""))
    if loanAmount > loanLimit:
        print(f"| Invalid loan amount! Loan amount should not exceed ₱{loanLimit:.02f}!")
        exit()
    
    loanDuration = int(input("\nEnter loan duration (in months): ").strip())
    loanWithInterest = (loanAmount * 0.1) + loanAmount
    paymentPerMonth = loanWithInterest / loanDuration
    
    print("\nTransaction Details:" +
          f"\n| Loan Amount: ₱{loanAmount:.02f}" +
          "\n| Loan Interest: 10%" +
          f"\n| Loan with Interest: ₱{loanWithInterest:.02f}" +
          f"\n| Loan Duration: {loanDuration} months" +
          f"\n| Payment per Month: ₱{paymentPerMonth:.02f}")

loanSystem()