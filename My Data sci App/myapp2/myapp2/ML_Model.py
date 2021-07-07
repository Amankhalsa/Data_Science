
def predict_Model(pclass,sex,age,sibsp,parch,fare,embarked,title):
	import pickle
	x = [[pclass,sex,age,sibsp,parch,fare,embarked,title]]
	rf = pickle.load(open('ML_titanic_Model.sav','rb'))
	prediction = rf.predict(x)
	if prediction == 1:
		prediction = 'Survived'
	elif prediction == 0:
		prediction = 'Not Survived'
	return prediction