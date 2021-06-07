import React, { Component } from 'react'
import { toastOnError } from "../../utils/Utils";

import Asset from './Asset'
import axios from 'axios';
import AddAsset from './AddAsset';

export default class PortfolioDetail extends Component {
  state = {
    portfolio: {assets:[]}
  }
  componentDidMount() {

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

    
    let assets = this.state.portfolio.assets.map(asset => {
      return <Asset key={asset.id} asset={asset}/> 
    })
    

    return (
      <div>
      <h1>{this.state.portfolio.name}</h1>
  
      {assets}
      <AddAsset portfolio={this.props.match.params.id}/>
      </div>

    )
  }
}

