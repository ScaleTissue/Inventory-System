from datetime import datetime

users = {
    'Kenneth': 'Seraspe',
    'user2': 'password2',
    'user3': 'password3',
    '1': '1',
}

#Login --Start--
def lgn_choices():
    print("Welcome to Cevent Event Planner")
    
    
    while True:
        print("Input your choice from 1-3")
        print("1.Login")
        print("2.Register")
        print("3.Exit")

        lgn_choice =input("Enter your choice: ")

        if lgn_choice == '1':
            return True
        elif lgn_choice == '2':
            main_reg()
        elif lgn_choice == '3':
            print("Exiting this bull crap")
            exit(0)
        else:
            print("Invalid Input")
            



def stm_login(username, password):
    if username in users and users[username] == password:
        return True
    else: 
        return False


def main_login():
    print("PLease input your credentials")


    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if stm_login(username, password):
            print("Login successful!")
            break
        else:
            print("Invalid username or password, please try again")


#register start
def lgn_reg(username, password):
    if username in users:
        print("user already exists. Please try another username.")
    else:
        users[username] = password
        print("You have successfully registered")

def main_reg():
    print("Input your credentials here: ")

    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        confirm_password = input("confirm your password: ")
    
        if password != confirm_password:
            print("Password don't match with the confirmation password  ")
        else:
            lgn_reg(username, password)
            break

#register end


#login --End--


#CRUD function
#main menu start

event_planner = {}

# Function to add an event to the planner
def add_event():
    name = input("Enter the name of the event: ")
    event_type = input("Enter the type of event: ")
    venue = input("Enter the venue: ")
    date_time = input("Enter the date and time (MM/DD/YYYY HH:MM AM/PM): ")

    # Validate date and time
    try:
        date_time_obj = datetime.strptime(date_time, "%m/%d/%Y %I:%M %p")
    except ValueError:
        print("Invalid date and time format. Please enter in MM/DD/YYYY HH:MM AM/PM format.")
        return

    special_guests = input("Enter the special guests (separated by commas if multiple): ").split(',')
    host_name = input("Enter the host name: ")

    event_planner[name] = {
        'Event Type': event_type,
        'Venue': venue,
        'Date and Time': date_time_obj.strftime("%m/%d/%Y %I:%M %p"),
        'Special Guests': special_guests,
        'Host Name': host_name
    }
    print("Event added successfully!")

# Function to view all events in the planner
def view_events():
    if event_planner:
        print("Your events:")
        for name, details in event_planner.items():
            print("Event Name:", name)
            print("Event Type:", details['Event Type'])
            print("Venue:", details['Venue'])
            print("Date and Time:", details['Date and Time'])
            print("Special Guests:", ', '.join(details['Special Guests']))
            print("Host Name:", details['Host Name'])
            print()
    else:
        print("No events scheduled.")

# Function to update an event in the planner
def update_event(name):
    if name in event_planner:
        print("Update Event:")
        event_type = input("Enter the new type of event: ")
        venue = input("Enter the new venue: ")
        date_time = input("Enter the new date and time (MM/DD/YYYY HH:MM AM/PM): ")
        
        # Validate date and time
        if not validate_date_time(date_time):
            print("Invalid date and time format. Please enter in MM/DD/YYYY HH:MM AM/PM format.")
            return

        special_guests = input("Enter the new special guests (separated by commas if multiple): ").split(',')
        host_name = input("Enter the new host name: ")

        # Update event details
        event_planner[name]['Event Type'] = event_type
        event_planner[name]['Venue'] = venue
        event_planner[name]['Date and Time'] = date_time
        event_planner[name]['Special Guests'] = special_guests
        event_planner[name]['Host Name'] = host_name

        print(f"Event '{name}' updated successfully!")
    else:
        print(f"No event found with the name '{name}'.")

def validate_date_time(date_time):
    try:
        datetime.strptime(date_time, "%m/%d/%Y %I:%M %p")
        return True
    except ValueError:
        return False


def delete_event(name):
    if name in event_planner:
        del event_planner[name]
        print(f"Event '{name}' deleted successfully!")
    else:
        print(f"No event found with the name '{name}'.")

def main():
    print("Welcome to the Event Planner!")

    while True:
        print("\nMenu:")
        print("1. Add Event")
        print("2. View Events")
        print("3. Update Event")
        print("4. Delete Event")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_event()
        elif choice == '2':
            view_events()
        elif choice == '3':
            name = input("Enter the name of the event to update: ")
            update_event(name)
        elif choice == '4':
            name = input("Enter the name of the event to delete: ")
            delete_event(name)
        elif choice == '5':
            print("Thank you for using the Event Planner. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


lgn_choices()
main_login()
main()