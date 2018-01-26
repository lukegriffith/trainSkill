


class DepartureSkill(object): 

    def __init__(self, NRClient, origin, destination, offset=30):
        self.nrc = NRClient
        self.origin = origin
        self.destination = destination
        self.offset = offset

        self.message = ''

        self.departure = {'found': False, 'sta': None, 'eta': None, 'origin': None}
        self.arrival = {'found':False, 'sta': None, 'eta': None}

        self.find_train()

        print(self.message)



    def get_next_departure(self):
        dep = self.nrc.get_fastest_departures(self.origin, self.destination, self.offset)
        service = dep['departures']['destination'][0]['service']

        print(service)

        if service['sta'] != None:
            self.departure['found'] = True
            self.departure['sta'] = service['sta']
            self.departure['eta'] = service['eta']
            self.departure['origin'] = service['origin']['location'][0]['locationName']

        return service['rsid']

    def get_train_arrival(self, rsid):

        trains = self.nrc.get_arrival_board_with_details(self.origin, self.destination, "to")


        for service in trains['trainServices']['service']:

            if service['rsid'] == rsid:

                print(service) 
                self.arrival['found'] = True
                self.arrival['sta'] = service['sta']
                self.arrival['eta'] = service['eta']
                return 


    def find_train(self):
        
        departure_rsid = self.get_next_departure()

        if self.departure['found']:
            self.get_train_arrival(departure_rsid)
            
            self.message = 'Train from {0} will be at your station at {1}, it will arrive into its destination at {2}. Its running {3}.'.format(
                self.departure['origin'], self.departure['sta'], self.arrival['sta'], self.arrival['eta']
            )

        else:
            self.message = 'No trains found.'

