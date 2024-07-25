service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Function to generate the next ticket ID
def next_id():
    last_id = max(service_tickets.keys(), default="Ticket000")
    new_id_num = int(last_id.replace("Ticket", "")) + 1
    return f"Ticket{new_id_num:03}"

# Function to open a new service ticket
def new_ticket():
    new_id = next_id()
    while True:
        customer = input("Enter customer name: \n")
        issue = input("Enter issue description: \n")
        print(f"Customer: {customer}, Issue: {issue}")
        correct = input("Is this information correct? (yes/no): ").lower()
        if correct == "yes":
            service_tickets[new_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
            print(f"New ticket created: {new_id}")
            break
        elif correct == "no":
            print("Please enter valid information.")
            continue

# Function to update a service ticket
def update_ticket():
    ticket_id = input("Enter the ticket ID to update (e.g., Ticket001): \n")
    if ticket_id in service_tickets:
        new_status = input("Enter new status (open/closed): \n").lower()
        if new_status in ["open", "closed"]:
            service_tickets[ticket_id]["Status"] = new_status
            print(f"Ticket {ticket_id} updated to {new_status}.")
        else:
            print("Invalid status. Please enter 'open' or 'closed'.")
    else:
        print("Ticket ID not found.")

# Function to display all service tickets
def display_tickets():
    if service_tickets:
        for ticket_id, ticket_info in service_tickets.items():
            print(f"{ticket_id}: {ticket_info}")
    else:
        print("No tickets available.")

# Function to filter tickets by status
def filter_tickets():
    status = input("Enter the status to filter by (open/closed): \n").lower()
    filtered_tickets = {k: v for k, v in service_tickets.items() if v["Status"] == status}
    if filtered_tickets:
        for ticket_id, ticket_info in filtered_tickets.items():
            print(f"{ticket_id}: {ticket_info}")
    else:
        print(f"No tickets with status '{status}'.")

# Function to delete a service ticket
def delete_ticket():
    ticket_id = input("Enter the ticket ID to delete (e.g., Ticket001): \n")
    if ticket_id in service_tickets:
        del service_tickets[ticket_id]
        print(f"Ticket {ticket_id} deleted.")
    else:
        print("Ticket ID not found.")

# Main menu function
def main():
    while True:
        ans = input('''
SERVICE TICKET MANAGER
Enter the corresponding number for the action you'd like to take:
    1 - Open a new service ticket.
    2 - Update a service ticket.
    3 - Display all service tickets.
    4 - Filter by status. 
    5 - Delete a service ticket.                              
    6 - Quit
''')
        if ans == '1':
            new_ticket()
        elif ans == '2':
            update_ticket()
        elif ans == '3':
            display_tickets()
        elif ans == '4':
            filter_tickets()
        elif ans == '5':
            delete_ticket()
        elif ans == '6':
            print("Thanks for using the Service Ticket Manager. Have a great day!")
            break
        else:
            print("Please enter a valid option.")

if __name__ == "__main__":
    main()
