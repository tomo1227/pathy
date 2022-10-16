import { defineStore } from "pinia";
import { ref } from "vue";

export const useAuthStore = defineStore(
  "auth",
  () => {
    const loginState = ref(false);
    const email = ref("");
    const accessToken = ref("");
    const refreshToken = ref("");

    // ログイン
    const login = (mail, access, refresh) => {
      loginState.value = true;
      email.value = mail;
      accessToken.value = access;
      refreshToken.value = refresh;
    };

    // ログアウト
    const logout = () => {
      loginState.value = false;
      email.value = "";
      accessToken.value = "";
      refreshToken.value = "";
    };

    // トークンのリフレッシュ
    const refresh = (access, refresh) => {
      accessToken.value = access;
      refreshToken.value = refresh;
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
  },
  {
    // storeの永続化
    persist: true,
  }
);
