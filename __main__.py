''' trainSKill  '''
from trainSkill.NationalRail import NrClient

TOKEN = '78857c37-7ed6-4b13-bfde-bc5409bc3de8'
URI = 'https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2017-10-01'




NR = NrClient(TOKEN, URI)


print(NR.getFastestDepartures('SNS', 'WAT', 30))

input()



#NR.getArrivalBoard('SNS', 'WAT', 'from')

print(NR.getArrivalBoardWithDetails('WAT', 'SNS', 'from'))



print(NR.getArrivalBoardWithDetails('WAT'))