import cv2;
import time;
import dropbox;
import random;

startTime= time.time()

def takeSnapshot():
    number= random.RandInt(0, 100);
    #inistialising cv2
    videoCaptureObject= cv2.VideoCapture(0);
    result= True;
    while(result):
        #read the frames while the camera is on
        ret, frame= videoCaptureObject.read();

        imageName= "img" + str(number) + ".png";

        #cv2.imWrite method is used to save an image to any storage device
        cv2.imwrite(imageName, frame);
        result= False;

    return imageName;
    print("Snapshot Taken");

    # releases the camera and closes all the windows that might be opened while this process
    videoCaptureObject.release();
    cv2.destroyAllWindows();

def uploadPics(imageName):
    accessToken= 'sl.BJ8zW52uvwcZ9m0hq9dLteFxXfpKd5_pTmUlv8A7MxUwvl06WK-MtKyxTY3ptSyBjmQsa8keqODJakXeWyUIiTYWamvaQfnBnAs8fPU24QLQdLAaJ5z8pTCaC5cJpLVX1pdQ4AbmY5c';
    file= imageName;
    file_from= file;
    file_to= "/NewFolder1/" + (imageName);

    dbx= dropbox.Dropbox(accessToken);
    with open(file_from, "rb") as f:
        dbx.files_upload(f.read(), file_to, mode= dropbox.files.WriteMode.overwrite);
        print("File Uploaded");

def main():
    while(True):
        if((time.time()- startTime)>= 10):
            name= takeSnapshot();
            uploadPics(name);

main();