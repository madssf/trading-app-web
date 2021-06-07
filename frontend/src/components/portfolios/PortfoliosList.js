import React, { Component } from 'react';

import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";

import { Container} from "react-bootstrap";
import {getPortfolios} from './PortfoliosActions'
import PortfolioListEntry from './PortfolioListEntry'


class PortfoliosList extends Component {
  componentDidMount() {
    this.props.getPortfolios();
  }

 
  render() {
    const {portfolios} = this.props.portfolios
    if (portfolios.length === 0){
      return <p>No portfolios yet.</p>
    }
    let items = portfolios.map(portfolio => {
      return <PortfolioListEntry key={portfolio.id} portfolio={portfolio}/>;
    })
    return (
          <Container>
          <div> 
          <h1>Portfolios</h1>
          <p>Displaying {portfolios.length} portfolios</p>
          {items}
          </div> 
          </Container>

     
  );
}
}

PortfoliosList.propTypes = {
  portfolios: PropTypes.object.isRequired,
  getPortfolios: PropTypes.func.isRequired,
};

const mapStateToProps = state => ({
  portfolios: state.portfolios,
});

export default connect(mapStateToProps, {getPortfolios})(withRouter(PortfoliosList));
