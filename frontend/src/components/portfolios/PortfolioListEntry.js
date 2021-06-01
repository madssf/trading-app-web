import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { deletePortfolio, updatePortfolio } from "./PortfoliosActions";
import { Button } from "react-bootstrap";

class PortfolioListEntry extends Component {
  onDeleteClick = () => {
    const { portfolio } = this.props;
    this.props.deletePortfolio(portfolio.id);
  };
  render() {
    const { portfolio } = this.props;
    return (
      <div>
        <hr />
        <p>{portfolio.name}</p>
        <p>{portfolio.description}</p>
      </div>
    );
  }
}

PortfolioListEntry.propTypes = {
  portfolio: PropTypes.object.isRequired
};
const mapStateToProps = state => ({});

export default connect(mapStateToProps, { deletePortfolio, updatePortfolio })(
  withRouter(PortfolioListEntry)
);
