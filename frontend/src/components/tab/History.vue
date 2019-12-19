<template>
  <v-row>
    <v-col cols="12" class="py-1 pl-7">历史记录</v-col>
    <v-col cols="12" class="py-1 py-md-2">
      <v-card outlined class="v-card--shadow">
        <v-timeline align-top dense>
          <v-timeline-item color="pink" small>
            <v-layout pt-1>
              <v-flex xs3>
                <strong>5pm</strong>
              </v-flex>
              <v-flex>
                <strong>New Icon</strong>
                <div class="caption">Mobile App</div>
              </v-flex>
            </v-layout>
          </v-timeline-item>

          <v-timeline-item
            color="teal lighten-3"
            small>
            <v-layout wrap pt-1>
              <v-flex xs3>
                <strong>3-4pm</strong>
              </v-flex>
              <v-flex>
                <strong>Design Stand Up</strong>
                <div class="caption mb-2">Hangouts</div>
                <v-avatar>
                  <v-img
                    src="https://avataaars.io/?avatarStyle=Circle&topType=LongHairFrida&accessoriesType=Kurt&hairColor=Red&facialHairType=BeardLight&facialHairColor=BrownDark&clotheType=GraphicShirt&clotheColor=Gray01&graphicType=Skull&eyeType=Wink&eyebrowType=RaisedExcitedNatural&mouthType=Disbelief&skinColor=Brown"
                  ></v-img>
                </v-avatar>
                <v-avatar>

                  <v-img
                    src="https://avataaars.io/?avatarStyle=Circle&topType=ShortHairFrizzle&accessoriesType=Prescription02&hairColor=Black&facialHairType=MoustacheMagnum&facialHairColor=BrownDark&clotheType=BlazerSweater&clotheColor=Black&eyeType=Default&eyebrowType=FlatNatural&mouthType=Default&skinColor=Tanned"
                  ></v-img>
                </v-avatar>
                <v-avatar>
                  <v-img
                    src="https://avataaars.io/?avatarStyle=Circle&topType=LongHairMiaWallace&accessoriesType=Sunglasses&hairColor=BlondeGolden&facialHairType=Blank&clotheType=BlazerSweater&eyeType=Surprised&eyebrowType=RaisedExcited&mouthType=Smile&skinColor=Pale"
                  ></v-img>
                </v-avatar>
              </v-flex>
            </v-layout>
          </v-timeline-item>

          <v-timeline-item color="pink" small>
            <v-layout pt-1>
              <v-flex xs3>
                <strong>12pm</strong>
              </v-flex>
              <v-flex>
                <strong>Lunch break</strong>
              </v-flex>
            </v-layout>
          </v-timeline-item>

          <v-timeline-item color="teal lighten-3" small>
            <v-layout pt-1>
              <v-flex xs3>
                <strong>9-11am</strong>
              </v-flex>
              <v-flex>
                <strong>Finish Home Screen</strong>
                <div class="caption">Web App</div>
              </v-flex>
            </v-layout>
          </v-timeline-item>
        </v-timeline>
      </v-card>
    </v-col>
  </v-row>
</template>