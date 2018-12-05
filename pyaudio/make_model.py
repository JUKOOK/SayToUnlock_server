from pyAudioAnalysis import audioTrainTest as aT
aT.featureAndTrain(["/Users/kimjukook/SayToUnlock_server/pyaudio/Gyungmin_wav/", 
"/Users/kimjukook/SayToUnlock_server/pyaudio/Jukook/", 
"/Users/kimjukook/SayToUnlock_server/pyaudio/HH/",
"/Users/kimjukook/SayToUnlock_server/pyaudio/SH/"], 
1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svm_STU_model", True)



