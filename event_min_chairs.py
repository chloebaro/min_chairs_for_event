def compute_min_number_chairs(times_per_person):
    """ times_per_person is a list of 2-entry tuples, where each tuple holds a person's entry and departure time from
    the event respectively, where the departure time > the entry time

    for example: [(1, 4), (2, 5)] is a valid input to this function
    """
    if len(times_per_person) > 0:

        min_entry_time = min([person[0] for person in times_per_person])
        max_departure_time = max([person[1] for person in times_per_person])

        chairs_needed_per_time = [0 for _ in range(min_entry_time, max_departure_time)]

        for person in times_per_person:
            for j in range(person[0], person[1]):
                chairs_needed_per_time[j - min_entry_time] += 1

        return max(chairs_needed_per_time)

    else:
        return 0


if __name__ == '__main__':
    people_times = []
    people = {}

    print("Welcome to my restaurant manager.\n")
    print("Enter \"add\" to add an attendee, \"del\" to delete an attendee, "
          "\"compute\" to compute the minimum number of chairs required for the event, "
          "\"reset\" to reset the list of people attending the event, or \"q\" to quit.\n")
    while True:
        command = input()
        if command.lower() == "add":
            name = input("Enter the full name of the attendee: ").lower()
            start_time = int(input("Enter the time they will arrive at the event: "))
            end_time = int(input("Enter the time they will leave the event: "))
            tup = (start_time, end_time)
            people[name] = tup
            people_times.append(tup)
        elif command.lower() == "del":
            name = input("Enter the name of the person you want to remove: ").lower()
            try:
                tup_to_delete = people[name]
                people_times.remove(tup_to_delete)
                del people[name]
            except KeyError:
                print("Person not found. \n")
        elif command.lower() == "compute":
            min_chairs = compute_min_number_chairs(people_times)
            print("The minimum number of chairs needed for the event is {}".format(min_chairs))
        elif command.lower() == "reset":
            people_times = []
            people = {}
        elif command.lower() == "q":
            break
        else:
            print("Command not recognized.\n")




