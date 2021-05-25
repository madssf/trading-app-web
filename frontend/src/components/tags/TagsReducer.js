import { GET_TAGS, ADD_TAG, DELETE_TAG, UPDATE_TAG } from "./TagsTypes";

const initialState = {
  tags: []
};

export const tagsReducer = (state = initialState, action) => {
  switch (action.type) {
    case GET_TAGS:
      return {
        ...state,
        tags: action.payload
      };
    case ADD_TAG:
      return {
        ...state,
        tags: [...state.tags, action.payload]
      };
    case DELETE_TAG:
        return {
          ...state,
          notes: state.tags.filter((item, index) => item.id !== action.payload)
        };
    case UPDATE_TAG:
        const updatedTags = state.tags.map(item => {
          if (item.id === action.payload.id) {
            return { ...item, ...action.payload };
          }
          return item;
        });
        return {
          ...state,
          tags: updatedTags
        };
      
    default:
      return state;
  }
};