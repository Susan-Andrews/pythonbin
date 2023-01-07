import pickle
py_dict = { 'name': 'harry', 'salary':9000, 'language': 'Hindi' }
myfile = open('filename.txt','wb')
pickle.dump(py_dict,myfile)
myfile.close()

myfile = open('filename.txt','rb')
py_dict = pickle.load(myfile)
myfile.close()