// frontend/src/Reducer.js
import { combineReducers } from "redux";
import { connectRouter } from "connected-react-router";

import { signupReducer } from "./components/signup/SignupReducer";
import { loginReducer } from "./components/login/LoginReducer";
import { tagsReducer } from "./components/tags/TagsReducer";
import { portfoliosReducer } from "./components/portfolios/PortfoliosReducer";


const createRootReducer = history =>
  combineReducers({
    router: connectRouter(history),
    createUser: signupReducer,
    auth: loginReducer,
    tags: tagsReducer,
    portfolios: portfoliosReducer
  });    

export default createRootReducer;