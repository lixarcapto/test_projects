



from data_model.core.body.Body import Body

class TestBody:

    def inner(self):
        body = Body()
        body.randomizeTraits(0)
        for i in range(12):
            body.advanceOneDay()
        print(body.writeOrganismAppearance())
        print(body.writeSensations())
