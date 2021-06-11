import React, { Component } from 'react'
import {Button} from 'react-bootstrap'
import PropTypes from 'prop-types'
import { withRouter } from "react-router-dom";
import {getCurrencies} from '../../store/CurrenciesActions'
import {getExchanges} from '../../store/ExchangesActions'

import { connect } from 'react-redux'
import './style.css'




class PortfolioNav extends Component {

  componentDidMount() {
    this.setState({nav: [true, false, false, false]})

    this.props.getCurrencies()
    this.props.getExchanges()
  }

  handleClick = event => {
    console.log(event.target)

    this.setState({nav: [true, false, false, false]})

  }

  render() {
    
    if (this.state === null) {
      return ""
    }
    return (
      <div className="portfolioNav">

        <Button type="assets" disabled={this.state.nav[0]} onClick={this.handleClick} className="tabTitle">Assets</Button>
        <Button type="graphs" disabled={this.state.nav[1]} onClick={this.handleClick} className="tabTitle">Graphs</Button>
        <Button type="strategy" disabled={this.state.nav[2]} onClick={this.handleClick} className="tabTitle">Strategy</Button>
        <Button type="credentials" disabled={this.state.nav[3]} onClick={this.handleClick}className="tabTitle">Credentials</Button>
        <div><p>{this.state !== null ? "lols" : ""}</p></div>
      </div>
    

    );
  }
}



PortfolioNav.propTypes = {
  currencies: PropTypes.object.isRequired,
  getCurrencies: PropTypes.func.isRequired,
  exchanges: PropTypes.object.isRequired,
  getExchanges: PropTypes.func.isRequired,
}
const mapStateToProps = state => ({
  currencies: state.currencies,
  exchanges: state.exchanges

});
export default connect(mapStateToProps, {getCurrencies, getExchanges})(withRouter(PortfolioNav))