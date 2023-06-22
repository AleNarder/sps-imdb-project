import argparse
import platform

parser = argparse.ArgumentParser()

parser.add_argument("-t", "--host", help = "target host", required=True)
parser.add_argument("-p", "--port", help = "target port", required=True)
parser.add_argument("-u", "--maxusers", help = "maximum number of users in the system",
                    required = False, default = 100, type=int)
parser.add_argument("-d", "--maxduration", help = "Maximum duration of the test",
                    required = True)
parser.add_argument("-ad", "--arrivalduration", help = "Duration of only one arrival phase",
                    required = True)
parser.add_argument("-ar", "--arrivalrate", help = "Rate of requests sent to the server per second",
                    required = True)
parser.add_argument("-ur", "--userequests", help = "Maximum number of requests per user",
                    required = False, default = 1000)
parser.add_argument("-q", "--query", help = "Query to be executed by the Database",
                    required = True)


args = parser.parse_args()

if platform.system() == 'Darwin':
    dtd_file = '/usr/local/Cellar/tsung/1.8.0/share/tsung/tsung-1.0.dtd'
elif platform.system() == 'Linux':
    dtd_file = '/usr/share/tsung/tsung-1.0.dtd'

closed_loop = f'''<?xml version="1.0"?>
<!DOCTYPE tsung SYSTEM "{ dtd_file }" []>

<!-- CLOSED LOOP TEMPLATE -->

<tsung loglevel="info">
    <clients>
        <client host="localhost" use_controller_vm="true" maxusers="{ args.maxusers + 100}"/>
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
            <users maxnumber="{ args.maxusers }" arrivalrate="{ args.arrivalrate }" unit="second"></users>
        </arrivalphase>
    </load>

    <options>
        <option name="file_server" id="queries" value="./queries.csv" />
    </options>

    <sessions>
        <session probability="100" name="closed_loop_test" type="ts_http">

            <for from="1" to="{ args.userequests }" var="i">

                <setdynvars sourcetype="file" fileid="queries" order="random" delimiter=";">
                    <var name="id" />
                </setdynvars>

                <thinktime value="0.2" random="true"></thinktime>

                <request subst="true">
                    <http url="http://{ args.host }:{ args.port }{ args.query }%%_id%%" method="GET"></http>
                </request>
            </for>
        </session>
    </sessions>

</tsung>'''

print(closed_loop)