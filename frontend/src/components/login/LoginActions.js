// frontend/src/components/login/LoginActions.js

import axios from "axios";
import { push } from "connected-react-router";
import { toast } from "react-toastify";
import * as LoginTypes from "./LoginTypes";
import { setAxiosAuthToken, toastOnError } from "../../utils/Utils";

export const login = (userData, redirectTo) => dispatch => {
  axios
    .post("/api/v1/token/login/", userData)
    .then(response => {
      const { auth_token } = response.data;
      setAxiosAuthToken(auth_token);
      dispatch(setToken(auth_token));
      dispatch(getCurrentUser(redirectTo));
    })
    .catch(error => {
      dispatch(unsetCurrentUser());
      toastOnError(error);
    });
};

export const getCurrentUser = redirectTo => dispatch => {
  axios
    .get("/api/v1/users/me/")
    .then(response => {
      const user = {
        username: response.data.username,
        email: response.data.email
      };
      dispatch(setCurrentUser(user, redirectTo));
    })
    .catch(error => {
      dispatch(unsetCurrentUser());
      toastOnError(error);
    });
};

export const setCurrentUser = (user, redirectTo) => dispatch => {
  localStorage.setItem("user", JSON.stringify(user));
  dispatch({
    type: LoginTypes.SET_CURRENT_USER,
    payload: user
  });

  if (redirectTo !== "") {
    dispatch(push(redirectTo));
  }
};

export const setToken = token => dispatch => {
  setAxiosAuthToken(token);
  localStorage.setItem("token", token);
  dispatch({
    type: LoginTypes.SET_TOKEN,
    payload: token
  });
};

export const unsetCurrentUser = () => dispatch => {
  setAxiosAuthToken("");
  localStorage.removeItem("token");
  localStorage.removeItem("user");
  dispatch({
    type: LoginTypes.UNSET_CURRENT_USER
  });
};

export const logout = () => dispatch => {
  axios
    .post("/api/v1/token/logout/")
    .then(response => {
      dispatch(unsetCurrentUser());
      dispatch(push("/"));
      toast.success("Logout successful.");
    })
    .catch(error => {
      dispatch(unsetCurrentUser());
      toastOnError(error);
    });
};
