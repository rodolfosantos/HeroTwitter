import gopro
import twitter


if __name__ == '__main__':
    takenPhotoName = gopro.takePhotoAndDownload()
    print twitter.tweet("Test", takenPhotoName)
    print takenPhotoName
