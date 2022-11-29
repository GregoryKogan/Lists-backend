// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    modules: [
        '@nuxtjs/color-mode',
        '@nuxtjs/google-fonts',
    ],
    runtimeConfig: {
        public: {
            apiBase: '/api'
        }
    },
    googleFonts: {
        families: {
          'Inter': true,
          Lato: [100, 300],
          Raleway: {
            wght: [100, 400],
            ital: [100]
          },
        }
    },      
})
