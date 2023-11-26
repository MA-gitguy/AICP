# Train ticket bot
Toward_journey = {"9:00": 480, "11:00": 480, "13:00": 480, "15:00": 480}
Returned = {"10:00":480, "12:00": 480, "14:00": 480, "16:00": 640}


def total_price(num_tickets, disct):
    Total_Amount = (num_tickets*25*2)-((2*disct)*25)
    print("\nYou need to pay: \n$", Total_Amount)
    remaining_tickets()
    start_day()


def remaining_tickets():
    print("\nThe Tickets remaining of 09:00 clock is: ", Toward_journey["9:00"])
    print("The Tickets remaining of 11:00 clock is: ", Toward_journey["11:00"])
    print("The Tickets remaining of 13:00 clock is: ", Toward_journey["13:00"])
    print("The Tickets remaining of 15:00 clock is: ", Toward_journey["15:00"])
    
def return_remaining():
    print("\nThe Tickets remaining of 10:00 clock is: ", Returned["10:00"])
    print("The Tickets remaining of 12:00 clock is: ", Returned["12:00"])
    print("The Tickets remaining of 14:00 clock is: ", Returned["14:00"])
    print("The Tickets remaining of 16:00 clock is: ", Returned["16:00"])


def discount(num_tickets):
        disct = num_tickets/10
        total_price(num_tickets, int(disct))
    

def return_time(selected_tickets):
    return_remaining()
    print("Which time you want to return: \n1. 10:00\t\t2. 12:00\t3. 14:00\t4. 16:00")
    return_t = input()
    if return_t == "1" or return_t == "10" or return_t == "10:00" and int(return_t) <= Returned["10:00"]:
        if Returned["10:00"] == 0:
            print("The tickets for this time are sold out.\nPlease select another time to returned back: ")
            return_time(selected_tickets)
        else:
            num_tickets = Returned["10:00"]-selected_tickets
            Returned["10:00"] = num_tickets
    elif return_t == "2" or return_t == "12" or return_t == "12:00" and int(return_t) <= Returned["12:00"]:
        if Returned["12:00"] == 0:
            print("The tickets for this time are sold out.\nPlease select another time to returned back: ")
            return_time(selected_tickets)
        else:
            num_tickets = Returned["12:00"]-selected_tickets
            Returned["12:00"] = num_tickets
    elif return_t == "3" or return_t == "14" or return_t == "14:00"and int(return_t) <= Returned["14:00"]:
        if Returned["14:00"] == 0:
            print("The tickets for this time are sold out.\nPlease select another time to returned back: ")
            return_time(selected_tickets)
        else:
            num_tickets = Returned["14:00"]-selected_tickets
            Returned["14:00"] = num_tickets
    elif return_t == "4" or return_t == "16" or return_t == "16:00" and int(return_t) <= Returned["16:00"]:
        if Returned["16:00"] == 0:
            print("The tickets for this time are sold out.\nPlease select another time to returned back: ")
            return_time(selected_tickets)
        else:
            num_tickets = Returned["16:00"]-selected_tickets
            Returned["16:00"] = num_tickets
    else:
        print("Please Select another time to return: ")
        return_time(selected_tickets)
        

def start_day():
    print("\nWhich time you want to go Sir: \n1. 9:00\t\t2. 11:00\t3. 13:00\t4. 15:00")
    selected_time = input()
    print("How much tickets you want to Purchase: \nNote: On each ticket 10 tickets purchase there is one free ticket!")
    selected_tickets = int(input())
    if selected_time == "1" or selected_time == "9" or selected_time == "9:00" and selected_tickets <= Toward_journey["9:00"]:
        if Toward_journey["9:00"] == 0:
            print("The tickets for this time are sold out.\nPlease select another time to travel: ")
            start_day()
        else:
            num_tickets = Toward_journey["9:00"]-selected_tickets
            Toward_journey["9:00"] = num_tickets
            return_time(selected_tickets)
            discount(selected_tickets)
    elif selected_time == "2" or selected_time == "11" or selected_time == "11:00" and selected_tickets <= Toward_journey["11:00"]:
        if Toward_journey["11:00"] == 0:
            print("The tickets for this time are sold out.\nPlease select another time to travel: ")
            start_day()
        else:
            num_tickets = Toward_journey["11:00"]-selected_tickets
            Toward_journey["11:00"] = num_tickets
            return_time(selected_tickets)
            discount(selected_tickets)
    elif selected_time == "3" or selected_time == "13" or selected_time == "13:00" and selected_tickets <= Toward_journey["13:00"]:
        if Toward_journey["13:00"] == 0:
            print("The tickets for this time are sold out.\nPlease select another time to travel: ")
            start_day()
        else:
            num_tickets = Toward_journey["13:00"]-selected_tickets
            Toward_journey["13:00"] = num_tickets
            return_time(selected_tickets)
            discount(selected_tickets)
    elif selected_time == "4" or selected_time == "15" or selected_time == "15:00" and selected_tickets <= Toward_journey["15:00"]:
        if Toward_journey["15:00"] == 0:
            print("The tickets for this time are sold out.\nPlease select another time to travel: ")
            start_day()
        else:
            num_tickets = Toward_journey["15:00"]-selected_tickets
            Toward_journey["15:00"] = num_tickets
            return_time(selected_tickets)
            discount(selected_tickets)
    else:
         start_day()
    
start_day()