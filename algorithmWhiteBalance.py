import cv2
import numpy as np

def white_balance(image):
    # Calcola la media dei canali R, G, B prima del bilanciamento
    avg_b_before = np.mean(image[:, :, 0])
    avg_g_before = np.mean(image[:, :, 1])
    avg_r_before = np.mean(image[:, :, 2])

    # Calcola la media dei canali R, G, B
    avg_b = np.mean(image[:, :, 0])
    avg_g = np.mean(image[:, :, 1])
    avg_r = np.mean(image[:, :, 2])

    # Calcola il fattore di bilanciamento per ogni canale
    avg = (avg_b + avg_g + avg_r) / 3
    avg_b /= avg
    avg_g /= avg
    avg_r /= avg

    # Applica il bilanciamento ai canali dell'immagine
    image[:, :, 0] = np.clip(image[:, :, 0] * avg_b, 0, 255)
    image[:, :, 1] = np.clip(image[:, :, 1] * avg_g, 0, 255)
    image[:, :, 2] = np.clip(image[:, :, 2] * avg_r, 0, 255)

    # Calcola la media dei canali R, G, B dopo il bilanciamento
    avg_b_after = np.mean(image[:, :, 0])
    avg_g_after = np.mean(image[:, :, 1])
    avg_r_after = np.mean(image[:, :, 2])

    return image, (avg_b_before, avg_g_before, avg_r_before), (avg_b_after, avg_g_after, avg_r_after)

# Percorso dell'immagine
image_path = r"QUA VA INSERITO IL PERCORSO DELL'IMMAGINE"

# Carica l'immagine specificando il percorso
input_image = cv2.imread(image_path)
if input_image is None:
    print("Impossibile caricare l'immagine. Controlla il percorso specificato.")
else:
    # Applica il bilanciamento del bianco all'immagine e ottieni i valori medi prima e dopo
    balanced_image, avg_before, avg_after = white_balance(input_image)

    # Mostra i valori medi prima e dopo il bilanciamento del bianco
    print("Valori medi dei canali RGB prima del bilanciamento:", avg_before)
    print("Valori medi dei canali RGB dopo il bilanciamento:", avg_after)

    # Mostra l'immagine originale e quella bilanciata
    cv2.imshow('Original Image', input_image)
    cv2.imshow('Balanced Image', balanced_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
