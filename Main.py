

from API import get_prediction

# path to trained model
model_path = r"C:\Users\Jeevika\OneDrive\Desktop\phishing\Phishing-Attack-Domain-Detection\models\Malicious_URL_Prediction.h5"

# input url
url = ""

# returns probability of url being malicious
prediction = get_prediction(url,model_path)
print(prediction)

