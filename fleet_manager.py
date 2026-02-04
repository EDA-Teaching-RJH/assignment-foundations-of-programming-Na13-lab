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
        