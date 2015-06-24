import gopro
import twitter

def takePhotoAndUpload(status):
    takenPhotoName = gopro.takePhotoAndDownload()
    return twitter.tweet(status, takenPhotoName)