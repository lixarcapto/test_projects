





class TabMap:

    def __init__(self):
        tabMap = dict()
        #VEGETALS
        tabMap["0"] = [
            "juncus-bunch",#151
            "wicker-bunch",#152
            "trunk-bunch",#153
            "flax-bunch",#154
            "wheat-grain-bag",#155
            "marigold-grain-bag",#156
            "millet-grain-bag",#157
            "corn-grain-bag",#158
            "mint-bag",#159
            "truffle-bag",#160
            "berries-bag",#161
            "flowr-bag",#162
            "straw-bunch",#163
            "flax-grain-bag"#164
        ]
        #DERIVATIVES VEGETABLES
        tabMap["1"] = [
            "flour-bag",#200
            "board-bunch",#201
            "bran-bag",#202 cascara
            "semolina-bag",#203
            "flake-bag",#204
            "vegetable-oil-vessel",#205
            "poor-flour-bag",#207
            "yeast-vessel"#208
        ]
        #ANIMALS
        tabMap["2"] = [
            "cow",#251
            "chicken",#252
            "horse",#253
            "pig",#254
            "turkey",#255
            "duck",#256
            "donkey",#257
            "sheep",#258
            "goat",#259
            "dog",#260
            "cat",#261
            "rabbit",#262
            "dove"#263
        ]
        #DERIVATIVES ANIMALS
        tabMap["3"] = [
            "wool-bag",#300
            "raw-skin-bag",#301
            "leather-bag",#302
            "fur-bag",#303
            "shellfish-fiber-bag",#304
            "suede-leather-bag",#305
            "chicken-meat-bag",#306
            "cow-meat-bag",#307
            "poor-meat-bag",#308
            "premium-meat",#309
            "pig-meat-bag",#310
            "wild-meat-bag",#311
            "exotic-meat-bag",#312
            "duck-meat-bag",#313
            "turkey-meat-bag",#314
            "goat-meat-bag",#315
            "rabbit-meat-bag",#316
            "bacon-bag",#317
            "foie-gras-bag",#318
            "gut-bag",#319
            "genitals-bag",#320
            "gizzard-bag",#321
            "liver-bag",#322
            "belly-bag",#323
        ]
        #FINAL PRODUCTS
        tabMap["4"] = [
             "water-vessel",#351
             "fancy-clothes",#352
             "cheap-clothes",#353
             "common-clothes",#354
             "sturdy-clothes",#355
             "winter-clothes",#356
             "formal-clothes"#357
        ]
        #MIDDLE PRODUCTS
        tabMap["5"] = [
            "bag",#450
            "box",#451
            "vessel",#452
            "rope",#453
            "furniture",#454
            "tool",#455
            "machine",#456
            "linen-fabric",#457
            "woolen-fabric",#458
            "silk-fabric",#459
            "cotton-fabric",#460
            "nylon",#461
            "felt-fabric",#462
            "polyester-fabric",#463
            "cane-fabric",#464
            "sea-silk-fabric",#465
            "gold-fabric",#466
            "gold-yarn",#467
            "polyester-yarn",#468
            "cotton-yarn",#469
            "ceramic-brick",#470
            "adobe-brick"#471
        ]
        #MINERALS
        tabMap["6"] = [
            "sand-bag",#600
            "stone-brick-box",#601
            "gravel-bag",#602
            "sweet-water-vessel",#603
            "salt-bag",#604
            "ground-bag",#605
            "limestone-brick-box",#606
            "peat-bag",#607
            "clay-bag",#608
            "humus-bag",#609
            "ash-bag",#610
            "diamonds-bag",#611
            "gems-bag",#612
            "quartz-bag",#613
            "lime-bag",#614
            "lanthanides-bag",#615
            "coal-bag",#616
            "marble-brick-box",#617
            "graphite-bag",#618
            "graphene-bag",#619
            "semi-precious-stones-bag",#620
            "coke-bag",#621
            "black-sand-bag"#622
        ]
        #ORES
        tabMap["7"] = [
            "hematite-bag",#0 hierro
            "pyrite-bag",#1 acido sulfurico
            "sphalerite-bag",#2 zinc + cadmio + rare metals
            "electro-bag",#3 oro 2 + plata 1
            "gold-nuggets-bag",#4
            "chalcopyrite-bag",#5 cobre 2 + 1 hierro
            "cinnabar-bag",#6 mercurio
            "coltan-bag",#7 lanthanides
            "cassiterite-bag",#8 estaño
            "stibinite-bag",#9 antimony
            "galena-bag",#10 lead
            "zirconia-bag",#11 zirconium and hafnium
            "pyrolusite-bag"#12 Manganese
        ]
        #METALS
        tabMap["8"] = [
            "silver-ingot-box",#51
            "gold-ingot-box",#52
            "copper-ingot-box",#53
            "tin-ingot-box",#54
            "quicksilver-vessel",#55
            "iron-ingot-box",#56
            "titanium-ingot-box",#57
            "brass-ingot-box",#58
            "bronze-ingot-box",#59
            "platinum-ingot-box",#60
            "nickel-ingot-box",#61
            "lead-ingot-box",#62
            "chrome-ingot-box",#63
            "cobalt-ingot-box",#64
            "manganese-ingot-box",#65
            "molybdenum-ingot-box",#66
            "aluminum-ingot-box",#67
            "magnesium-ingot-box",#68
            "cadmium-ingot-box",#69
            "antimony-ingot-box",#70
            "zirconium-ingot-box",#71
            "hafnium-ingot-box",#72
            "manganese-ingot-box",#73
            "welding-bag",#74
            "stainless-steel-ingot-box"#75
        ]
        #CHEMICAL
        tabMap["9"] = [
            "sulfuric-acid-vessel",#100
            "rubber-vessel",#101
            "carbon-fiber-bag",#102
            "cyanide-vessel"#103
        ]
        tabMap["10"] = [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        tabMap["11"] = [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        self.inner = tabMap
