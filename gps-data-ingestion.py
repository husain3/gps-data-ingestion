from flask import Flask, request, Response
import datetime
import csv

app = Flask(__name__)

column_names = ['latitude', 'longitude', 'altitude', 'hdop', 'datetime']

@app.route('/ingest_gps', methods=['POST'])
def door_sensor_change():
    try:
        lat = request.args.get('lat')
        long = request.args.get('long')
        altitude = request.args.get('altitude')
        hdop = request.args.get('hdop')

        gps_data = {}
        gps_data['latitude'] = request.args.get('lat')
        gps_data['longitude'] = request.args.get('long')
        gps_data['altitude'] = request.args.get('altitude')
        gps_data['hdop'] = request.args.get('hdop')
        gps_data['datetime'] = datetime.datetime.now()

        with open('gps_data.csv', 'a') as csv_file:
            dict_object = csv.DictWriter(csv_file, fieldnames=column_names)
            dict_object.writerow(gps_data)

        return Response('OK', status=200, mimetype='text/html')

    except AssertionError as a:
        return Response(f'Unable to process. Reason: {a}', status=400, mimetype='text/html')
    except Exception as e:
        print(e)
        return Response(f'Unable to process. Reason: {e}', status=500, mimetype='text/html')


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=9999)
