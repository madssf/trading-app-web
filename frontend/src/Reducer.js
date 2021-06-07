// frontend/src/Reducer.js
import { combineReducers } from "redux";
import { connectRouter } from "connected-react-router";

import { signupReducer } from "./components/signup/SignupReducer";
import { loginReducer } from "./components/login/LoginReducer";
import { currenciesReducer } from "./components/currencies/CurrenciesReducer"
import { portfoliosReducer } from "./components/portfolios/PortfoliosReducer"
import { portfolioReducer } from "./components/portfolios/PortfolioReducer"

const createRootReducer = history =>
  combineReducers({
    router: connectRouter(history),
    createUser: signupReducer,
    auth: loginReducer,
    currencies: currenciesReducer,
    portfolios: portfoliosReducer,
    portfolio: portfolioReducer


  });    

export default createRootReducer;