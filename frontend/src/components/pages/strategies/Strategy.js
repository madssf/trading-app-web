import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";

class Strategy extends Component {
  render() {
    const { strategy } = this.props;
    return (
      <div>
        <hr />
        <p className="strat">
        <b>{strategy.name}</b> 
        <p className="stratDescText"> {strategy.description}</p>
        </p>
      </div>
    );
  }
}

Strategy.propTypes = {
  strategy: PropTypes.object.isRequired
};
const mapStateToProps = state => ({});

export default connect(mapStateToProps)(
  withRouter(Strategy)
);