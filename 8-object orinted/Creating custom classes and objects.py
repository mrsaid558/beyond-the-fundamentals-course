# thsi is the third lesson in chapter 8
# Creating custom classes and objects

class Attendee:
    "common base class for all attendeers"
    
    def __init__(self, name, tickets):
        self.name = name
        self.tickets = tickets
    
    def displayAttendee(self):
        print(f"Name: {self.name}, Tickets: {self.tickets}")
    
    def addTicket(self):
        self.tickets += 1
        print(f"{self.name} tickets increase to {self.tickets}")
        
attendee_1 = Attendee("Ahmed", 3)
attendee_2 = Attendee("Mohamed", 1)

attendee_2.addTicket()
attendee_2.addTicket()

attendee_1.displayAttendee()
attendee_2.displayAttendee()