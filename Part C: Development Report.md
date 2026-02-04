## Part C: The Development Report (25 Marks)

**Length:** 1 Page.

1.  **Legacy Code Post-Mortem:** A breakdown of the 10 bugs found in Part A. You must explain _why_ the bug occurred (e.g., "The code `if x = 1` causes a Syntax Error because `=` is assignment, whereas `==` is comparison" ). **(20 Marks)  2 per bug**
    
2.  **Parallel List Strategy:** Explain the dangers of using parallel lists. What happens if you remove a name from the `names` list but forget to remove the ID from the `ids` list? How did your code prevent this, or how could it be prevented? **(5 Marks)**
Incomplete = **0 Marks**
Partial Implementation = **3 Marks** 
Full Implementation = **5 Marks**

## Legacy Code Post-Mortem:

#1st Bug: The first bug found in Part A was an infinite loading loop. The while loading < 5: loop was missing and increment statement which meant that the condition remained true forever, therefore being stuck in an infinite loop. By adding loading += 1, this ensured that the variable reaches 5, allowing the program to proceed to the main menu.

#2nd Bug: The hardcoded i for in range(10) was trying to look for a 5th item that didn't exist as the lists, n, r and d only contained for 4 items. This was therefore giving IndexError. By replacing it with the loop i in range(len(n)), this allows the loop to only run for the actual number of items in te list.

#3rd Bug: The "Add Crew" logic only updated the name list n, leaving the rank r and division d lists shorter than the name list.This meant that the person that was added had no rank or division. This was breaking the parallel logic. By adding r.append(new_rank) and d.append(new_division), every name has now a corresponding rank and division.

#4th Bug: Remove Crew ValueError Crash was due to the orignial code trying to find a name using n.index(rem) without checking if the name existed. By adding the logic if rem in n, it would check now if the name exists and if it doesns't it would type "Name not found" instead of crashing. 

#5th Bug: Logical "or" trap in analysis; The original code was rank == "Captain" or "Commander", this meant that "Commander" was a non empty spring, making the whole condition true to every single person. By also adding rank == "Commander", this forces Python to check the rank against both strings.

#6th Bug: String/Integer Type Error; The original code was trying to combine a string with an integer using + ("High ranking officers:" + count). This cannot happen without a conversion. By using the str() function, this allowed the number to be converted into text.

#7th Bug: Reduntant Check; The original code used 2 separate if statements which meant that it was checking the length of the list twice. This means that even if the first condition was met, it would still check the second condition. By replacing it with a if/else statement, if the 1st condtion is met, the 2nd is automatically skipped. 

#8th Bug: A while fuel > 0: loop was used but a break was used immediately inside it which made the logic irrelevant. In the fixed version it ensures the loop has an exit strategy that doesn't hang the terminal.

#9th Bug: The logic (System Check, Fuel,etc) was written after the main while True loop which only allowed the code to run after the user exits the system. By organising the logic so that the boot up checks happen at the start and shutdown checks happen correctly at the end.

#10th Bug: Missing Function Call; At the end the script just said run_system_monolith without the () which meant that the function was not triggered and it was just a function name. By adding the () like run_system_monolith(), the function was triggered so the program actually started.