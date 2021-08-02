import React, { Component } from 'react'
import './style.css';

import { toastOnError } from "../../../utils/Utils";
import axios from 'axios';
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import PropTypes from "prop-types";
import {getCurrencies} from '../../store/CurrenciesActions'
import {getExchanges} from '../../store/ExchangesActions'

import {Container} from "react-bootstrap";
import { Tabs, Tab, AppBar } from "@material-ui/core";

import Assets from './assets/Assets'
import Trades from './trades/Trades'
import Stats from './stats/Stats'
import Settings from './settings/Settings';
import Strategy from './strategy/Strategy';


class Portfolio extends Component {
  
  constructor(props) {
    super(props);
  
    this.state = {
      portfolio: {},
      selectedCurrency: null,
      selectedExchange: null,
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
      executing: false,
      sum: "",
      selectedTab: 0})
  


    axios
    .get(`/api/v1/my_portfolios/${this.props.match.params.id}`)
    .then(res => {

      const portfolio = res.data;
      this.setState({ portfolio: portfolio });
      for(var x = 0; x<this.state.portfolio.assets.length; x++){
        for(var y = 0; y<this.state.portfolio.assets[x].positions.length; y++) {
          sum += this.state.portfolio.assets[x].positions[y].value
        }
        
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

  

    return (

      <div className="portfolio">
        <div className="portfolioHeader">
      
          <h1 className="pageTitle headerLeft">{this.state.portfolio.name}</h1><p className="sumText headerRight">{this.state.sum} $</p>
        </div>
      
        <div className="portfolioNav">
        <AppBar className="portfolioNavAppBar" position="static">
          <Tabs value={this.state.selectedTab} onChange={this.handleChange} centered>
            <Tab label="Assets" />
            <Tab label="Trades" />
            <Tab label="Strategy" />
            <Tab label="Stats" />
            <Tab label="Settings" />
          </Tabs>
        </AppBar>
        </div>
        
        <Container className="portfolioContent">

          {this.state.selectedTab === 0 ? 
          <div className="assets">
        
          {this.state.portfolio.assets !== undefined && this.props.exchanges !== undefined ? 
            <Assets portfolio={this.state.portfolio} currencies={this.props.currencies.currencies} exchanges={this.props.exchanges.exchanges}/> 
         : ""}
          
          </div>

          : ""}

          {this.state.selectedTab === 1 ?
            <Trades portfolio={this.state.portfolio} currencies={this.props.currencies} exchanges={this.props.exchanges}/> : ""
          }

          {this.state.selectedTab === 2 ? 
          <div className="strategy">
            
            {this.state.portfolio.strategy !== undefined ? 
            <Strategy data={this.state.portfolio}/>
            : "No strategy"}
          </div>

          : ""}

          {this.state.selectedTab === 3 ? 
          <div className="graphs">
        
            <Stats assets={this.state.assets}/>

          </div>

          : ""}
        
        {this.state.selectedTab === 4 ? 
          <div className="settings">
        
             {this.state.portfolio !== undefined ? 
            <Settings data={this.state.portfolio}/>
            : "No portfolio data"}

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