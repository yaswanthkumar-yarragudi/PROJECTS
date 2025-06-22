def cur_x():
    exchange = {
        "usd": 1.0,
        "inr": 83.30,
        "eur": 0.93,
        "gbp": 0.8,
        "aud": 1.5,
        "jpy": 151.5,
        "cad": 1.36,
        "cny": 7.23
    }
    
    print("="*30+"\n")
    print("Available currencies:", ", ".join(exchange.keys()).upper())
    
    while True:
        print("\n" + "="*30)
        try:
            x = input("Enter currency to convert FROM (or 'exit' to quit): ").lower().strip()
            if x == 'exit':
                print("Goodbye!")
                break
                
            if x not in exchange:
                print(f"Error: '{x.upper()}' is not a supported currency")
                continue
                
            y = input("Enter currency to convert TO: ").lower().strip()
            if y not in exchange:
                print(f"Error: '{y.upper()}' is not a supported currency")
                continue
                
            amount = float(input("Enter amount: "))
            if(amount<0):
                print("Negative Amount Entered !! Try Again ...")
                continue
            
            usd_value = amount / exchange[x]
            total = usd_value * exchange[y]
            
            print(f"\n{amount:.2f} {x.upper()} = {total:.3f} {y.upper()}")
            
            again = input("\nConvert again? (y/n): ").lower()
            if again != 'y':
                print("\nThank you for using the currency converter!\n")
                break
                
        except ValueError:
            print("Error: Please enter a valid number for the amount")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero") 

if __name__ == "__main__":
    cur_x()





