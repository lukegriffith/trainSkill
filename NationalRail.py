

from zeep import Client



class NrClient(object):


    def __init__(self, token, uri):
        ''' Object constructs with access token from site. '''

        
        

        
        self.client = Client(uri)

        accesskey_type = self.client.get_type('ns0:AccessToken')
        
        self.token = accesskey_type(TokenValue=token)

    def getFastestDepartures(self, origin, destination, offset):
        ''' query api for the fastest departures from origin to destination, offset in minutes. '''        
        
        return self.client.service.GetFastestDepartures(crs=origin, filterList=destination, timeOffset = offset, timeWindow= 120, _soapheaders={'AccessToken': self.token})
        

    def getArrivalBoardWithDetails(self, target, filterCode=None, filtertype=None):
        ''' Method gets the arrival board, for the target with the filter type being to or from.
            FilterCode is the station code of the filter, by default None.'''
        return self.client.service.GetArrBoardWithDetails(numRows = 10, crs=target, filterCrs=filterCode, filterType=filtertype, _soapheaders={'AccessToken': self.token})

