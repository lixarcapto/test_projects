


from data_access.app.person.PersonKeysData import PersonKeysData

class RacesByCulturesData:

    def __init__(self):
        self.PersonKeysData = PersonKeysData()
        self.RACES_BY_CULTURE_ARRAY = [
          [#spanish 0
              self.PersonKeysData.RACE.MEDITERRANEAN,
              self.PersonKeysData.RACE.ARAB,
              self.PersonKeysData.RACE.CELTIC
          ],
          [#english 1
              self.PersonKeysData.RACE.CELTIC,
              self.PersonKeysData.RACE.NORDIC,
              self.PersonKeysData.RACE.GERMANIC,
              self.PersonKeysData.RACE.MEDITERRANEAN
          ],
          [#aleman 2
              self.PersonKeysData.RACE.NORDIC,
              self.PersonKeysData.RACE.GERMANIC,
              self.PersonKeysData.RACE.SLAVS
          ],
          [#italianos 3
              self.PersonKeysData.RACE.MEDITERRANEAN,
              self.PersonKeysData.RACE.GERMANIC
          ],
          [#nordicos 4
              self.PersonKeysData.RACE.NORDIC
          ],
          [#arabes 5
              self.PersonKeysData.RACE.ARAB,
              self.PersonKeysData.RACE.TURKISH
          ],
          [#bereberes 6
              self.PersonKeysData.RACE.ARAB,
              self.PersonKeysData.RACE.SAHELINE,
              self.PersonKeysData.RACE.SUBSAHARAN,
              self.PersonKeysData.RACE.MEDITERRANEAN
          ],
          [#nguni 7
              self.PersonKeysData.RACE.SUBSAHARAN
          ],
          [#americanos 8
              self.PersonKeysData.RACE.GERMANIC,
              self.PersonKeysData.RACE.CELTIC,
              self.PersonKeysData.RACE.INDOAMERICAN,
              self.PersonKeysData.RACE.NORDIC,
              self.PersonKeysData.RACE.MEDITERRANEAN,
              self.PersonKeysData.RACE.ASIAN
          ],
          [#astecas 9
              self.PersonKeysData.RACE.INDOAMERICAN
          ],
          [#incas 10
              self.PersonKeysData.RACE.INDOAMERICAN
          ],
          [#chinos 11
              self.PersonKeysData.RACE.ASIAN,
              self.PersonKeysData.RACE.MONGOLIAN
          ],
          [#japoneses 12
              self.PersonKeysData.RACE.ASIAN
          ],
          [#koreanos 13
              self.PersonKeysData.RACE.ASIAN
          ],
          [#hindi 14
              self.PersonKeysData.RACE.INDIAN,
              self.PersonKeysData.RACE.ARAB,
              self.PersonKeysData.RACE.ASIAN
          ],
          [#polinesios 15
              self.PersonKeysData.RACE.POLYNESIAN
          ],
          [#frances 16
              self.PersonKeysData.RACE.CELTIC,
              self.PersonKeysData.RACE.GERMANIC
          ],
          [#mongoles 17
              self.PersonKeysData.RACE.MONGOLIAN,
              self.PersonKeysData.RACE.TURKISH
          ],
          [#rusos 18
              self.PersonKeysData.RACE.TURKISH,
              self.PersonKeysData.RACE.SLAVS,
              self.PersonKeysData.RACE.NORDIC,
              self.PersonKeysData.RACE.ASIAN
          ],
          [#afrikaners 19
              self.PersonKeysData.RACE.SUBSAHARAN,
              self.PersonKeysData.RACE.GERMANIC,
              self.PersonKeysData.RACE.CELTIC
          ]
        ]
