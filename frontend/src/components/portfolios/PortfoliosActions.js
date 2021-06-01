import axios from "axios";
import { toastOnError } from "../../utils/Utils";
import { GET_PORTFOLIOS, ADD_PORTFOLIO, DELETE_PORTFOLIO, UPDATE_PORTFOLIO } from "./PortfoliosTypes";

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

export const addPortfolio = portfolio => dispatch => {
  axios
    .post("/api/v1/portfolios/", portfolio)
    .then(response => {
      dispatch({
        type: ADD_PORTFOLIO,
        payload: response.data
      });
    })
    .catch(error => {
      toastOnError(error);
    });
};

export const deletePortfolio = id => dispatch => {
  axios
    .delete(`/api/v1/portfolios/${id}/`)
    .then(response => {
      dispatch({
        type: DELETE_PORTFOLIO,
        payload: id
      });
    })
    .catch(error => {
      toastOnError(error);
    });
};

export const updatePortfolio = (id, portfolio) => dispatch => {
  axios
    .patch(`/api/v1/portfolios/${id}/`, portfolio)
    .then(response => {
      dispatch({
        type: UPDATE_PORTFOLIO,
        payload: response.data
      });
    })
    .catch(error => {
      toastOnError(error);
    });
};
