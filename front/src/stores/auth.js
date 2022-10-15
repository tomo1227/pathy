import { defineStore } from "pinia";
import { ref } from "vue";

export const useAuthStore = defineStore("auth", () => {
  const loginState = ref(false);
  const email = ref("");
  const accessToken = ref("");
  const refreshToken = ref("");

  const login = (mail, access, refresh) => {
    loginState.value = true;
    email.value = mail;
    accessToken.value = access;
    refreshToken.value = refresh;
  };

  const logout = () => {
    loginState.value = false;
    email.value = "";
    accessToken.value = "";
    refreshToken.value = "";
  };

  const refresh = (access) => {
    accessToken.value = access;
  };

  return {
    loginState,
    email,
    accessToken,
    refreshToken,
    login,
    logout,
    refresh,
  };
});
