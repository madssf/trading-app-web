import * as SignupTypes from "./SignupTypes";

const initialState = {
  usernameError: "",
  passwordError: "",
  isSubimtted: false
};

export const signupReducer = (state = initialState, action) => {
  switch (action.type) {
    case SignupTypes.CREATE_USER_SUBMITTED:
      return {
        usernameError: "",
        passwordError: "",
        isSubimtted: true
      };
    case SignupTypes.CREATE_USER_ERROR:
      const errorState = {
        usernameError: "",
        passwordError: "",
        isSubimtted: false
      };
      if (action.errorData.hasOwnProperty("username")) {
        errorState.usernameError = action.errorData["username"];
      }
      if (action.errorData.hasOwnProperty("password")) {
        errorState.passwordError = action.errorData["password"];
      }
      return errorState;
    case SignupTypes.CREATE_USER_SUCCESS:
      return {
        usernameError: "",
        passwordError: "",
        isSubimtted: false
      };
    default:
      return state;
  }
}