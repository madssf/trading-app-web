import axios from "axios";
import { toastOnError } from "../../utils/Utils";
import { GET_CURRENCIES } from "./CurrenciesTypes";

export const getCurrencies = () => dispatch => {
  axios
    .get("/api/v1/currencies/")
    .then(response => {
      dispatch({
        type: GET_CURRENCIES,
        payload: response.data
      });
    })
    .catch(error => {
      toastOnError(error);
    });
};
