import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-t", "--host", help = "target host", required=True)
parser.add_argument("-p", "--port", help = "target port", required=True)

args = parser.parse_args()

closed_loop = f'''<?xml version="1.0"?>
<!DOCTYPE tsung SYSTEM "/usr/share/tsung/tsung-1.0.dtd" []>

<!-- CLOSED LOOP TEMPLATE -->

<tsung loglevel="info">
    <clients>
        <client host="localhost" use_controller_vm="true" maxusers="10000"/>
    </clients>


    <servers>
        <server host="{ args.host }" port="{ args.port }" type="tcp"></server>
    </servers>

    <!-- The "load" section allows to define different arrival phases-->
    <!-- The attribute "duration" is optional, and stops the load test even if
    some sessions are still active-->
    <!-- With "maxnumber" we limit the system to handle a certain amount of users-->
    
    <load duration="30" unit="minute">
        <arrivalphase phase="1" duration="5" unit="minute" wait_all_sessions_end="true">
            <users maxnumber="2000" arrivalrate="10" unit="second"></users>
        </arrivalphase>

        <arrivalphase phase="2" duration="6" unit="minute" wait_all_sessions_end="true">
            <users maxnumber="5000" arrivalrate="30" unit="second"></users>
        </arrivalphase>

        <arrivalphase phase="3" duration="10" unit="minute" wait_all_sessions_end="true">
            <users maxnumber="9500" arrivalrate="40" unit="second"></users>
        </arrivalphase>
    </load>

    <options>
        <option name="file_server" id="queries" value="./queries.csv" />
    </options>

    <sessions>
        <session probability="100" name="closed_loop_test" type="ts_http">

            <setdynvars sourcetype="file" fileid="queries" order="iter" delimiter=";">
                <var name="id" />
            </setdynvars>

            <for from="1" to="10000" var="i">
                <thinktime min="1" max="5" random="true"></thinktime>
                <request subst="true">
                    <http url="http://{ args.host }:{ args.port }/rpc/get_title_details?tconstvar=%%_id%%" method="GET"></http>
                </request>
            </for>
        </session>
    </sessions>

</tsung>'''

print(closed_loop)