import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";

class Currency extends Component {
  render() {
    const { currency } = this.props;
    return (
      <div>
        <hr />
        <p>
        <b>{currency.symbol}</b>: {currency.name} :  {currency.mcap_rank} : <b>{currency.last_price}</b> | {currency.pct_change_24h}
        </p>
      </div>
    );
  }
}

Currency.propTypes = {
  currency: PropTypes.object.isRequired
};
const mapStateToProps = state => ({});

export default connect(mapStateToProps)(
  withRouter(Currency)
);