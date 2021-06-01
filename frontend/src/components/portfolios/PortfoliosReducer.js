import { GET_PORTFOLIOS, ADD_PORTFOLIO, DELETE_PORTFOLIO, UPDATE_PORTFOLIO } from "./PortfoliosTypes";

const initialState = {
  portfolios: []
};

export const portfoliosReducer = (state = initialState, action) => {
  switch (action.type) {
    case GET_PORTFOLIOS:
      return {
        ...state,
        portfolios: action.payload
      };
    case ADD_PORTFOLIO:
      return {
        ...state,
        portfolios: [...state.portfolios, action.payload]
      };
    case DELETE_PORTFOLIO:
        return {
          ...state,
          portfolios: state.portfolios.filter((item, index) => item.id !== action.payload)
        };
    case UPDATE_PORTFOLIO:
        const updatedPortfolios = state.portfolios.map(item => {
          if (item.id === action.payload.id) {
            return { ...item, ...action.payload };
          }
          return item;
        });
        return {
          ...state,
          portfolios: updatedPortfolios
        };
      
    default:
      return state;
  }
};