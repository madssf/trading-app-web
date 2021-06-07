import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";

class Portfolio extends Component {
  render() {
    const { portfolio } = this.props;
    return (
      <div>
        <hr />
        <p>
        <b>{portfolio.name}</b>: {portfolio.description}
        </p>
      </div>
    );
  }
}

Portfolio.propTypes = {
  portfolio: PropTypes.object.isRequired
};
const mapStateToProps = state => ({});

export default connect(mapStateToProps)(
  withRouter(Portfolio)
);