import { defineStore } from "pinia";
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

export const useAuthStore = defineStore(
  "auth",
  () => {
    const router = useRouter();

    // loginState=true → ログイン中
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
    const refresher = (access, refresh) => {
      accessToken.value = access;
      refreshToken.value = refresh;
    };

    // トークンrefresh
    const refreshApi = () => {
      axios
        .post("auth/jwt/refresh", {
          refresh: `${refreshToken.value}`,
        })
        .then((response) => {
          // storeのトークン更新
          refresher(response.data.access, response.data.refresh);
          location.reload();
        })
        .catch(() => {
          // トークンrefresh出来なかったら、ログアウトしてログイン画面へ
          logout();
          router.push("/login");
        });
    };

    return {
      loginState,
      email,
      accessToken,
      refreshToken,
      login,
      logout,
      refresher,
      refreshApi,
    };
  },
  {
    // Storeの永続化
    persist: true,
  }
);
