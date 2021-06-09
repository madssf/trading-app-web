import React, {useState} from 'react';
import axios from 'axios';
import {Container, Button} from "react-bootstrap";
import DateTimePicker from "../../utils/DateTimePicker";
import {toastOnError} from "../../utils/Utils";

import DatePicker from 'react-datetime';
import moment from 'moment';
import 'react-datetime/css/react-datetime.css';

import Dropdown from '../dropdown/Dropdown';
import "./style.css"
export default class AddAsset extends React.Component {
  constructor(props){
    super(props);
    this.state={
        stakeDisplay: false,
    }
}
  
  state = {
    staked: true, 
    currency: null,
    exchange: null,
    status: null,
    amount: null,
    apr: null,
    stakeStart: moment(),
    stakeEnd: moment()
  }




  handleChange = event => {
    this.setState({ [event.target.name]: event.target.value });
  };

  setShowStaked = event => {
    let staked = !this.state.showStaked
    this.setState({showStaked: staked})
  }

  handleSubmit = event => {
    event.preventDefault();

    const asset = {
      portfolio: this.props.portfolio, 
      currency: this.state.currency.id,
      exchange: this.state.exchange.id,
      status: this.state.status.status,
      amount: this.state.amount,
      apr: this.state.apr,
      stake_start: this.state.stakeStart,
      stake_end: this.state.stakeEnd,
      close_time: null
    };

    // do validation
/*
    axios.post(`http://localhost:1337/api/v1/portfolio_assets/`, asset, {headers: {
      'Content-Type': 'application/json'
  }})
      .then(res => {
      }).catch(error => {
        toastOnError(error);
      });
*/
    console.log(asset)
  }

  render() {
    return (
      <div className="addAssetForm">
      <Container>

        <span>
          <h2 className="addAssetHeader">Add an asset manually:</h2>
        </span>
        <input className="amountInput" type="number" step="0.001"name="amount" placeholder="Amount" onChange={this.handleChange} />

        <form onSubmit={this.handleSubmit}>
      
      <label>
      <button type="submit">Add</button>

      </label>

    </form>

        <div className="dropdowns" >
          
          <Dropdown 
          options={this.props.currencies} 
          prompt="Select a currency..."
          id='id'
          label='name'
          value={this.state.currency}
          onChange={val => this.setState({currency
            : val})}
          />

           <Dropdown 
          options={this.props.exchanges} 
          prompt="Select an exchange..."
          id='id'
          label='name'
          value={this.state.exchange}
          onChange={val => this.setState({exchange
            : val})}
          />

           <Dropdown 
          options={[{'id': 1, 'status': 'SPOT'},{'id': 2, 'status': 'FLEX'},{'id': 3, 'status': 'LOCK'}]} 
          prompt="Select status..."
          id='id'
          label='status'
          value={this.state.status}
          onChange={val => this.setState({status
            : val})}
          />
        </div>

        <Button className="currencyAssetBtn" onClick={() => this.setShowStaked(prev => !prev)}>{this.state.showStaked ? "Hide staked info" : "Show staked info"}</Button>

        <div className="stakedForm">

        {this.state.showStaked ? <Container>
          <div className="DateTimePicker">
            <DatePicker
            inputProps={{
              style: { width: 250 }
            }}
            value={this.state.stakeStart}
            dateFormat="DD-MM-YYYY"
            timeFormat="hh:mm A"
            onChange={val => this.setState({stakeStart: val})}
            /> 
          </div>
          <div className="DateTimePicker">
            <DatePicker
            inputProps={{
              style: { width: 250 }
            }}
            value={this.state.stakeEnd}
            dateFormat="DD-MM-YYYY"
            timeFormat="hh:mm A"
            onChange={val => this.setState({stakeEnd: val.format('DD-MM-YYYY, hh:mm')})}
            /> 
          </div>
          </Container> : ""}

        {this.state.showStaked ? <input type="number" step="0.01" name="apr" placeholder="APR" onChange={this.handleChange} /> : ""}



      
        </div>

      </Container>
      </div>
    )
  }
}