import cv2
import os

# Créer le dossier pour les images
input_name = input("Entrez le prénom de la personne : ").lower()
if not os.path.exists('image/' + input_name):
    os.makedirs('image/' + input_name)

# Charger le modèle de détection de visage
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

# Ouvrir la vidéo
video_path = 'video.mp4'
capture = cv2.VideoCapture(video_path)

# Initialiser l'ID des images
id = 0

# Boucle pour lire chaque frame de la vidéo
while True:
    ret, frame = capture.read()
    if not ret:
        break
    
    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Détecter les visages dans l'image
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(50, 50))

    # Boucler à travers chaque visage détecté et enregistrer l'image
    for x, y, w, h in faces:
        # Enregistrer l'image du visage dans le dossier approprié
        cv2.imwrite("image/{}/p-{:d}.png".format(input_name, id), frame[y:y+h, x:x+w])
        id += 1
        # Dessiner un rectangle autour du visage
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Afficher la vidéo avec les visages détectés
    cv2.imshow('Video', frame)

    # Sortir de la boucle si la touche 'q' est pressée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la capture et détruire toutes les fenêtres
capture.release()
cv2.destroyAllWindows()
