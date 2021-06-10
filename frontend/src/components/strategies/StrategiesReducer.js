import { GET_STRATEGIES } from "./StrategiesTypes";

const initialState = {
  strategies: []
};

export const strategiesReducer = (state = initialState, action) => {
  switch (action.type) {
    case GET_STRATEGIES:
      return {
        ...state,
        strategies: action.payload
      };

    default:
      return state;
  }
};