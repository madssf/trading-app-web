import { GET_CURRENCIES } from "./CurrenciesTypes";

const initialState = {
  currencies: []
};

export const currenciesReducer = (state = initialState, action) => {
  switch (action.type) {
    case GET_CURRENCIES:
      return {
        ...state,
        currencies: action.payload
      };

    default:
      return state;
  }
};