// frontend/src/Reducer.js
import { combineReducers } from "redux";
import { connectRouter } from "connected-react-router";

import { signupReducer } from "./components/auth/signup/SignupReducer";
import { loginReducer } from "./components/auth/login/LoginReducer";
import { currenciesReducer } from "./components/store/CurrenciesReducer"
import { exchangesReducer } from "./components/store/ExchangesReducer"
import { strategiesReducer } from "./components/store/StrategiesReducer";
const createRootReducer = history =>
  combineReducers({
    router: connectRouter(history),
    createUser: signupReducer,
    auth: loginReducer,
    currencies: currenciesReducer,
    exchanges: exchangesReducer,
    strategies: strategiesReducer,


  });    

export default createRootReducer;