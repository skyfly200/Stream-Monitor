import requests, json, iso8601, datetime, pytz

# Way Highs Main Server URL
# http://162.243.92.85:8000
def streamStats(serverUrl):
    # gets stats from icecast server in JSON format
    return requests.get((serverUrl + '/status-json.xsl'))

def streamTime(serverUrl):
    # gets stats from icecast server in JSON format
    res = streamStats(serverUrl)

    # catch errors in processing JSON
    try:
        # parse client start timestamp from server stats
        connect_timestamp_iso = json.loads(res.text)['icestats']['source']['stream_start_iso8601']
    except:
        print "Server JSON processing error", res.txt

    # convert timestamp from ISO8601 format to python datetime object
    connect_timestamp = iso8601.parse_date(connect_timestamp_iso)

    return connect_timestamp

def streamTimeUp(serverUrl):
    # get timestamp of last client connection
    connect_timestamp = streamTime(serverUrl)

    # time zone info of server start timestamp
    tz_info = connect_timestamp.tzinfo

    # time since the client connected last
    connection_length = datetime.datetime.now(tz_info) - connect_timestamp

    return connection_length.seconds
