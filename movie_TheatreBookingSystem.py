capacity=350
remaining_seats = capacity

total_bookings=0
tickets_sold=0
rejected_bookings=0

while remaining_seats>0:
  no_ofTickets=int(input("Enter no of tickets(0 for exit):"))
  if no_ofTickets==0:
    break
  if(no_ofTickets<1 or no_ofTickets>15 or no_ofTickets>remaining_seats):
    print("Booking Rejected: Invalid ticket Count")
    rejected_bookings+=1
    continue
  valid_booking= True
  for i in range(no_ofTickets):
    age=int(input(f"enter age of a person{i+1}:"))

    if age <12:
      valid_booking=False
      break
  if not valid_booking:
    print("Booking Rejected - Age Restriction")
    rejected_bookings+=1
    continue
  
  remaining_seats-=no_ofTickets
  tickets_sold+=no_ofTickets
  total_bookings+=1

  print(f"Booking Confirmed-{no_ofTickets} Tickets")

print("Total Bookings:", total_bookings)
print("Total Tickets Sold:", tickets_sold)
print("Rejected Bookings:", rejected_bookings)
print("Remaining Seats:", remaining_seats)


    