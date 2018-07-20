import face_recognition
import cv2
import base64
import auxiliar_array_library as auxArrayLib

import io
import numpy as np
from PIL import Image


def entrenarRedQuercus(known_face_names,known_face_encodings):
    print("Entrenando red...")
    # Load a sample picture and learn how to recognize it.
    javi_image = face_recognition.load_image_file("quercusfaces/javi.jpg")
    javi_image_encoding = face_recognition.face_encodings(javi_image)[0]
    #print(face_recognition.face_landmarks(javi_image, face_locations=None))

    # Load a sample picture and learn how to recognize it.
    alberto_image = face_recognition.load_image_file("quercusfaces/alberto.jpg")
    alberto_image_encoding = face_recognition.face_encodings(alberto_image)[0]

    # Load a sample picture and learn how to recognize it.
    victor_image = face_recognition.load_image_file("quercusfaces/victor.jpg")
    victor_image_encoding = face_recognition.face_encodings(victor_image)[0]

    # Load a sample picture and learn how to recognize it.
    paula_image = face_recognition.load_image_file("quercusfaces/paula.jpg")
    paula_image_encoding = face_recognition.face_encodings(paula_image)[0]

    # Load a sample picture and learn how to recognize it.
    justo_image = face_recognition.load_image_file("quercusfaces/justo.jpg")
    justo_image_encoding = face_recognition.face_encodings(justo_image)[0]

    # Load a sample picture and learn how to recognize it.
    marcos_image = face_recognition.load_image_file("quercusfaces/marcos.jpg")
    marcos_image_encoding = face_recognition.face_encodings(marcos_image)[0]

    # Load a sample picture and learn how to recognize it.
    juan_image = face_recognition.load_image_file("quercusfaces/juanher.jpg")
    juan_image_encoding = face_recognition.face_encodings(juan_image)[0]

    # Load a sample picture and learn how to recognize it.
    quique_image = face_recognition.load_image_file("quercusfaces/quique.jpg")
    quique_image_encoding = face_recognition.face_encodings(quique_image)[0]

    # Load a sample picture and learn how to recognize it.
    pery_image = face_recognition.load_image_file("quercusfaces/pery.png")
    pery_image_encoding = face_recognition.face_encodings(pery_image)[0]

    # Load a sample picture and learn how to recognize it.
    fernando_image = face_recognition.load_image_file("quercusfaces/fernando.png")
    fernando_image_encoding = face_recognition.face_encodings(fernando_image)[0]

    # Load a sample picture and learn how to recognize it.
    mario_image = face_recognition.load_image_file("quercusfaces/mario.jpg")
    mario_image_encoding = face_recognition.face_encodings(mario_image)[0]

    # Create arrays of known face encodings and their names
    known_face_encodings.extend([
        alberto_image_encoding,
        victor_image_encoding,
        paula_image_encoding,
        justo_image_encoding,
        marcos_image_encoding,
        juan_image_encoding,
        quique_image_encoding,
        pery_image_encoding,
        fernando_image_encoding,
        mario_image_encoding,
        javi_image_encoding
    ])
    known_face_names.extend([
        "Alberto",
        "Victor",
        "Paula",
        "Justo",
        "Marcos",
        "Juan",
        "Quique",
        "Pery",
        "Fernando",
        "Mario",
        "Javier Rojo"
    ])

    print(">>>>> Red entrenada ...")


def saveFaces(known_face_names, known_face_encodings):

    try:
        name_file= open("files/nameFile.txt", "a")

        for face_name in known_face_names:
            name_file.write(face_name+"\n")

        name_file.close()
    except:
        print("No se ha podido abrir el fichero de nombres")

    # try:
    #     encodings_file= open("encodingsFile.txt", "a")
    #
    #     for face_encoding in known_face_encodings:
    #
    #         encodings_file.write(str(face_encoding)+"\n")
    #
    #     encodings_file.close()
    # except:
    #     print("No se ha podido abrir el fichero de encodings")

    try:
        encodings_file= open("files/encodingsFile.txt", "a")
        for face_encoding in known_face_encodings:
            for encoding_value in face_encoding:
                encodings_file.write(str(encoding_value)+"\n")
            encodings_file.write("##End##\n")

        encodings_file.close()
    except:

        print("No se ha podido abrir el fichero de encodings para salvar los datos")



def get_encoding(image_base64):

    image_fit_encoding = []

    imgdata= stringToImage(image_base64)
    imgCV= toRGB(imgdata)
    cv2.imwrite('imageFit.png', imgCV)

    image_fit = face_recognition.load_image_file("imageFit.png")

    image_fit_encodings= face_recognition.face_encodings(image_fit)

    if image_fit_encodings.__len__() >0:
        image_fit_encoding= image_fit_encodings[0]

    return image_fit_encoding


def myreadlines(f, newline):
  buf = ""
  while True:
    while newline in buf:
      pos = buf.index(newline)
      yield buf[:pos]
      buf = buf[pos + len(newline):]
    chunk = f.read(4096)
    if not chunk:
      yield buf
      break
    buf += chunk


#PRE: known_face_names and known_face_encodings must be empty arrays.
def loadFaces(known_face_names, known_face_encodings):

    try:
        with open('files/nameFile.txt') as f:
            for name in myreadlines(f, "\n"):
                if not name.__eq__(""):
                    known_face_names.append(name)

    except:
        print("No se ha podido abrir el fichero de nombres para leer los nombres registrados")

    # try:
    #     with open('encodingsFile.txt') as f:
    #         for encoding in myreadlines(f, "]"):
    #             print (encoding+"]")
    #             known_face_encodings.append(encoding+"]")
    # except:
    #     print("No se ha podido abrir el fichero de encodings")

    try:
        encoding=[]
        with open('files/encodingsFile.txt') as f:
            for encoding_value in myreadlines(f, "\n"):
                if not encoding_value.__eq__(""):
                    if encoding_value.__eq__("##End##"):
                        known_face_encodings.append(encoding)
                        encoding=[]
                    else:
                        encoding.append(float(encoding_value))
    except:
        print("No se ha podido abrir el fichero de encodings para leer los datos")


# Take in base64 string and return PIL image
def stringToImage(base64_string):
    imgdata = base64.b64decode(base64_string)
    return Image.open(io.BytesIO(imgdata))

# convert PIL Image to an RGB image( technically a numpy array ) that's compatible with opencv
def toRGB(image):
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)


def reconocerPersona(known_face_names, known_face_encodings, image64):

    imgdata= stringToImage(image64)
    imgCV= toRGB(imgdata)
    cv2.imwrite('image.png', imgCV)

    print(str(imgdata))

    img = cv2.imread('image.png')
    rgb_frame= face_recognition.load_image_file("image.png")

    # Find all the faces and face encodings in the frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        name = "Unknown"

# MODIFICATED CODE

        # # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]
        #     distance = distances[first_match_index]
        #     print("COINCIDENCIAS:")
        #     print(matches)
        #     print("DISTANCIAS:")
        #     print(distances)
        #     print('{    "name":'+name+
        #           '"distance:"'+str(distance)+'}')

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            match_index, distance = auxArrayLib.selectLowerValue(distances)
            name = known_face_names[match_index]
            print("COINCIDENCIAS:")
            print(matches)
            print("DISTANCIAS:")
            print(distances)
            print('{    "name":' + name +
                  '"distance:"' + str(distance) + '}')

# END MODIFICATED CODE

        # Draw a box around the face
        cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(img, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(img, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        #
        #
        # cv2.imshow("image", img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    try:
        retval, buffer = cv2.imencode('.jpg', img)
        img_encoded = base64.b64encode(buffer)
        return img_encoded
    except:
        print(">> NO se ha podido convertir la imagen a base64")
        return image64