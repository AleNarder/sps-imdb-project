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
        <client host="localhost" use_controller_vm="true" />
    </clients>


    <servers>
        <server host="{ args.host }" port="{ args.port }" type="tcp"></server>
    </servers>


    <load duration="5" unit="minute">
        <arrivalphase phase="1" duration="10" unit="minute">
            <users maxnumber="10" arrivalrate="2" unit="second"></users>
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
                <thinktime min="2" max="10" random="true"></thinktime>
                <request subst="true">
                    <http url="http://{ args.host }:{ args.port }/rpc/get_title_details?tconstvar=%%_id%%" method="GET"></http>
                </request>
            </for>
        </session>
    </sessions>

</tsung>'''

print(closed_loop)