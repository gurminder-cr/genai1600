import joblib 
model= joblib.load('encoder.pkl')

print(model.transform(['good','bad']))