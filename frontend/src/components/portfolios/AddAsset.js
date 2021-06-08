import React from 'react';
import axios from 'axios';
import { toastOnError } from "../../utils/Utils";

export default class AddAsset extends React.Component {
  
  state = {
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
      currency: this.props.currency,
      exchange: this.state.exchange,
      status: this.state.status,
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
        console.log(res);
        console.log(res.data);
      }).catch(error => {
        toastOnError(error);
      });

  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <label>
            Add asset:
            <input type="text" name="currency" placeholder="Currency" onChange={this.handleChange} />
            <input type="text" name="exchange" placeholder="Exchange" onChange={this.handleChange} />
            <input type="text" name="status" placeholder="Status" onChange={this.handleChange} />
            <input type="text" name="amount" placeholder="Amount" onChange={this.handleChange} />
            <input type="text" name="apr" placeholder="APR" onChange={this.handleChange} />
            <input type="text" name="stake_start" placeholder="Stake start" onChange={this.handleChange} />
            <input type="text" name="stake_end" placeholder="Stake end" onChange={this.handleChange} />
          </label>
          <button type="submit">Add</button>
        </form>
      </div>
    )
  }
}