prop = raw_input("Enter property Name: ")

issue = raw_input("Enter issue: ")

notes = open("ticket_notes.txt", "a+")

notes.write(prop +" - " + issue + "\n")

notes.close()
