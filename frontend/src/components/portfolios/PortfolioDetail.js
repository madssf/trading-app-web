import React, { Component } from 'react'
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import {getPortfolioById} from './PortfoliosActions'
import Asset from './Asset'

export class PortfolioDetail extends Component {
  componentDidMount() {
    this.props.getPortfolioById(this.props.match.params.id);
  }
  render() {

    const {portfolio} = this.props.portfolio
    
    let assets = this.props.portfolio.assets.map(asset => {
      return <Asset key={asset.id} asset={asset}/>
    })
    

    return (
      <div>
      <h1>{portfolio.name}</h1>
      <p>Strategy: <b>{portfolio.strategy}</b></p>
      {assets}

      </div>

    )
  }
}


PortfolioDetail.propTypes = {
  portfolio: PropTypes.object.isRequired,
  getPortfolioById: PropTypes.func.isRequired,
};

const mapStateToProps = state => ({
  portfolio: state.portfolio,
});

export default connect(mapStateToProps, {getPortfolioById})(withRouter(PortfolioDetail));
