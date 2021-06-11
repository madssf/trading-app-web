import React, { Component } from 'react'
import { connect } from 'react-redux'
import PropTypes from "prop-types";
import { withRouter } from "react-router-dom";

import {getCurrencies} from '../../store/CurrenciesActions'
import {getExchanges} from '../../store/ExchangesActions'

import PortfolioNav from './PortfolioNav'
import PortfolioDetail from './PortfolioDetail'

import { toastOnError } from "../../../utils/Utils";
import axios from 'axios';


export class Portfolio extends Component {

  state = {
    hasAssets: false,
    portfolio: {assets:[]},
    selectedCurrency: null,
    selectedExchange: null,
    showAdd: false,
    showBatchAdd: false,
    executing: false,
    refreshing: false
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
    if (this.state.assets === undefined) {
      this.setState({hasAssets: false})
    } else {
      this.setState({hasAssets: true})
    }
  }

  execute() {
    this.setState({executing: true})
    console.log('executing')
  }

  refresh() {
    this.setState({refreshing: true})
    console.log('refreshing')
  }

  
  render() {

    let sum = 0
    if (this.state.assets === undefined || this.state.assets.length === 0) {
        sum = 0
    } else {
        for(var x = 0; x<this.state.assets.length; x++){sum += this.state.assets[x].value}
    }
    sum = Math.round(sum*100)/100
  
    return (


      <div className="portfolioHeader">
        <div className="portfolioTitleInfo">
        <h1 className="pageTitle">{this.state.portfolio.name}</h1> 
        <p className="sumText"> {sum} $</p>
        </div>
        <PortfolioNav portfolio={this.state.portfolio} exchanges={this.state.exchanges} currencies={this.state.currencies}/>
        <PortfolioDetail />
      </div>
    )
  }
}

Portfolio.propTypes = {
  currencies: PropTypes.object.isRequired,
  getCurrencies: PropTypes.func.isRequired,
  exchanges: PropTypes.object.isRequired,
  getExchanges: PropTypes.func.isRequired,
}
const mapStateToProps = state => ({
  currencies: state.currencies,
  exchanges: state.exchanges

});
export default connect(mapStateToProps, {getCurrencies, getExchanges})(withRouter(Portfolio))