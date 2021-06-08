import React, { Component } from 'react'
import { toastOnError } from "../../utils/Utils";
import axios from 'axios';
import PropTypes from "prop-types";

import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import {getCurrencies} from '../currencies/CurrenciesActions'
import {getExchanges} from '../exchanges/ExchangesActions'


import Asset from './Asset'
import AddAsset from './AddAsset';

import Dropdown from '../dropdown/Dropdown'

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
      this.setState({ portfolio });
    })
    .catch(error => {
      toastOnError(error);
    });
  }
  
  render() {

    const {currencies} = this.props.currencies
    const {exchanges} = this.props.exchanges

    let assets = this.state.portfolio.assets.map(asset => {
      return <Asset key={asset.id} asset={asset}/> 
    })
    

    return (
      <div>
      <h1>{this.state.portfolio.name}</h1>
  
      {assets}
      <AddAsset portfolio={this.props.match.params.id} currency={this.state.value}/>
      <div style={{width:200}}>
      <Dropdown 
      options={currencies} 
      prompt="Select a currency..."
      id='id'
      label='name'
      value={this.state.selectedCurrency}
      onChange={val => this.setState({selectedCurrency: val})}
      />
      <Dropdown 
      options={exchanges} 
      prompt="Select an exchange..."
      id='id'
      label='name'
      value={this.state.selectedExchange}
      onChange={val => this.setState({selectedExchange
        : val})}
      />
      </div>
      <p>
      {this.state.selectedCurrency !== null ? this.state.selectedCurrency.id : ""}
      </p>
      <p>
      {this.state.selectedExchange !== null ? this.state.selectedExchange.id : ""}
      </p>
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