<template>
  <v-img class="white--text"
    src="/assets/img/blurcamera.jpg"
    :aspect-ratio="16/9"
    gradient="to top right, rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2)"
    >
    <slot>
      <v-container class="container-xl">
        <v-row justify="center">
          <v-col sm="11" md="9" cols="12">
            <h1 class="mb-4 display-3 text-uppercase font-weight-bold text-bgshadow"> Hi, I'm Michael George</h1>
            <div class="mb-4 display-2 font-weight-light text-bgshadow"> 我是一名软件工程师</div>
            <!-- <div class="mb-4 text-bgshadow">Vivamus elementum semper nisi. Maecenas malesuada. Donec sodales sagittis magna. Proin faucibus arcu quis ante. Vivamus quis mi.</div> -->
          </v-col>
        </v-row>
      </v-container>
    </slot>
  </v-img>
</template>
