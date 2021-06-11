import React, { Component } from 'react'
import './style.css';

import { toastOnError } from "../../../utils/Utils";
import axios from 'axios';
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import PropTypes from "prop-types";
import {getCurrencies} from '../../store/CurrenciesActions'
import {getExchanges} from '../../store/ExchangesActions'

import {Container, Button} from "react-bootstrap";
import { Tabs, Tab, AppBar } from "@material-ui/core";

import Assets from './assets/Assets'
import AddAsset from './assets/AddAsset';
import BatchAddAsset from './assets/BatchAddAsset';
import Graphs from './graphs/Graphs'
import Settings from './settings/Settings';
import Strategy from './strategy/Strategy';


class Portfolio extends Component {
  
  constructor(props) {
    super(props);
  
    this.state = {
      portfolio: {assets:[]},
      selectedCurrency: null,
      selectedExchange: null,
      showAdd: false,
      showBatchAdd: false,
      executing: false,
      sum: "",
      selectedTab: 0
    }
  }

  componentDidMount() {
    this.props.getCurrencies();
    this.props.getExchanges();

    this.setState({portfolio: {assets:[]},
      selectedCurrency: null,
      selectedExchange: null,
      showAdd: false,
      showBatchAdd: false,
      executing: false,
      sum: "",
      selectedTab: 0})
  


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


  handleChange = (e, a) => { 
    this.setState({selectedTab: a});
  }

  
  render() {

    const {currencies} = this.props.currencies
    const {exchanges} = this.props.exchanges
  

    return (

      <div className="portfolio">
        <div className="portfolioHeader">
      
          <h1 className="pageTitle headerLeft">{this.state.portfolio.name}</h1><p className="sumText headerRight">{this.state.sum} $</p>
        </div>
      
        <div className="portfolioNav">
        <AppBar className="portfolioNavAppBar" position="static">
          <Tabs value={this.state.selectedTab} onChange={this.handleChange} centered>
            <Tab label="Assets" />
            <Tab label="Strategy" />
            <Tab label="Graphs" />
            <Tab label="Settings" />
          </Tabs>
        </AppBar>
        </div>
        
        <Container className="portfolioContent">

          {this.state.selectedTab === 0 ? 
          <div className="assets">
        
          {this.state.assets !== undefined && this.props.exchanges !== undefined ? 
            <Assets assets={this.state.assets} exchanges={this.props.exchanges}/> 
         : ""}

          <Button className="toggleView" onClick={() => this.setState({showAdd: !this.state.showAdd})}>{this.state.showAdd ? "Close" : "Add assets"}</Button>
          <Button className="toggleView" onClick={() => this.setState({showBatchAdd: !this.state.showBatchAdd})}>{this.state.showBatchAdd ? "Close" : "Batch add assets"}</Button>
          {this.state.showAdd ?  
          <AddAsset portfolio={this.props.match.params.id} currencies={currencies} exchanges={exchanges}/>
            : ""}
          {this.state.showBatchAdd ?  
          <BatchAddAsset portfolio={this.props.match.params.id} exchanges={exchanges}/>
            : ""}
          </div>

          : ""}

          {this.state.selectedTab === 1 ? 
          <div className="strategy">
        
            <Strategy/>

          </div>

          : ""}

          {this.state.selectedTab === 2 ? 
          <div className="graphs">
        
            <Graphs assets={this.state.assets}/>

          </div>

          : ""}
        
        {this.state.selectedTab === 3 ? 
          <div className="settings">
        
            <Settings/>

          </div>

          : ""}

        </Container>

  
     


    

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