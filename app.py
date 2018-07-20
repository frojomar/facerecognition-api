from Flask import Flask, jsonify, request
import face_recognitionImpl as frImpl
import os

app = Flask(__name__)


@app.route('/', methods=['POST'])
def reconocer_persona_api():

    print("Nueva petición a la API: Reconocer persona")

    json_data = request.get_json()
    image64 = json_data['image']

    print(image64)

    known_face_encodings = []
    known_face_names = []
    frImpl.loadFaces(known_face_names, known_face_encodings)

    result=frImpl.reconocerPersona(known_face_names, known_face_encodings, image64)

    return result

    #return jsonify("{image:"+str(result)+"}")

@app.route('/addPerson', methods=['POST'])
def nueva_persona_api():

    print("Nueva petición a la API: Añadir persona")

    json_data = request.get_json()
    image64 = json_data['image']
    name= json_data['name']

    print(image64)
    print("NOMBRE PERSONA:"+str(name))

    if str(name).strip().__eq__(""):
        return jsonify("{'status': 'errorName'}")

    else:
        face_encoding= frImpl.get_encoding(image64)

        if face_encoding.__len__() <= 0:
            return jsonify("{'status': 'errorImage'}")

        else:
            print(face_encoding)

            known_face_encodings = [face_encoding]
            known_face_names = [name]
            frImpl.saveFaces(known_face_names,known_face_encodings)

            return jsonify("{'status': 'ok'}")

if __name__=='__main__':
    port=os.environ["PORT"]
    app.run(host='0.0.0.0', port=int(port), debug=True, threaded=True)
