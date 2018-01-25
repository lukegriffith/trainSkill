


class DepartureSkill(object): 

    def __init__(self, NRClient, origin, destination, offset=30):
        self.nrc = NRClient
        self.origin = origin
        self.destination = destination
        self.offset = offset


    def getNextTrain(self):
        
        dep = self.nrc.get_fastest_departures(self.origin, self.destination, self.offset)


        rsid = dep['departures']['destination'][0]['service']['rsid']

        return rsid