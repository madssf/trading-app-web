import { GET_EXCHANGES } from "./ExchangesTypes";

const initialState = {
  exchanges: []
};

export const exchangesReducer = (state = initialState, action) => {
  switch (action.type) {
    case GET_EXCHANGES:
      return {
        ...state,
        exchanges: action.payload
      };

    default:
      return state;
  }
};