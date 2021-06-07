
import React from 'react';
import { toastOnError } from "../../utils/Utils";
import { Link } from "react-router-dom";

import axios from 'axios';

export default class PortfoliosList extends React.Component {
  state = {
    portfolios: []
  }

  componentDidMount() {
    axios
    .get("/api/v1/portfolios/")
    .then(res => {
        const portfolios = res.data;
        this.setState({ portfolios });
      }).catch(error => {
        toastOnError(error);    
      });
  }


  render() {
    return (
      <ul>
        { this.state.portfolios.map(portfolio => <Link to={`/portfolios/${portfolio.id}`}>{portfolio.name}</Link>)}
      </ul>
    )
  }
}