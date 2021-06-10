import axios from "axios";
import { toastOnError } from "../../utils/Utils";
import { GET_STRATEGIES } from "./StrategiesTypes";

export const getStrategies = () => dispatch => {
  axios
    .get("/api/v1/strategies/")
    .then(response => {
      dispatch({
        type: GET_STRATEGIES,
        payload: response.data
      });
    })
    .catch(error => {
      toastOnError(error);
    });
};
