import axios from "axios";
import { toastOnError } from "../../utils/Utils";
import { GET_TAGS, ADD_TAG, DELETE_TAG, UPDATE_TAG } from "./TagsTypes";

export const getTags = () => dispatch => {
  axios
    .get("/api/v1/tags/")
    .then(response => {
      dispatch({
        type: GET_TAGS,
        payload: response.data
      });
    })
    .catch(error => {
      toastOnError(error);
    });
};

export const addTag = tag => dispatch => {
  axios
    .post("/api/v1/tags/", tag)
    .then(response => {
      dispatch({
        type: ADD_TAG,
        payload: response.data
      });
    })
    .catch(error => {
      toastOnError(error);
    });
};

export const deleteTag = id => dispatch => {
  axios
    .delete(`/api/v1/tags/${id}/`)
    .then(response => {
      dispatch({
        type: DELETE_TAG,
        payload: id
      });
    })
    .catch(error => {
      toastOnError(error);
    });
};

export const updateTag = (id, tag) => dispatch => {
  axios
    .patch(`/api/v1/tags/${id}/`, tag)
    .then(response => {
      dispatch({
        type: UPDATE_TAG,
        payload: response.data
      });
    })
    .catch(error => {
      toastOnError(error);
    });
};
