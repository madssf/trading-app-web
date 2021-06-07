import { GET_PORTFOLIO_BY_ID } from "./PortfoliosTypes";
import produce from 'immer';

const initialState = {
    portfolio: {},

};

export const portfolioReducer = (state = initialState, action) => {
  switch (action.type) {

    case GET_PORTFOLIO_BY_ID:
        return {
          ...state,
          portfolio: action.payload
        };
          
      
        
    default:
      return state;
  }
};