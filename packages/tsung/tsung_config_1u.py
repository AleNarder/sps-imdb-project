import argparse
import platform

parser = argparse.ArgumentParser()

parser.add_argument("-t", "--host", help = "target host", required=True)
parser.add_argument("-p", "--port", help = "target port", required=True)
parser.add_argument("-d", "--maxduration", help = "Maximum duration of the test",
                    required = True)
parser.add_argument("-ad", "--arrivalduration", help = "Duration of only one arrival phase",
                    required = True)
parser.add_argument("-ur", "--userequests", help = "Maximum number of requests per user",
                    required = False, default = 1000)
parser.add_argument("-q", "--query", help = "Query to be executed by the Database",
                    required = True)


args = parser.parse_args()

dtd_file = ''

if platform.system() == 'Darwin':
    dtd_file = '/usr/local/Cellar/tsung/1.8.0/share/tsung/tsung-1.0.dtd'
elif platform.system() == 'Linux':
    dtd_file = '/usr/share/tsung/tsung-1.0.dtd'

closed_loop = f'''<?xml version="1.0"?>
<!DOCTYPE tsung SYSTEM "{ dtd_file }" []>

<!-- CLOSED LOOP TEMPLATE -->

<tsung loglevel="info">
    <clients>
        <client host="localhost" use_controller_vm="true"/>
    </clients>

    <servers>
        <server host="{ args.host }" port="{ args.port }" type="tcp"></server>
    </servers>

    <!-- The "load" section allows to define different arrival phases-->
    <!-- The attribute "duration" is optional, and stops the load test even if
    some sessions are still active-->
    <!-- With "maxnumber" we limit the system to handle a certain amount of users-->
    
    <load duration="{ args.maxduration }" unit="minute">
        <arrivalphase phase="1" duration="{ args.arrivalduration }" unit="minute" wait_all_sessions_end="true">
            <users maxnumber="1" arrivalrate="1" unit="second"></users>
        </arrivalphase>
    </load>

    <options>
        <option name="file_server" id="queries" value="./queries.csv" />
    </options>

    <sessions>
        <session probability="100" name="single_user_testing" type="ts_http">

            <for from="1" to="{ args.userequests }" var="i">

                <setdynvars sourcetype="file" fileid="queries" order="random" delimiter=";">
                    <var name="id" />
                </setdynvars>

                <!-- Transaction to avoid inserting the connection time in the transaction-mean computation -->
                <transaction name="query">
                    <!-- Execute Request -->
                    <request subst="true">
                        <http url="http://{ args.host }:{ args.port }{ args.query }%%_id%%" method="GET"></http>
                    </request>
                </transaction>

            </for>
        </session>
    </sessions>

</tsung>'''

print(closed_loop)