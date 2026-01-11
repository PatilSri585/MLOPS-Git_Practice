print("Hello, World!") #1st Commit
print("This is a demo Python script.") #2nd Commit
print("It demonstrates basic print functionality.") #3rd Commit

#Test1 branch is carved from 3rd commit
print("This line is added in Test1 branch.") #Test1 Commit
print("Another line in Test1 branch.") #Test1 Commit 2

<<<<<<< HEAD
print("conflict commit.") #Conflict commit on main
=======
print("Back to test branch.") #Conflict Commit on test
>>>>>>> test1
