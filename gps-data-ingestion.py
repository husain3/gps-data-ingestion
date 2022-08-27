from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/ingest_gps', methods=['POST'])
def door_sensor_change():
    lat = request.args.get('lat')
    long = request.args.get('long')
    altitude = request.args.get('altitude')
    hdop = request.args.get('hdop')
    
    try:

        return Response('OK', status=200, mimetype='text/html')

    except AssertionError as a:
        return Response(f'Unable to process. Reason: {a}', status=400, mimetype='text/html')
    except Exception as e:
        print(e)
        return Response(f'Unable to process. Reason: {e}', status=500, mimetype='text/html')


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=9999)
