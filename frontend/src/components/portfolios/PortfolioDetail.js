import React, { Component } from 'react'
import { toastOnError } from "../../utils/Utils";
import axios from 'axios';
import PropTypes from "prop-types";
import {Container, Button} from "react-bootstrap";

import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import {getCurrencies} from '../currencies/CurrenciesActions'
import {getExchanges} from '../exchanges/ExchangesActions'

import PortfolioDetailView from './PortfolioDetailView/PortfolioDetailView'
import Assets from './Assets'
import AddAsset from './AddAsset';
import BatchAddAsset from './BatchAddAsset';
import Credentials from './Credentials';
import Strategy from './Strategy';

class PortfolioDetail extends Component {

  state = {
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

    const {currencies} = this.props.currencies
    const {exchanges} = this.props.exchanges


    return (
      <div className="portfolioDetail">
      <h1 className="pageTitle">{this.state.portfolio.name}</h1>

      <div className="portfolioDetailGrid">
      
      <div className="portfolioDetailGrid1">
        
      {this.state.assets !== undefined && this.props.exchanges !== undefined ? 
      
      <Assets assets={this.state.assets} exchanges={this.props.exchanges}/> 
      
      
      : ""}

      </div>

      <div className="portfolioDetailGrid2">
        {this.state.portfolio !== undefined ? <PortfolioDetailView portfolio={this.state.portfolio}/> : ""}
        {this.state.portfolio !== undefined ? <Strategy portfolio={this.state.portfolio}/> : ""}

      </div>

      <div className="portfolioDetailGrid3">

        <Button className="executeBtn" disabled={this.state.executing} onClick={() => this.execute()}>Execute</Button>
        <Button className="refreshBtn" disabled={this.state.refreshing} onClick={() => this.refresh()}>Refresh</Button>
        <Button className="toggleView" onClick={() => this.setState({showAdd: !this.state.showAdd})}>{this.state.showAdd ? "Close" : "Add assets"}</Button>
          {this.state.showAdd ?  
          <AddAsset portfolio={this.props.match.params.id} currencies={currencies} exchanges={exchanges}/>
            : ""}
        <Button className="toggleView" onClick={() => this.setState({showBatchAdd: !this.state.showBatchAdd})}>{this.state.showBatchAdd ? "Close" : "Batch add assets"}</Button>
          {this.state.showBatchAdd ?  
          <BatchAddAsset portfolio={this.props.match.params.id} exchanges={exchanges}/>
            : ""}

        <Button className="toggleView" onClick={() => this.setState({showCredentials: !this.state.showCredentials})}>{this.state.showCredentials ? "Close" : "Manage credentials"}</Button>
          {this.state.showCredentials ?  
          <Credentials portfolio={this.props.match.params.id} exchanges={exchanges}/>
          : ""}
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