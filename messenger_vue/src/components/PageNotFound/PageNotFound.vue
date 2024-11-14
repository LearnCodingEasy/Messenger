<template>
  <div class="PageNotFound">
    <div class="w-full">
      <img
        :src="imageSrc"
        @error="loadFallbackImage"
        alt="Page Not Found"
        class="img-fluid h-screen w-full"
      />
    </div>
  </div>
</template>
<script>
export default {
  name: 'PageNotFound',
  data() {
    return {
      // الرابط الأساسي للصورة من الإنترنت
      imageSrc:
        'https://raw.githubusercontent.com/LearnCodingEasy/Images/refs/heads/main/images/Page_Not_Found/404.jpg',
    }
  },
  methods: {
    loadFallbackImage() {
      // في حالة الخطأ، تغيير الصورة إلى المسار المحلي
      // eslint-disable-next-line no-undef
      this.imageSrc = require('../../Images/Page_Not_Found/404.jpg')
      console.log(`Bad`)
    },
  },
  mounted() {
    document.title = 'Trello | Page Not Found'
  },
}
</script>

<style lang="scss">
.PageNotFound {
  > div {
    height: calc(100vh - 70px);
  }
}
</style>
