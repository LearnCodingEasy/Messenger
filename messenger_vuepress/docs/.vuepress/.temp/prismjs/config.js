import "F:/Messenger/messenger_vuepress/node_modules/@vuepress/highlighter-helper/lib/client/styles/base.css"
import "F:/Messenger/messenger_vuepress/node_modules/@vuepress/plugin-prismjs/lib/client/styles/nord.css"
import "F:/Messenger/messenger_vuepress/node_modules/@vuepress/highlighter-helper/lib/client/styles/line-numbers.css"
import "F:/Messenger/messenger_vuepress/node_modules/@vuepress/highlighter-helper/lib/client/styles/notation-highlight.css"
import "F:/Messenger/messenger_vuepress/node_modules/@vuepress/highlighter-helper/lib/client/styles/collapsed-lines.css"
import { setupCollapsedLines } from "F:/Messenger/messenger_vuepress/node_modules/@vuepress/highlighter-helper/lib/client/composables/collapsedLines.js"

export default {
  setup() {
    setupCollapsedLines()
  }
}