#!/usr/bin/python
#--------------------------------------------------------------------------------------------------------------------------------
# Import Libraries
import sys
import argparse
from stravalib import Client
#--------------------------------------------------------------------------------------------------------------------------------
# **** Todo *****
# ----
# Setup error logging
# change unit's to usable
#--------------------------------------------------------------------------------------------------------------------------------


# Variables
#--------------------------------------------------------------------------------------------------------------------------------
stypes='distance,altitude,velocity_smooth,heartrate,cadence,watts,temp,moving,grade_smooth'
a_stypes = stypes.split(',')
strm_ser_type='time'
reso='default'
row=""
#--------------------------------------------------------------------------------------------------------------------------------
# Parse command-line options
#--------------------------------------------------------------------------------------------------------------------------------
parser = argparse.ArgumentParser(description='options for strapy',epilog="The Filoutput peice hasn't been implemented yet")

parser.add_argument('-t',metavar='STRaccess_token', required=True,
                    dest='STRaccess_token', action='store',
                    help='Stava Access Token - specific to this app')

parser.add_argument('-s',metavar='STRactsess', required=True,
                    dest='STRactsess', action='store',
                    help='Stava session ID for activity to be analysed')

parser.add_argument('-o', dest='outfile', action='store',
                    help='output file Std out if not')

#not sure why needed
parser.add_argument('-c',metavar='STRclientid', required=False,
                    dest='STRclientid', action='store',
                    help='Stava Client ID')

args = parser.parse_args()

#--------------------------------------------------------------------------------------------------------------------------------

client = Client(access_token=args.STRaccess_token)

#print("*** - Athlete Method")
#athlete = client.get_athlete()
#print("Hello, {}. I know your email is {}".format(athlete.firstname, athlete.email))

#print("*** - Activity Method")
#activity = client.get_activity(anal_sess)
#print("type = " + activity.type)
#print("distance = " + format(activity.distance))

# Activities can have many streams, you can request desired stream types
#print("type={0.type} distance={1} km".format(activity,unithelper.kilometers(activity.distance)))

#print("*** - Streams Method")
streams = client.get_activity_streams(args.STRactsess, types=a_stypes, series_type=strm_ser_type)

header = strm_ser_type      
for x in streams.keys():
        header += (",{}").format(x)
print(header)

#header=','.join(streams.keys()).format()
#print("HEADER",header)
#sys.exit()

iter=0
for t in streams[strm_ser_type].data:
    row = format(streams[strm_ser_type].data[iter])
    for k in streams.keys():
        row += "," + format(streams[k].data[iter])
    iter += 1
    print(row)
    

# Activities can have many streams, you can request n desired stream types
#types = ['time', 'latlng', 'altitude', 'heartrate', 'temp', ]
#streams = client.get_activity_streams(STRactsess, types=types, resolution='medium')
#  Result is a dictionary object.  The dict's key are the stream type.
#if 'altitude' in streams.keys()
#    print(streams['altitude'].data)
    
#assert len(list(activities)) == 10

#activity = client.get_activity(activity_id)
#comments = activity.comments
#comments.limit = 1
#assert len(list(comments)) == 1