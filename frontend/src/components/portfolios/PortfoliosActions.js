import axios from "axios";
import { toastOnError } from "../../utils/Utils";
import { GET_PORTFOLIOS, GET_PORTFOLIO_BY_ID } from "./PortfoliosTypes";

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

export const getPortfolioById = id => dispatch => {
  axios
    .get(`/api/v1/my_portfolios/${id}`)
    .then(response => {
      dispatch({
        type: GET_PORTFOLIO_BY_ID,
        payload: response.data
      });
    })
    .catch(error => {
      toastOnError(error);
    });
};

