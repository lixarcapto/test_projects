
import Scene as Scene

def main():
    scene = Scene.Scene()
    userInputStr = ""
    text = ""
    scene.startScene()
    while(True):
        text = ""
        scene.advanceGlobalTime()
        userInputStr = input()
        text += " el " + str(scene.day) + " de " + str(scene.month) + " de "
        text += str(scene.year)
        text += scene.regionArray[0].writeRegionData() + " vivia "
        text += scene.regionArray[0].getPerson(0).writeInformation()
        text += scene.regionArray[0].getPerson(0).writeUpdateInformation()
        text += scene.regionArray[0].getPerson(0).writeWhatAreYouDoing()
        print(text)
        if(userInputStr == "f"):
            break
    return

main()
