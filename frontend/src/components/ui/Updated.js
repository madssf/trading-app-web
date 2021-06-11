import React, { Component } from 'react';

import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { Container} from "react-bootstrap";
import {getCurrencies} from '../store/CurrenciesActions'
import moment from 'moment';


class Updated extends Component {
  componentDidMount() {
    this.props.getCurrencies();
  }


 
  render() {
    const {currencies} = this.props.currencies
    if (currencies.length === 0){
      return <p>-</p>
    }
    
    let items = currencies.map(currency => {return moment(currency.modified)})
    let updated = moment("2006-07-05")
    for(var i = 0; i < items.length; i++) {
        if (items[i].isAfter(updated)) {
          updated = items[i]
        } 
    }
  

    return (
          <div> 
          <p className="updatedText">{updated.format("hh:mm:ss")}</p>
          </div> 

     
  );
}
}

Updated.propTypes = {
  currencies: PropTypes.object.isRequired,
  getCurrencies: PropTypes.func.isRequired,
};

const mapStateToProps = state => ({
  currencies: state.currencies,
});

export default connect(mapStateToProps, {getCurrencies})(withRouter(Updated));