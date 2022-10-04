from flask import Flask, jsonify, request

app = Flask(__name__)
#1. 
temperature = [
    {
        "temp_id" : 1,
        "date" : "Oct 4, 2022",
        "temperature" : "37 degrees"
    },
    {
        "temp_id" : 2,
        "date" : "Oct 3, 2022",
        "temperature" : "36 degrees"
    }
]
#2.
@app.route('/temperature', methods=['GET'])
def displayTemperature():
    return jsonify(temperature)

#3.
@app.route('/temperature/<int:index>')
def getTemperature(index):
    get = temperature[index]
    return jsonify(get)

#4. 
@app.route('/temperature', methods=['POST'])
def addTemperatures():
    temperatures = request.get_json()
    temperature.append(temperatures)
    return {'id': len(temperature)},200

#5. 
@app.route('/temperature/<int:index>', methods=['DELETE'])
def deleteTemperature(index):
    temperature.pop(index)
    return 'Temperature was successfully deleted', 200

if __name__== '__main__':
    app.run()