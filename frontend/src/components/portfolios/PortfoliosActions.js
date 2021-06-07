import axios from "axios";
import { toastOnError } from "../../utils/Utils";

export const getPortfolios = () => dispatch => {
  axios
    .get("/api/v1/portfolios/")
    .then(response => {
    
    })
    .catch(error => {
      toastOnError(error);
    });
};

export const getPortfolioById = id => dispatch => {
  axios
    .get(`/api/v1/my_portfolios/${id}`)
    .then(response => {
    
    })
    .catch(error => {
      toastOnError(error);
    });
};

