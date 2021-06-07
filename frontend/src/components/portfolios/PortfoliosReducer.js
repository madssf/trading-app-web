import { GET_PORTFOLIOS } from "./PortfoliosTypes";

const initialState = {
  portfolios: [],
};

export const portfoliosReducer = (state = initialState, action) => {
  switch (action.type) {
    case GET_PORTFOLIOS:
      return {
        ...state,
        portfolios: action.payload
      };
   

    default:
      return state;
  }
};