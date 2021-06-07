import React, { Component } from 'react';

import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { Container} from "react-bootstrap";
import {getCurrencies} from './CurrenciesActions'
import Currency from './Currency'


class CurrenciesList extends Component {
  componentDidMount() {
    this.props.getCurrencies();
  }

 
  render() {
    const {currencies} = this.props.currencies
    if (currencies.length === 0){
      return <p>No currencies yet.</p>
    }
    let items = currencies.map(currency => {
      return <Currency key={currency.id} currency={currency}/>;
    })
    return (
          <Container>
          <div> 
          <h1>Currencies</h1>
          <p>Displaying {currencies.length} currencies</p>
          {items}
          </div> 
          </Container>

     
  );
}
}

CurrenciesList.propTypes = {
  currencies: PropTypes.object.isRequired,
  getCurrencies: PropTypes.func.isRequired,
};

const mapStateToProps = state => ({
  currencies: state.currencies,
});

export default connect(mapStateToProps, {getCurrencies})(withRouter(CurrenciesList));
