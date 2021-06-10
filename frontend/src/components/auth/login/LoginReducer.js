// frontend/src/components/login/LoginReducer.js file

import * as LoginTypes from "./LoginTypes";

const initialState = {
  isAuthenticated: false,
  user: {},
  token: ""
};

export const loginReducer = (state = initialState, action) => {
  switch (action.type) {
    case LoginTypes.SET_TOKEN:
      return {
        ...state,
        isAuthenticated: true,
        token: action.payload
      };
    case LoginTypes.SET_CURRENT_USER:
      return {
        ...state,
        user: action.payload
      };
    case LoginTypes.UNSET_CURRENT_USER:
      return initialState;
    default:
      return state;
  }
};

