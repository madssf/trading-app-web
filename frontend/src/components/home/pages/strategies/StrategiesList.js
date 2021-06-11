import React, { Component } from 'react';

import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { Container} from "react-bootstrap";
import {getStrategies} from '../../../store/StrategiesActions'
import Strategy from './Strategy'


class StrategiesList extends Component {
  componentDidMount() {
    this.props.getStrategies();
  }

 
  render() {
    const {strategies} = this.props.strategies
    if (strategies.length === 0){
      return <p>No currencies yet.</p>
    }
    let items = strategies.map(strategy => {     
      return <Strategy key={strategy.id} strategy={strategy}/>;
    })
    return (
          <Container>
          <div> 
          <h1>Strategies</h1>
          {items}
          </div> 
          </Container>

     
  );
}
}

StrategiesList.propTypes = {
  strategies: PropTypes.object.isRequired,
  getStrategies: PropTypes.func.isRequired,
};

const mapStateToProps = state => ({
  strategies: state.strategies,
});

export default connect(mapStateToProps, {getStrategies})(withRouter(StrategiesList));
