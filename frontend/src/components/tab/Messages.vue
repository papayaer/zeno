<template>
  <v-row>
    <v-col cols="12" class="py-1 pl-7">消息</v-col>
    <v-col cols="12" class="py-1 py-md-2">
      <v-card outlined class="v-card--shadow">
        <v-card-text class="py-0">
          <v-timeline dense>
            <v-slide-x-reverse-transition
              group
              hide-on-leave
            >
              <v-timeline-item
                v-for="item in items"
                :key="item.id"
                :color="item.color"
                small
                fill-dot
              >
                <v-alert
                  :value="true"
                  :color="item.color"
                  :icon="item.icon"
                  class="white--text"
                >
                  Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod convenire principes at. Est et nobis iisque percipit, an vim zril disputando voluptatibus, vix an salutandi sententiae.
                </v-alert>
              </v-timeline-item>
            </v-slide-x-reverse-transition>
          </v-timeline>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>


<script>
  const COLORS = [
    'info',
    'warning',
    'error',
    'success',
  ]
  const ICONS = {
    info: 'mdi-information',
    warning: 'mdi-alert',
    error: 'mdi-alert-circle',
    success: 'mdi-check-circle',
  }

  export default {
    data: () => ({
      interval: null,
      items: [
        {
          id: 1,
          color: 'info',
          icon: ICONS['info'],
        },
      ],
      nonce: 2,
    }),

    beforeDestroy () {
      this.stop()
    },

    methods: {
      addEvent () {
        let { color, icon } = this.genAlert()

        const previousColor = this.items[0].color

        while (previousColor === color) {
          color = this.genColor()
        }

        this.items.unshift({
          id: this.nonce++,
          color,
          icon,
        })

        if (this.nonce > 6) {
          this.items.pop()
        }
      },
      genAlert () {
        const color = this.genColor()

        return {
          color,
          icon: this.genIcon(color),
        }
      },
      genColor () {
        return COLORS[Math.floor(Math.random() * 3)]
      },
      genIcon (color) {
        return ICONS[color]
      },
      start () {
        this.interval = setInterval(this.addEvent, 3000)
      },
      stop () {
        clearInterval(this.interval)
        this.interval = null
      },
    },
  }
</script>