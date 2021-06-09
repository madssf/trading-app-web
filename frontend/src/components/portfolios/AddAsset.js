import React from 'react';
import axios from 'axios';
import {Container} from "react-bootstrap";
import DateTimePicker from "../../utils/DateTimePicker";
import {toastOnError} from "../../utils/Utils";

import Dropdown from '../dropdown/Dropdown';
import "./style.css"
export default class AddAsset extends React.Component {
  
  state = {
    currency: null,
    exchange: null,
    status: null,
    amount: null,
    apr: null,
    stakeStart: null,
    stakeEnd: null
  }

  handleChange = event => {
    this.setState({ [event.target.name]: event.target.value });
  };

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

    axios.post(`http://localhost:1337/api/v1/portfolio_assets/`, asset, {headers: {
      'Content-Type': 'application/json'
  }})
      .then(res => {
      }).catch(error => {
        toastOnError(error);
      });

  }

  render() {
    return (
      <Container >
      <div className="addAssetForm" style={{}}>
        <span>Add an asset manually:</span>
        <div style={{width: 300}}>
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
        <div>

          <DateTimePicker />
          <DateTimePicker />
          <DateTimePicker />


        </div>
        <form onSubmit={this.handleSubmit}>
          <label>
            <input type="number" step="0.001"name="amount" placeholder="Amount" onChange={this.handleChange} />
            <input type="number" step="0.01" name="apr" placeholder="APR" onChange={this.handleChange} />
            <input type="text" name="stake_start" placeholder="Stake start" onChange={this.handleChange} />
            <input type="text" name="stake_end" placeholder="Stake end" onChange={this.handleChange} />
          </label>
          <button type="submit">Add</button>
        </form>
      </div>
      </Container>
    )
  }
}