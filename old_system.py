n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0
    while loading < 5:
        print("Loading module " + str(loading))
        loading += 1 #Fix: Prevents infinite loop
        
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        
        if opt == "1":  #Fix: Use len(n) instead of hardcoded 10 to avoid IndexError
            print("Current Crew List:")
            
            for i in range(len(n)):
                print(n[i] + " - " + r[i]) 
                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
            n.append(new_name)
            n.append(new_rank)
            n.append(new_div) 
            print("Crew member added.") #Fix: Keeps lists synced
            
        elif opt == "3":
            rem = input("Name to remove: ")
            if rem in n
                idx = n.index(rem)
                n.pop(idx)
                r.pop(idx)
                d.pop(idx)
                print("Removed.")
            else:
                print("Name not found") 
            #Fix: Prevents ValueError; By adding (if rem in n), the program would not crash and write ("Name not found")
            
        elif opt == "4":
            print("Analyzing...")
            count = 0
            
            for rank in r:
                if rank == "Captain" or rank == "Commander": 
                #Fix: Correct logical comparison ("commander") was recognised as a non empty spring
                    count = count + 1
            print("High ranking officers:" + str(count)) 
            #Fix: Place str() function. Since count in an integer and the message is a string, it gives TypeError as it cannot "add" a number to a tex
            
        elif opt == "5":
            print("Shutting down.")
            break
        else:
            print("Invalid.")
            
        
        x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        else:     #Fix: Replace the if/if into if/else. Prevents it from evaluating the length of the list twice to evaluating it just once.
            print("Database empty.")

        
        fuel = 100
        consumption = 0
        while fuel > 0:
            
            print("Idling...")
            break 
            
        print("End of cycle.")

run_system_monolith
