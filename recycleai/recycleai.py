from fastai.vision import *

def recycleai_main(img):
    #classify Image
    img = open_image(BytesIO(img.read()))
    learner = load_learner(Path("/home/elliot/ylambda/recycleai"))
    _,_,losses = learner.predict(img)

    return ({
        "predictions": sorted(
            zip(learner.data.classes, map(float, losses)),
            key=lambda p: p[1],
            reverse=True)})
