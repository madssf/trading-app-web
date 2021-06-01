import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { getPortfolios } from "./PortfoliosActions";

import PortfolioListEntry from "./PortfolioListEntry";
import axios from "axios";

class PortfoliosList extends Component {
  componentDidMount() {
    this.props.getPortfolios();
  }

  render() {
    const { portfolios } = this.props.portfolios;

    if (portfolios.length === 0) {
      return <p>No portfolios yet, but you can add one.</p>;
    }

    let items = portfolios.map(portfolio => {
      return <PortfolioListEntry key={portfolio.id} portfolio={portfolio} />;
    });

    return (
      <div>
        <h2>portfolios</h2>
        {items}
        <hr />
      </div>
    );
  }


}

PortfoliosList.propTypes = {
  getPortfolios: PropTypes.func.isRequired,
  portfolios: PropTypes.object.isRequired
};

const mapStateToProps = state => ({
  portfolios: state.portfolios
});

export default connect(mapStateToProps, {
  getPortfolios
})(withRouter(PortfoliosList));