from pyAudioAnalysis import audioTrainTest as aT
[Result, P, classNames] = aT.fileClassification("get_test.wav", "svm_STU_model","svm")
print(Result)
print(P.round(3)*100)
print(classNames)
