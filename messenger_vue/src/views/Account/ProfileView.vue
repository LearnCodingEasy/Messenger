<script setup>
// import { RouterLink, RouterView } from 'vue-router'
import axios from 'axios'

// import { ref } from 'vue'
//
import { onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'

const userStore = useUserStore()
userStore.initStore()
const router = useRouter()

onMounted(() => {
  // Perform any necessary operations on component mount
  if (!userStore.user.access) {
    // console.log('User Data: ', userStore.user)
    // Replace '/login' with your actual login route
    router.push('/login')
  } else {
    // Set default Authorization header for axios
    axios.defaults.headers.common['Authorization'] = `Bearer ${userStore.user.access}`
    // console.log('User Data: ', userStore.user)
    // userStore.user = this.formInfo
    // console.log('this.formInfo: ', this.formInfo);
    // console.log('userStore.user: ', userStore.user);
  }
})
</script>

<template>
  <div class="wrapper_profile">
    <div class="container mx-auto">
      <div class="inner_profile px-2">
        <aside class="sidebar_profile flex-none" :class="{ sidebar_open: sidebar_open }">
          <!-- Toggle Aside View -->
          <div class="aside_toggle" @click="toggleSidebarOpen">
            <i class="pi pi-angle-double-right"></i>
          </div>
          <!-- Get User Info -->
          <div
            class="user_image"
            @click="activeTab = '1'"
            :class="[activeTab === '1' ? 'activeView' : '']"
          >
            <div class="user_image_icon">
              <i class="pi pi-user"></i>
            </div>
            <div class="user_name_data">
              <div class="">{{ userStore.user.name }}</div>
              <div class="">{{ userStore.user.surname }}</div>
            </div>
          </div>
          <!-- Password -->
          <div
            class="user_name"
            @click="activeTab = '2'"
            :class="[activeTab === '1' ? 'activeView' : '']"
          >
            <div class="user_name_icon">
              <i class="pi pi-key"></i>
            </div>
            <div class="user_name_data">
              <div class="">******</div>
            </div>
          </div>
          <!-- Get All Friends -->
          <div
            class="user_email"
            @click="activeTab = '3'"
            :class="[activeTab === '1' ? 'activeView' : '']"
          >
            <div class="user_email_icon">
              <fa :icon="['fas', 'users']" class="text-2xl" />
            </div>
            <div class="user_email_data">
              <div class="">Friends All</div>
            </div>
          </div>
          <!-- Friends Suggest -->
          <div
            class="user_Password"
            @click="activeTab = '4'"
            :class="[activeTab === '1' ? 'activeView' : '']"
          >
            <div class="user_Password_icon">
              <fa :icon="['fas', 'user-check']" class="text-2xl" />
            </div>
            <div class="user_Password_data">
              <div class="">Friends Suggest</div>
            </div>
          </div>
          <!-- Requests -->
          <div
            class="user_Password"
            @click="activeTab = '5'"
            :class="[activeTab === '1' ? 'activeView' : '']"
          >
            <div class="user_Password_icon">
              <fa :icon="['fas', 'user-plus']" class="text-2xl" />
            </div>
            <div class="user_Password_data">
              <div class="">Friends Requests</div>
            </div>
          </div>
          <!-- User Tasks -->
          <div
            class="user_Password"
            @click="activeTab = '6'"
            :class="[activeTab === '1' ? 'activeView' : '']"
          >
            <div class="user_Password_icon">
              <fa :icon="['fas', 'thumbtack']" class="text-2xl" />
            </div>
            <div class="user_Password_data">
              <div class="">User Tasks</div>
            </div>
          </div>
        </aside>
        <div class="data_profile flex p-8">
          <!-- User Info -->
          <div class="wrapper_info_data flex justify-between items-center" v-if="activeTab === '1'">
            <div class="wrapper_old_data">
              <div class="inner_old_data flex justify-between items-end">
                <prime_card class="w-96">
                  <template #header>
                    <!-- Owner Image -->
                    <div class="" v-if="userStore.user.id == user.id">
                      <!-- cover -->
                      <div class="image_cover">
                        <img
                          class="w-full h-64"
                          v-if="userStore.user.get_cover !== 'undefined'"
                          :src="userStore.user.get_cover"
                        />
                        <img
                          class="w-full h-64"
                          v-else-if="userStore.user.get_cover == ' '"
                          :src="userStore.user.get_cover"
                        />
                        <img
                          class="w-full h-64"
                          v-else
                          src="../../assets/Images/Page_Not_Found/404.jpg"
                        />
                        <img />
                      </div>
                      <!-- Avatar -->
                      <div
                        class="image_avatar border rounded-full"
                        v-if="userStore.user.id == user.id"
                        style="
                          width: 75px;
                          height: 75px;
                          display: flex;
                          justify-content: center;
                          align-items: center;
                          margin-top: -37px;
                          margin-left: 10px;
                          position: relative;
                        "
                      >
                        <img
                          class="w-full h-full shadow-lg rounded-full"
                          v-if="userStore.user.get_avatar !== 'undefined'"
                          :src="userStore.user.get_avatar"
                        />
                        <img
                          class="w-full h-full shadow-lg rounded-full"
                          v-else-if="userStore.user.get_avatar == ' '"
                          :src="userStore.user.get_avatar"
                        />
                        <img
                          class="w-full h-full shadow-lg rounded-full"
                          v-else
                          src="../../assets/Images/Page_Not_Found/404.jpg"
                        />
                        <prime_badge
                          size="small"
                          :severity="user.is_online ? 'success' : 'danger'"
                          style="position: absolute; bottom: -8px; opacity: 0.8"
                        ></prime_badge>
                      </div>
                    </div>
                    <!-- User Visit Profile User -->
                    <div v-else class="image_avatar">
                      <!-- Cover -->
                      <div class="image_cover">
                        <img class="w-full h-64" :src="user.get_cover" />
                      </div>
                      <!-- Avatar -->
                      <div
                        class="image_avatar border rounded-full"
                        style="
                          width: 75px;
                          height: 75px;
                          display: flex;
                          justify-content: center;
                          align-items: center;
                          margin-top: -37px;
                          margin-left: 10px;
                          position: relative;
                        "
                      >
                        <img class="w-full h-full shadow-lg rounded-full" :src="user.get_avatar" />
                        <prime_badge
                          size="small"
                          :severity="user.is_online ? 'success' : 'danger'"
                          style="position: absolute; bottom: -8px; opacity: 0.8"
                        ></prime_badge>
                      </div>
                    </div>
                  </template>
                  <template #content>
                    <!-- name -->
                    <div class="">
                      <h3 class="text-2xl font-bold" v-if="userStore.user.id == user.id">
                        {{ formInfo.name }}
                      </h3>
                      <h3 class="text-2xl font-bold" v-else>{{ user.name }}</h3>
                    </div>
                    <!-- Surname -->
                    <div class="">
                      <h3 class="text-1xl font-bold" v-if="userStore.user.id == user.id">
                        {{ formInfo.surname }}
                      </h3>
                      <h3 class="text-1xl font-bold" v-else>
                        {{ user.surname }}
                      </h3>
                    </div>
                    <!-- Email -->
                    <div class="">
                      <small class="text-1xl font-bold" v-if="userStore.user.id == user.id">
                        {{ formInfo.email }}
                      </small>
                      <small class="text-1xl font-bold" v-else>
                        {{ user.email }}
                      </small>
                    </div>
                    <!-- date of birth -->
                    <!-- gender -->
                    <div class="flex justify-between items-center">
                      <!-- date of birth -->
                      <div class="">
                        <h3 class="text-1xl font-bold" v-if="userStore.user.id == user.id">
                          {{ formInfo.date_of_birth }}
                        </h3>
                        <h3 class="text-1xl font-bold" v-else>
                          {{ user.date_of_birth }}
                        </h3>
                      </div>
                      <!-- gender -->
                      <div class="">
                        <h3 class="text-1xl font-bold" v-if="userStore.user.id == user.id">
                          {{ formInfo.gender }}
                        </h3>
                        <h3 class="text-1xl font-bold" v-else>
                          {{ user.gender }}
                        </h3>
                      </div>
                    </div>
                  </template>
                  <template #footer>
                    <!-- Count [Friends , آخر تسجيل دخول ] -->
                    <div class="">
                      <!-- Friends -->
                      <div class="flex justify-between py-1">
                        <div class="">
                          <prime_button
                            type="button"
                            label="Friends"
                            :badge="user.friends_count"
                            badgeSeverity="contrast"
                            outlined
                          />
                        </div>
                        <div class="">
                          <prime_button
                            type="button"
                            label="Tasks"
                            :badge="user.task_count"
                            badgeSeverity="contrast"
                            outlined
                          />
                        </div>
                      </div>
                      <!-- آخر تسجيل دخول -->
                      <div class="flex justify-between py-1">
                        <small> Joining: {{ user.date_joined_formatted }} Ago </small>
                      </div>
                    </div>
                    <!-- اذا كان زائر  -->
                    <div class="">
                      <div class="flex justify-between border-b-2 py-2">
                        <!-- ارسال طلب صداقة -->
                        <button
                          @click="sendFriendshipRequest"
                          class="btn btn-primary Add_friend"
                          v-if="can_send_friendship_request"
                        >
                          <span class="icon">
                            <fa :icon="['fas', 'plus']"></fa>
                          </span>
                          <span class="text"> Add Friend</span>
                        </button>
                        <div v-else>
                          <button
                            class="btn btn-primary Add_friend"
                            v-if="userStore.user.id != user.id"
                          >
                            <span class="icon">
                              <fa :icon="['fas', 'user']"></fa>
                            </span>
                            <span class="text"> Friend</span>
                          </button>
                        </div>
                        <!-- ارسال رساله -->
                        <button class="btn-primary message_friend" @click="sendDirectMessage">
                          <span class="icon">
                            <fa :icon="['fab', 'facebook-messenger']"></fa>
                          </span>
                          <span class="text"> Message</span>
                        </button>
                      </div>
                    </div>
                  </template>
                </prime_card>
              </div>
            </div>
            <!-- Is Owner -->
            <div class="wrapper_new_data md:ml-8" v-if="userStore.user.id == user.id">
              <form class="space-y-4" v-on:submit.prevent="formEditProfileInfo">
                <!-- Avatar -->
                <!-- Cover -->
                <div class="flex justify-between items-center">
                  <div class="new_data">
                    <label>Avatar</label><br />
                    <input type="file" class="form-control" ref="fileAvatar" />
                  </div>
                  <div class="new_data">
                    <label>Cover</label><br />
                    <input type="file" class="form-control" ref="fileCover" />
                  </div>
                </div>
                <!-- Name -->
                <div class="new_data">
                  <label>Name</label><br />
                  <input
                    type="text"
                    v-model="formInfo.name"
                    placeholder="Your full name"
                    class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
                  />
                </div>
                <!-- Surname -->
                <div class="new_data">
                  <label>Surname</label><br />
                  <input
                    type="text"
                    v-model="formInfo.surname"
                    placeholder="Your full Surname"
                    class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
                  />
                </div>
                <!-- Email -->
                <div class="new_data">
                  <label>E-mail</label><br />
                  <input
                    type="email"
                    v-model="formInfo.email"
                    placeholder="Your e-mail address"
                    class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
                  />
                </div>
                <!-- Date of birth -->
                <div class="col-span-full">Date of birth</div>
                <div class="col-span-full">
                  <div class="flex flex-col md:flex-row gap-2">
                    <!-- Day -->
                    <prime_input_group>
                      <prime_date_picker v-model="day" view="day" dateFormat="dd" />
                    </prime_input_group>
                    <!-- Month -->
                    <prime_input_group>
                      <prime_date_picker v-model="month" view="month" dateFormat="mm" />
                    </prime_input_group>
                    <!-- Year -->
                    <prime_input_group>
                      <prime_date_picker v-model="year" view="year" dateFormat="yy" />
                    </prime_input_group>
                  </div>
                </div>
                <!-- Gender -->
                <div class="col-span-full">Gender</div>
                <div class="flex flex-col md:flex-row gap-2">
                  <prime_input_group>
                    <prime_radio_button
                      v-model="formInfo.gender"
                      inputId="ingredient1"
                      name="gender"
                      value="Female"
                    />
                    <label for="ingredient1" class="ml-2"> Female </label>
                  </prime_input_group>
                  <prime_input_group>
                    <prime_radio_button
                      v-model="formInfo.gender"
                      inputId="ingredient2"
                      name="gender"
                      value="Male"
                    />
                    <label for="ingredient2" class="ml-2"> Male </label>
                  </prime_input_group>
                  <prime_input_group>
                    <prime_radio_button
                      v-model="formInfo.gender"
                      inputId="ingredient3"
                      name="gender"
                      value="Custom"
                    />
                    <label for="ingredient3" class="ml-2"> Custom </label>
                  </prime_input_group>
                </div>
                <div>
                  <button
                    class="py-4 px-6 bg-blue-400 text-white rounded-lg"
                    v-on:click.prevent="formEditProfileInfo"
                  >
                    Save changes
                  </button>
                </div>
              </form>
            </div>
          </div>
          <!-- wrapper_password_data -->
          <div
            class="wrapper_password_data flex justify-between items-center"
            v-if="activeTab === '2'"
          >
            <div class="wrapper_old_data">
              <div class="inner_old_data flex justify-between items-end">
                <prime_card class="w-96">
                  <template #header>
                    <img
                      v-if="userStore.user.get_avatar != 'undefined'"
                      :src="userStore.user.get_avatar"
                    />
                    <img v-else src="../../assets/Images/Page_Not_Found/404.jpg" />
                    <img />
                  </template>
                  <template #content>
                    <h3 class="text-2xl font-bold">
                      {{ userStore.user.name }}
                    </h3>
                    <h3 class="text-1xl font-bold">
                      {{ userStore.user.surname }}
                    </h3>
                  </template>
                  <template #body>
                    <div class="">{{ userStore.user.email }}</div>
                  </template>
                  <template #footer>{{ userStore.user.email }}</template>
                </prime_card>
              </div>
            </div>
            <div class="wrapper_new_data ml-8" v-if="userStore.user.id == user.id">
              <form class="space-y-6" v-on:submit.prevent="submitForm">
                <div class="new_data">
                  <label>Old password</label><br />
                  <input
                    type="password"
                    v-model="formPassword.old_password"
                    placeholder="Your old password"
                    class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
                  />
                </div>

                <div class="new_data">
                  <label>New password</label><br />
                  <input
                    type="password"
                    v-model="formPassword.new_password1"
                    placeholder="Your new password"
                    class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
                  />
                </div>

                <div class="new_data">
                  <label>Repeat password</label><br />
                  <input
                    type="password"
                    v-model="formPassword.new_password2"
                    placeholder="Repeat password"
                    class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
                  />
                </div>
                <div>
                  <button class="py-4 px-6 bg-blue-400 text-white rounded-lg">Save changes</button>
                </div>
              </form>
            </div>
          </div>
          <!-- All Friends -->
          <div class="w-full" v-if="activeTab === '3'">
            <div class="main-center col-span-2 space-y-4">
              <div class="flex justify-between items-center mb-6">
                <h3 class="text-xl">Your Friends</h3>
                <prime_button
                  type="button"
                  label="All Friends"
                  icon="pi pi-user-plus"
                  :badge="friends.length"
                  badgeSeverity="contrast"
                  outlined
                />
              </div>
              <div class="rounded-lg grid grid-cols-3 gap-4" v-if="friends.length">
                <div
                  class="p-4 text-center border shadow-xl rounded-lg"
                  v-for="user in friends"
                  v-bind:key="user.id"
                >
                  <img :src="user.get_avatar" class="mb-6 rounded-full h-32 w-32 m-auto" />
                  <p>
                    <strong @click="activeTab = '1'">
                      <RouterLink :to="{ name: 'profile', params: { id: user.id } }">{{
                        user.name
                      }}</RouterLink>
                    </strong>
                  </p>
                  <div class="mt-6 flex space-x-8 justify-around">
                    <p class="text-xs text-gray-500">{{ user.friends_count }} friends</p>
                    <p class="text-xs text-gray-500">{{ user.task_count }} Tasks</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- Friends Suggest  -->
          <div class="w-full" v-if="activeTab === '4'">
            <div class="flex justify-between items-center mb-6">
              <h3 class="text-xl">People You May Know</h3>
              <prime_button
                type="button"
                label="Friendship Suggest"
                icon="pi pi-user-plus"
                :badge="friendsSuggest.length"
                badgeSeverity="contrast"
                outlined
              />
            </div>
            <div class="rounded-lg grid grid-cols-3 gap-4 mt-3">
              <div
                class="text-center border shadow-xl rounded-lg p-4"
                v-for="friendSuggest in friendsSuggest"
                v-bind:key="friendSuggest.id"
              >
                <div class="mb-2">
                  <img :src="friendSuggest.get_avatar" class="mb-2 rounded-full h-32 w-32 m-auto" />
                  <p class="text-xs">
                    <strong>{{ friendSuggest.name }}</strong>
                    <br />
                    <small>{{ friendSuggest.email }}</small>
                  </p>
                </div>
                <RouterLink
                  @click="activeTab = '1'"
                  :to="{ name: 'profile', params: { id: friendSuggest.id } }"
                  class="py-2 px-3 bg-blue-400 text-white text-xs rounded-lg"
                  >Show</RouterLink
                >
              </div>
            </div>
          </div>
          <!--  Friendship Requests -->
          <div class="w-full" v-if="activeTab === '5'">
            <div class="w-full" v-if="friendshipRequests.length">
              <div class="flex justify-between items-center mb-6">
                <h3 class="text-xl">Friendship Requests</h3>
                <prime_button
                  type="button"
                  label="Friendship requests"
                  icon="pi pi-user-plus"
                  :badge="friendshipRequests.length"
                  badgeSeverity="contrast"
                  outlined
                />
              </div>
              <div class="rounded-lg grid grid-cols-3 gap-4 mt-3">
                <div
                  class="text-center border shadow-xl rounded-lg p-4"
                  v-for="friendshipRequest in friendshipRequests"
                  v-bind:key="friendshipRequest.id"
                >
                  <img
                    :src="friendshipRequest.created_by.get_avatar"
                    class="mb-6 rounded-full h-32 w-32 m-auto"
                  />
                  <p @click="activeTab = '1'">
                    <strong>
                      <RouterLink
                        :to="{
                          name: 'profile',
                          params: { id: friendshipRequest.created_by.id },
                        }"
                        >{{ friendshipRequest.created_by.name }}</RouterLink
                      >
                    </strong>
                  </p>

                  <div class="mt-6 flex space-x-8 justify-around">
                    <p class="text-xs text-gray-500">
                      {{ friendshipRequest.created_by.friends_count }} Friends
                    </p>
                    <p class="text-xs text-gray-500">
                      {{ friendshipRequest.created_by.posts_count }} Tasks
                    </p>
                  </div>

                  <div class="mt-4 flex justify-between">
                    <button
                      class="inline-block py-2 px-4 bg-blue-400 text-white rounded-lg"
                      @click="handleRequest('accepted', friendshipRequest.created_by.id)"
                    >
                      Accept
                    </button>
                    <button
                      class="inline-block py-2 px-4 bg-red-600 text-white rounded-lg"
                      @click="handleRequest('rejected', friendshipRequest.created_by.id)"
                    >
                      Reject
                    </button>
                  </div>
                </div>
              </div>
            </div>
            <div class="" v-else>
              <div class="flex justify-between items-center mb-6">
                <h3 class="text-xl">No Friendship Requests</h3>
                <prime_button
                  type="button"
                  label="Friendship requests"
                  icon="pi pi-user-plus"
                  :badge="friendshipRequests.length"
                  badgeSeverity="contrast"
                  outlined
                />
              </div>
            </div>
          </div>
          <!-- Get All Of User Tasks -->
          <div class="w-full" v-if="activeTab === '6'">
            <div class="flex justify-between items-center mb-6">
              <h3 class="text-xl uppercase">Your Tasks</h3>
              <prime_button
                type="button"
                label="All Tasks"
                icon="pi pi-user-plus"
                :badge="friendsSuggest.length"
                badgeSeverity="contrast"
                outlined
              />
            </div>
            hi
            <div
              class="text-center border shadow-xl rounded-lg p-4"
              v-for="friendshipRequest in friendshipRequests"
              v-bind:key="friendshipRequest.id"
            >
              {{ friendshipRequest.id }}
              {{ friendshipRequest.status }}
              <div v-if="friendshipRequest.status === 'not sent'">
                <p>Request not sent yet.</p>
                <button @click="handleRequest('sent', friendshipRequest.created_by.id)">
                  Send Request
                </button>
              </div>
              <div v-else-if="friendshipRequest.status === 'waiting'">
                <p>Waiting for a response...</p>
                <button @click="handleRequest('cancel', friendshipRequest.created_by.id)">
                  Cancel Request
                </button>
              </div>
              <div v-else-if="friendshipRequest.status === 'accepted'">
                <p>Request accepted!</p>
              </div>
              <div v-else-if="friendshipRequest.status === 'rejected'">
                <p>Request rejected.</p>
              </div>
              <div v-else-if="friendshipRequest.status === 'cancel'">
                <p>Request cancelled.</p>
              </div>
            </div>
          </div>
          <!-- User Tasks -->
          <template v-if="errorsFormInfo.length > 0">
            <div class="bg-red-300 text-white rounded-lg p-6">
              <p v-for="error in errorsFormInfo" v-bind:key="error">
                {{ error }}
              </p>
            </div>
          </template>
          <template v-if="errorsFormPassword.length > 0">
            <div class="bg-red-300 text-white rounded-lg p-6">
              <p v-for="error in errorsFormPassword" v-bind:key="error">
                {{ error }}
              </p>
            </div>
          </template>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
// import { useUserStore } from '@/stores/user'
// const userStoreScript = useUserStore()
// استيراد مكتبة Moment.js
// import moment from 'moment'

export default {
  name: 'profileView',
  setup() {
    return {}
  },
  beforeCreate() {},
  data() {
    return {
      // 🧑 User Info
      user: {
        id: '',
      },
      can_send_friendship_request: null,
      //
      friends: [],
      friendshipRequests: [],
      //
      friendsSuggest: [],
      // Layer
      sidebar_open: false,
      activeTab: `1`,
      // Form Info
      formInfo: {
        name: ``,
        surname: ``,
        email: ``,
        date_of_birth: ``,
        gender: ``,
      },
      day: '',
      month: '',
      year: '',
      errorsFormInfo: [],
      // Form Password
      formPassword: {
        old_password: '',
        new_password1: '',
        new_password2: '',
      },
      errorsFormPassword: [],
      //
    }
  },
  watch: {
    '$route.params.id': {
      handler: function () {
        this.getProfile()
      },
      deep: true,
      immediate: true,
    },
  },
  mounted() {
    document.title = 'Trello | Profile'
    this.getProfile()
    this.getFriends()
    this.getFriendSuggestions()
    // التأكد من أن بيانات المستخدم موجودة قبل محاولة الوصول إليها
    // عند تسجيل الدخول localStorage تحميل البيانات من
    const userStore = useUserStore()
    // For Test
    // let line = '📌'.repeat(30)
    // console.log(` %c${line} `, 'color: #1cd07c; font-size: 16px')
    // console.log('User Store [localStorage] Mounted 💻: ', userStore.user)
    if (userStore.user) {
      this.formInfo.name = userStore.user.name
      this.formInfo.surname = userStore.user.surname
      this.formInfo.email = userStore.user.email
      // this.formInfo.date_of_birth = userStore.user.date_of_birth
      let daySlice = userStore.user.date_of_birth.slice(8, 11)
      this.day = daySlice
      let dayMonth = userStore.user.date_of_birth.slice(5, 7)
      this.month = dayMonth
      let dayYear = userStore.user.date_of_birth.slice(0, 4)
      this.year = dayYear

      this.formInfo.gender = userStore.user.gender
    }
  },

  methods: {
    // 👇 Toggle Aside View
    toggleSidebarOpen() {
      this.sidebar_open = !this.sidebar_open
    },
    // ____________________________________________
    // ____________________________________________
    // ____________________________________________
    // 🧑 User Info
    // ____________________________________________
    // ____________________________________________
    // ____________________________________________
    // 🧑 Get Profile Info By Id
    getProfile() {
      const userStore = useUserStore()

      axios
        .get(`/api/profile/${this.$route.params.id}/`)
        .then((response) => {
          this.user = response.data.user
          this.can_send_friendship_request = response.data.can_send_friendship_request
          // For Test
          let line = '📌'.repeat(30)
          console.log(` %c${line} `, 'color: #1cd07c; font-size: 16px')
          console.log('Profile Django Data Of User: ', response.data)
          if (response.data.user.id == userStore.user.id) {
            this.can_send_friendship_request = false
          }
        })
        .catch((error) => {
          console.error('error', error)
          this.$toast.add({
            severity: 'error',
            summary: `Error 🧑 Get Profile Info By Id `,
            detail: `${error.message}`,
            life: 3000,
          })
        })
    },
    // 🙏 Send Friend Ship Request
    sendFriendshipRequest() {
      axios
        .post(`/api/friends/${this.$route.params.id}/request/`)
        .then((response) => {
          console.log('api/friends id request data', response.data)

          this.can_send_friendship_request = false

          if (response.data.message == 'request already sent') {
            this.toast.add({
              severity: 'success',
              summary: `Error Profile`,
              detail: `The request has already been sent!`,
              life: 3000,
            })
          } else {
            this.$toast.add({
              severity: 'error',
              summary: `Error Profile`,
              detail: `The request was sent!`,
              life: 3000,
            })
          }
        })
        .catch((error) => {
          console.log('error', error)
        })
    },
    // 📝 Update User Profile Info
    formEditProfileInfo() {
      this.errorsFormInfo = []
      const userStore = useUserStore()

      if (this.errorsFormInfo.length === 0) {
        // التحقق من وجود بيانات المستخدم في المتجر
        if (userStore && userStore.user) {
          // استخراج اليوم، الشهر، والسنة من كائنات Date وتنسيقها
          const day = this.day
          const month = this.month
          const year = this.year
          const formattedDate = `${year}-${month}-${day}`
          // إعداد البيانات المرسلة مع الطلب
          let formData = new FormData()
          formData.append('avatar', this.$refs.fileAvatar.files[0])
          formData.append('cover', this.$refs.fileCover.files[0])
          formData.append('name', this.formInfo.name)
          formData.append('surname', this.formInfo.surname)
          formData.append('email', this.formInfo.email)
          formData.append('date_of_birth', formattedDate)
          formData.append('gender', this.formInfo.gender)
          axios
            .post('/api/editprofile/', formData, {
              headers: {
                'Content-Type': 'multipart/form-data',
              },
            })
            .then((response) => {
              // localStorage تحديث البيانات في
              // قم بتحديث معلومات المستخدم في المتجر
              userStore.setUserInfo({
                id: userStore.user.id,
                name: this.formInfo.name,
                surname: this.formInfo.surname,
                email: this.formInfo.email,
                date_of_birth: response.data.user.date_of_birth,
                gender: this.formInfo.gender,
                get_avatar: response.data.user.get_avatar,
                get_cover: response.data.user.get_cover,
              })

              // this.toast.add({
              //   severity: 'success',
              //   summary: `🧑 Profile`,
              //   detail: `The information was saved ${response.data.message}`,
              //   life: 3000,
              // })
              if (response.data.message === 'information updated') {
                this.toast.add({
                  severity: 'success',
                  summary: `🧑 Profile`,
                  detail: `The information was saved`,
                  life: 3000,
                })
              }
            })
            .catch((error) => {
              console.log('error', error)
            })
        }
      }
    },
    // ____________________________________________
    // ____________________________________________
    // ____________________________________________
    // 🧑 Get All Friends
    // ____________________________________________
    // ____________________________________________
    // ____________________________________________
    // 🧑 Get All Friends
    getFriends() {
      axios
        .get(`/api/friends/${this.$route.params.id}/`)
        .then((response) => {
          // // For Test
          let line = '📌'.repeat(30)
          console.log(` %c${line} `, 'color: #1cd07c; font-size: 16px')
          console.log('Profile Friends Django Data : ', response.data)
          this.friendshipRequests = response.data.requests
          this.friends = response.data.friends
          this.user = response.data.user
        })
        .catch((error) => {
          console.log('error', error)
        })
    },
    handleRequest(status, pk) {
      console.log('handleRequest', status)
      axios
        .post(`/api/friends/${pk}/${status}/`)
        .then((response) => {
          console.log('data', response.data)
          if (response.data.message == 'Friendship request accepted successfully') {
            this.toast.add({
              severity: 'success',
              summary: `Status ✔️`,
              detail: `Friend Is ${status}`,
              life: 3000,
            })
          }
          if (response.data.message == 'Friendship request rejected successfully') {
            this.toast.add({
              severity: 'error',
              summary: `Status ❌`,
              detail: `Friend Is ${status}`,
              life: 3000,
            })
          }
        })
        .catch((error) => {
          console.log('error', error)
          this.toast.add({
            severity: 'error',
            summary: `Error Friend Status ❌`,
            detail: `Something went wrong Friend Status`,
            life: 3000,
          })
        })
    },
    getFriendSuggestions() {
      axios
        .get('/api/friends/suggested/')
        .then((response) => {
          this.friendsSuggest = response.data
          // For Test
          let line = '📌'.repeat(30)
          console.log(` %c${line} `, 'color: #1cd07c; font-size: 16px')
          console.log('get Friend Suggestions() Django Data : ', response.data)
        })
        .catch((error) => {
          console.log('error', error)
        })
    },
    sendDirectMessage() {
      console.log('sendDirectMessage')
      axios
        .get(`/api/chat/${this.$route.params.id}/get-or-create/`)
        .then((response) => {
          console.log(`chat response.data`, response.data)

          this.$router.push('/')
        })
        .catch((error) => {
          console.log('error', error)
        })
    },
  },
}
</script>

<style lang="scss" scoped></style>
