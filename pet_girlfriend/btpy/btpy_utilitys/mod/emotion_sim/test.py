

from EmotionSim import EmotionSim

def main():
    emotion_sim = EmotionSim()
    for i in range(6):
        emotion_sim.sum_emotion("anger", 5)
        print(emotion_sim.get_emotion())
        emotion_sim.update()
    print(emotion_sim.write())
    sum_emotion_test()
    sum_boredom_test()

def sum_boredom_test():
    print("sum_boredom_test")
    #
    emotion_sim = EmotionSim()
    emotion_sim.sum_emotion(
        emotion_sim.EMOTION.ANGER, 5)
    emotion_sim.sum_emotion(
        emotion_sim.EMOTION.FEAR, 4)
    emotion_sim.sum_emotion(
        emotion_sim.EMOTION.JOY, 3)
    emotion_sim.sum_emotion("boredom", 3)
    anger = emotion_sim.get_emotion_value(
        "anger")
    print(anger == 3)


def sum_emotion_test():
    print("sum_emotion_test")
    # prueba si puede sumar una emocion
    # correctamente
    emotion_sim = EmotionSim()
    for i in range(10):
        emotion_sim.sum_emotion(
        emotion_sim.EMOTION.ANGER, 1)
    r = emotion_sim.get_emotion_value("anger")
    print(r == 10)
    # prueba si puede sumar dos emociones
    # correctamente
    emotion_sim = EmotionSim()
    for i in range(5):
        emotion_sim.sum_emotion(
        emotion_sim.EMOTION.ANGER, 1)
    for i in range(5):
        emotion_sim.sum_emotion(
        emotion_sim.EMOTION.FEAR, 1)
    anger = emotion_sim.get_emotion_value(
        "anger")
    fear = emotion_sim.get_emotion_value(
        "fear")
    print(anger == fear)
    # prueba si puede sumar una emocion
    # sin llegar al limite
    emotion_sim = EmotionSim()
    for i in range(15):
        emotion_sim.sum_emotion(
        emotion_sim.EMOTION.ANGER, 1)
    r = emotion_sim.get_emotion_value("anger")
    print(r == 10)



main()