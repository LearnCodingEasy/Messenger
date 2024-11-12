import comp from "F:/Messenger/messenger_vuepress/docs/.vuepress/.temp/pages/index.html.vue"
const data = JSON.parse("{\"path\":\"/\",\"title\":\"Messenger\",\"lang\":\"en-US\",\"frontmatter\":{},\"headers\":[{\"level\":2,\"title\":\"Github\",\"slug\":\"github\",\"link\":\"#github\",\"children\":[]},{\"level\":2,\"title\":\"LICENSE\",\"slug\":\"license\",\"link\":\"#license\",\"children\":[]},{\"level\":2,\"title\":\"Vite Press\",\"slug\":\"vite-press\",\"link\":\"#vite-press\",\"children\":[]}],\"git\":{\"updatedTime\":1731401638000,\"contributors\":[{\"name\":\"Hossam Rashad\",\"email\":\"learncodingeasy@yahoo.com\",\"commits\":1,\"url\":\"https://github.com/Hossam Rashad\"}]},\"filePathRelative\":\"index.md\"}")
export { comp, data }

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept()
  if (__VUE_HMR_RUNTIME__.updatePageData) {
    __VUE_HMR_RUNTIME__.updatePageData(data)
  }
}

if (import.meta.hot) {
  import.meta.hot.accept(({ data }) => {
    __VUE_HMR_RUNTIME__.updatePageData(data)
  })
}
