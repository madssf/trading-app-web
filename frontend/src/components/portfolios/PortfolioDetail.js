import React, { Component } from 'react'
import { toastOnError } from "../../utils/Utils";
import axios from 'axios';
import PropTypes from "prop-types";

import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import {getCurrencies} from '../currencies/CurrenciesActions'
import {getExchanges} from '../exchanges/ExchangesActions'


import Assets from './Assets'
import AddAsset from './AddAsset';

class PortfolioDetail extends Component {

  state = {
    portfolio: {assets:[]},
    selectedCurrency: null,
    selectedExchange: null,
  }
  componentDidMount() {
    this.props.getCurrencies();
    this.props.getExchanges();

    axios
    .get(`/api/v1/my_portfolios/${this.props.match.params.id}`)
    .then(res => {
      const portfolio = res.data;
      const assets = portfolio.assets
      this.setState({ portfolio });
      this.setState({ assets });

    })
    .catch(error => {
      toastOnError(error);
    });
  }
  
  render() {

    const {currencies} = this.props.currencies
    const {exchanges} = this.props.exchanges


    return (
      <div className="portfolioDetail">
      <h1 className="pageTitle">{this.state.portfolio.name}</h1>
      <div className="portfolioDetailGrid">
      <div className="portfolioDetailGrid1">
      {this.state.assets !== undefined && this.props.exchanges !== undefined ? <Assets assets={this.state.assets} exchanges={this.props.exchanges}/> : "No assets"}
      </div>
      <div className="portfolioDetailGrid2">
      <AddAsset portfolio={this.props.match.params.id} currencies={currencies} exchanges={exchanges}/>
      </div>
      </div>
      </div>
    )
  }
}

PortfolioDetail.propTypes = {
  currencies: PropTypes.object.isRequired,
  getCurrencies: PropTypes.func.isRequired,
  exchanges: PropTypes.object.isRequired,
  getExchanges: PropTypes.func.isRequired,
}
const mapStateToProps = state => ({
  currencies: state.currencies,
  exchanges: state.exchanges

});
export default connect(mapStateToProps, {getCurrencies, getExchanges})(withRouter(PortfolioDetail))