// frontend/src/Reducer.js
import { combineReducers } from "redux";
import { connectRouter } from "connected-react-router";

import { signupReducer } from "./components/signup/SignupReducer";
import { loginReducer } from "./components/login/LoginReducer";
import { currenciesReducer } from "./components/currencies/CurrenciesReducer"
import { exchangesReducer } from "./components/exchanges/ExchangesReducer"
const createRootReducer = history =>
  combineReducers({
    router: connectRouter(history),
    createUser: signupReducer,
    auth: loginReducer,
    currencies: currenciesReducer,
    exchanges: exchangesReducer,

  });    

export default createRootReducer;