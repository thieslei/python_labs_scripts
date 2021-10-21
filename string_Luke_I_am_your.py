### Level BASIC

### This script will:
# - Read 1 Person Name (Darth Vader or Leia, Han, R2D2)
# - Return the relation to them
# - Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.

#Person	            Relation
#Darth Vader 	    father
#Leia	            sister
#Han	            brother in law
#R2D2	            droid


entry = input("I'm Luke Skywalker, Who are you? ")


def relation_to_luke(entry):
    if entry == "Darth Vader":
        print("Luke, I am your father.")
    elif entry == "Leia":
        print("Luke, I am your sister.")
    elif entry == "Han":
        print("Luke, I am your brother in law.")
    elif entry == "R2D2":
        print("Luke, I am your Droid.")
    else:
        print("Sorry, we are NOT related to.")

relation_to_luke(entry)


### Autor thieslei@gmail.com