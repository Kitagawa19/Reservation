import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  css: {
    preprocessorOptions: {
      scss: {
        additionalData:
          '@import "/src/../node_modules/wave-ui/src/wave-ui/scss/_variables.scss";'
      }
    }
  },
  plugins: [vue()]
})
