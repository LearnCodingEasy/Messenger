<script setup>
import axios from 'axios'
</script>

<template>
  <main class="" style="position: sticky; top: 0; left: 0">
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
      <!--  -->
      <div class="main-left col-span-1">
        <div class="p-4 bg-white border border-gray-200 rounded-lg">
          <div class="space-y-4">
            <div v-if="conversations.length" class="if_user_have_conversations">
              <div
                class="flex items-center justify-between my-2 wrapper_control_conversation cursor-pointer"
                v-for="conversation in conversations"
                v-bind:key="conversation.id"
                v-on:click="setActiveConversation(conversation.id)"
              >
                <div class="flex items-center space-x-2">
                  <template v-for="user in conversation.users" :key="user.id">
                    <img
                      v-if="user.id !== userStore.user.id"
                      :src="user.get_avatar"
                      class="h-10 w-10 rounded-full"
                    />

                    <p class="text-xs font-bold" v-if="user.id !== userStore.user.id">
                      {{ user.name }}
                    </p>
                  </template>
                </div>
                <span class="text-xs text-gray-500"
                  >{{ conversation.modified_at_formatted }} ago</span
                >
              </div>
            </div>
            <!-- <div> -->
            <div v-else>
              <div v-for="friend in friends" :key="friend.id">
                <div @click="sendDirectMessage" class="flex items-center justify-between">
                  <div class="friend_image">
                    <img :src="friend.get_avatar" class="w-12 h-12 rounded-full" />
                  </div>
                  <div>{{ friend.name }}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!--  -->
      <div class="main-center col-span-3 space-y-4 h-dvh overflow-hidden">
        <div class="bg-white border border-gray-200 rounded-lg">
          <div class="flex flex-col flex-grow p-4">
            <template v-for="message in activeConversation.messages" :key="message.id">
              <div
                class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end"
                v-if="message.created_by.id == userStore.user.id"
              >
                <div>
                  <div class="bg-blue-600 text-white p-3 rounded-l-lg rounded-br-lg">
                    <p class="text-sm">{{ message.body }}</p>
                  </div>
                  <span class="text-xs text-gray-500 leading-none"
                    >{{ message.created_at_formatted }} ago</span
                  >
                </div>
                <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                  <img :src="message.created_by.get_avatar" class="w-[40px] rounded-full" />
                </div>
              </div>

              <div class="flex w-full mt-2 space-x-3 max-w-md" v-else>
                <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                  <img :src="message.created_by.get_avatar" class="w-[40px] rounded-full" />
                </div>
                <div>
                  <div class="bg-gray-300 p-3 rounded-r-lg rounded-bl-lg">
                    <p class="text-sm">{{ message.body }}</p>
                  </div>
                  <span class="text-xs text-gray-500 leading-none"
                    >{{ message.created_at_formatted }} ago</span
                  >
                </div>
              </div>
            </template>
          </div>
        </div>
        <!--  -->
        <div class="bg-white border border-gray-200 rounded-lg">
          <form v-on:submit.prevent="submitForm">
            <div class="p-4">
              <textarea
                v-model="body"
                class="p-4 w-full bg-gray-100 rounded-lg"
                placeholder="What do you want to say?"
              ></textarea>
            </div>

            <div class="p-4 border-t border-gray-100 flex justify-between">
              <button
                class="inline-block py-4 px-6 text-white rounded-lg"
                style="background-image: linear-gradient(to right, #5b66f6, #5b66f6)"
              >
                Send
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import { useUserStore } from '@/stores/user'

export default {
  name: 'HomeView',

  setup() {
    const userStore = useUserStore()

    return {
      userStore,
    }
  },

  data() {
    return {
      // All User Of Friends
      friends: [],
      conversations: [],
      activeConversation: {},
      body: '',
    }
  },

  mounted() {
    this.getConversations()
    this.getFriends()

    // 📝 عنوان الصفحة
    document.title = 'Message | Home'
  },

  methods: {
    setActiveConversation(id) {
      console.log('setActiveConversation', id)
      this.activeConversation = id
      this.getMessages()
    },
    getConversations() {
      axios
        .get('/api/chat/')
        .then((response) => {
          console.log('📋 عرض قائمة المحادثات (المسار الرئيسي)')
          console.log('getConversations : ', response.data)
          // // For Test
          let line = '📌'.repeat(30)
          console.log(` %c${line} `, 'color: #1cd07c; font-size: 16px')
          console.log('Conversations List Data : ', response.data)
          this.conversations = response.data

          if (this.conversations.length) {
            this.activeConversation = this.conversations[0].id
            console.log('this.conversations[0].id: ', this.conversations[0].id)
            console.log('this.activeConversation: ', this.activeConversation)
          }

          this.getMessages()
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getMessages() {
      console.log('getMessages')

      axios
        .get(`/api/chat/${this.activeConversation}/`)
        .then((response) => {
          console.log(response.data)

          this.activeConversation = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    // 🧑 Get All Friends
    getFriends() {
      axios
        .get(`/api/friends/${this.userStore.user.id}/`)
        .then((response) => {
          // // For Test
          let line = '📌'.repeat(30)
          console.log(` %c${line} `, 'color: #1cd07c; font-size: 16px')
          console.log('Home Friends Django Data : ', response.data)
          // this.friendshipRequests = response.data.requests
          this.friends = response.data.friends
          // this.user = response.data.user
        })
        .catch((error) => {
          console.log('error', error)
        })
    },
    sendDirectMessage() {
      console.log('sendDirectMessage')
      axios
        .get(`/api/chat/${this.userStore.user.id}/get-or-create/`)
        .then((response) => {
          console.log(`chat response.data`, response.data)

          this.$router.push('/')
        })
        .catch((error) => {
          console.log('error', error)
        })
    },
    submitForm() {
      console.log('submitForm', this.body)

      axios
        .post(`/api/chat/${this.activeConversation.id}/send/`, {
          body: this.body,
        })
        .then((response) => {
          console.log(response.data)
          this.body = ``
          this.activeConversation.messages.push(response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
}
</script>
