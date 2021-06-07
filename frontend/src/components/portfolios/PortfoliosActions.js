import axios from "axios";
import { toastOnError } from "../../utils/Utils";
import { GET_PORTFOLIOS } from "./PortfoliosTypes";

export const getPortfolios = () => dispatch => {
  axios
    .get("/api/v1/portfolios/")
    .then(response => {
      dispatch({
        type: GET_PORTFOLIOS,
        payload: response.data
      });
    })
    .catch(error => {
      toastOnError(error);
    });
};
