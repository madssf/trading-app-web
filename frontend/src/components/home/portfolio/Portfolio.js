import React, { Component } from 'react'
import './style.css';

import { toastOnError } from "../../../utils/Utils";
import axios from 'axios';
import PropTypes from "prop-types";
import {Container, Button} from "react-bootstrap";

import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import {getCurrencies} from '../../store/CurrenciesActions'
import {getExchanges} from '../../store/ExchangesActions'

import PortfolioNav from './PortfolioNav';
import Assets from './assets/Assets'
import Graphs from './graphs/Graphs'
import AddAsset from './assets/AddAsset';
import BatchAddAsset from './assets/BatchAddAsset';
import Credentials from './Credentials';
import Strategy from './strategy/Strategy';

class Portfolio extends Component {

  state = {
    portfolio: {assets:[]},
    selectedCurrency: null,
    selectedExchange: null,
    showAdd: false,
    showBatchAdd: false,
    executing: false,
    refreshing: false,
    sum: ""
  }

  componentDidMount() {
    this.props.getCurrencies();
    this.props.getExchanges();



    axios
    .get(`/api/v1/my_portfolios/${this.props.match.params.id}`)
    .then(res => {
      const portfolio = res.data;
      this.setState({ portfolio: portfolio });
      this.setState({ assets: portfolio.assets });
      for(var x = 0; x<this.state.assets.length; x++){
        sum += this.state.assets[x].value
      }
      
      this.setState({sum: Math.round(sum*100)/100})
  

    })
    .catch(error => {
      toastOnError(error);
    });

    let sum = 0
    
   

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
        <div className="portfolioHeader">
      
      <h1 className="pageTitle headerLeft">{this.state.portfolio.name}</h1><p className="sumText headerRight">{this.state.sum} $</p>
    
      </div>
        <PortfolioNav /> 
      
        <div className="portfolioGrid1">
          <Container>
        
      {this.state.assets !== undefined && this.props.exchanges !== undefined ? 
      
      <Assets assets={this.state.assets} exchanges={this.props.exchanges}/> 
    
      : ""}

          <Button className="refreshBtn" disabled={this.state.refreshing} onClick={() => this.refresh()}>Refresh</Button>

          <Button className="toggleView" onClick={() => this.setState({showAdd: !this.state.showAdd})}>{this.state.showAdd ? "Close" : "Add assets"}</Button>
         
        <Button className="toggleView" onClick={() => this.setState({showBatchAdd: !this.state.showBatchAdd})}>{this.state.showBatchAdd ? "Close" : "Batch add assets"}</Button>
        {this.state.showAdd ?  
          <AddAsset portfolio={this.props.match.params.id} currencies={currencies} exchanges={exchanges}/>
            : ""}
          {this.state.showBatchAdd ?  
          <BatchAddAsset portfolio={this.props.match.params.id} exchanges={exchanges}/>
            : ""}
          </Container>
        </div>

      <div className="portfolioGrid2">
        <Container>
        {this.state.portfolio !== undefined ? <Graphs portfolio={this.state.portfolio}/> : ""}
        {this.state.portfolio !== undefined ? <Strategy portfolio={this.state.portfolio}/> : ""}
        </Container>
      </div>

      <div className="portfolioGrid3">
      <Container>

        <Button className="action" disabled={this.state.executing} onClick={() => this.execute()}>Execute</Button>
       
               <Button className="toggleView" onClick={() => this.setState({showCredentials: !this.state.showCredentials})}>{this.state.showCredentials ? "Close" : "Manage credentials"}</Button>
          {this.state.showCredentials ?  
          <Credentials portfolio={this.props.match.params.id} exchanges={exchanges}/>
          : ""}
                  </Container>

      </div>


    

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