import axios from "axios";
import { toastOnError } from "../../utils/Utils";
import { GET_EXCHANGES } from "./ExchangesTypes";

export const getExchanges = () => dispatch => {
  axios
    .get("/api/v1/exchanges/")
    .then(response => {
      dispatch({
        type: GET_EXCHANGES,
        payload: response.data
      });
    })
    .catch(error => {
      toastOnError(error);
    });
};
