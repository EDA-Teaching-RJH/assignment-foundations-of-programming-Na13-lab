def init_database():
    names= ["William Regal", "Edward Teach", "Jack Sparrow", "Deanna Troi", "Zakaria Sheikh"]
    ranks = ["Lieutenant", "Commander", "Captain", "Counselor", "Lieutenant"]
    divisions = ["Security", "Command", "Command", "Counseling", "Operations"]
    ids = [ "03", "02", "01", "05", "04"]
    return names, ranks, divisions, ids 

def display_menu(current_user):
    print("\n--- WELCOME TO THE MENU ---")
    print(f"Logged in as: {current_user}")
    print("1. View Crew Members\n2. Add Crew Members\n3. Remove Crew Members")
    print("4. Update Rank\n5. Search Crew\n6. Filter by Division")
    print("7. Calculate Payroll\n8. Count officers\n9. Exit")
    choice = input("Select option:")
    return choice

def view_crew_members(names, rank, divisions, ids):
    print(f"\n{ 'ID':<10}{'Name':<20}{'Rank':<15}{'Division':<15}")
    print("-"*60)
    for i in range(len(names)):
        print(f"{ids[i]:<10}{names[i]:<20}{rank[i]:<15}{divisions[i]:<15}")

def add_crew_member(names, ranks, divisions, ids):
    new_id = input("Enter ID:")
    if new_id in ids:
        print("ID already exists. Please try again.")
        return names, ranks, divisions, ids
    new_rank = input("Enter Rank(Captain/Commander/Lieutenant/Counselor):")
    valid_ranks = ["Captain", "Commander", "Lieutenant", "Counselor"] 
    if new_rank not in valid_ranks:
        print("Invalid rank. Please try again.")
        return
    names.append(input("Please enter a Name:"))
    ranks.append(new_rank)
    new_division = input("Enter Division(Security/Command/Counseling/Operations):") 
    valid_divisions = ["Security", "Command", "Counseling", "Operations"]
    if new_division not in valid_divisions:
        print("Invalid Division. Please try again.")
        return
    ids.append(new_id) 
    print("Crew Member added successfully. Welcome aboard!")

def remove_crew_member(names, ranks, divisions, ids):
    target_id = input("Enter the ID of the crew member you wish to remove:")
    if target_id in ids:
        idx = ids.index(target_id)
        names.pop(idx)
        ranks.pop(idx)
        divisions.pop(idx)
        ids.pop(idx)
        print("Crew Member removed successfully.")
    else:
        print("ID not found. Please try again!")

def update_rank(names, ranks, divisions, ids):
    target_id = input("Enter the ID of the crew member whose you wish to promote/demote:")
    if target_id in ids:
        idx = ids.index(target_id)
        new_rank = input("Enter new Rank(Captain/Commander/Lieutenant/Counselor):")
        valid_ranks = ["Captain", "Commander", "Lieutenant", "Counselor"]
        if new_rank in valid_ranks:
            ranks[idx] = new_rank
            print("Rank updated successfully.")
        else:
            print("Invalid rank. Please try again.")
    else:
        print("ID not found. Please try again!")

def search_crew(names, ranks, divisions, ids):
    term = input("Search for name:").lower()
    for i in range(len(names)):
        if term in names[i].lower():
            print(f"Match found: {ids[i]} - {names[i]} - {ranks[i]}")
    def filter_by_division(names, divisions, ranks, ids):
        div_choice = input("Enter Division to filter by(Security/Command/Counseling/Operations):")
        for i in range(len(names)):
            if divisions[i] == div_choice:
                print(f"{ids[i]} - {names[i]} - {ranks[i]}")

def calculate_payroll(ranks):
    total = 0
    for r in ranks:
        if r == "Captain":
            total += 8000
        elif r == "Commander":
            total += 6000
        else:
            total += 4000
    print(f"Total Monthly Crew Payroll: £{total}")

def count_officers(ranks):
    count = ranks.count("Captain") + ranks.count("Commander")
    print(f"Total of High-Rank Officers: {count}")
    