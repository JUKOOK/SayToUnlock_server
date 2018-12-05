# JuKook Kim - SayTounlock PyAudio Server : socket networking
# Command Line use : python audioAnalysis.py trainClassifier -i <directory1> ... <directoryN> --method 
#                   <svm, svm_rbf, knn, extratrees, gradientboosting or randomforest> -o <modelName> --beat

# python audioAnalysis.py trainClassifier -i classifierData/speech/ classifierData/music/ --method svm -o data/svmSM
# python audioAnalysis.py trainClassifier -i classifierData/speech/ classifierData/music/ --method knn -o data/knnSM


import os
import socket
import sys
from pyaudio.pyAudioAnalysis import audioTrainTest as aT
 
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print 'socket created'

# HOST = "10.64.148.71"
#HOST = "192.168.0.3"  # JUKOOK_5G
HOST = "192.168.0.37"  # Anthouse_5G
PORT = 8887

#Bind socket to Host and Port
try:
    s.bind((HOST, PORT))
except socket.error as err:
    print 'Bind Failed, Error Code: ' + str(err[0]) + ', Message: ' + err[1]
    sys.exit()
 
print 'Socket Bind Success!'

while 1:
    s.listen(10)
    print 'Socket is now listening'
    
    conn,addr = s.accept()
    print 'Connet with ' + addr[0] + ':' + str(addr[1])

    try:
        f = open("get_test.wav", "wb")
    except:
        print("Can't open file!")

    while 1:
        buf = conn.recv(1024)
        if "end" in buf: break
        if buf: 
            f.write(buf)
        
    if os.path.getsize("get_test.wav") == 0:
        print("Receive error!")
    else:
        print("Receiving Done!")

    import os

    test_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'get_test.wav')
    try:
        [Result, P, classNames] = aT.fileClassification(test_file, "svm_STU_model", "svm")
        print(Result)
        print(P)
        print(str(classNames))
    except:
        print("Can't found get_test.wav!")
        raisef

    try:
        max = P[1]
        for i in P:
            if(max < i):
                max = i

        if(max == P[1]): # Registered Voice
            conn.sendall("success")
            print("success")
        else:
            conn.sendall("fail")
            print("fail")
        print("Send message well!")
    except:
        print("Can't send results")
        raise

    conn.close()

    
 
 
