import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { deletePortfolio, updatePortfolio } from "./PortfoliosActions";
import { Button } from "react-bootstrap";

class portfolio extends Component {
  onDeleteClick = () => {
    const { portfolio } = this.props;
    this.props.deletePortfolio(portfolio.id);
  };
  render() {
    const { portfolio } = this.props;
    return (
      <div>
        <hr />
        <p>{portfolio.name} | {portfolio.description}</p>
        <Button variant="danger" size="sm" onClick={this.onDeleteClick}>
          Delete
        </Button>

      </div>
    );
  }
}

portfolio.propTypes = {
  portfolio: PropTypes.object.isRequired
};
const mapStateToProps = state => ({});

export default connect(mapStateToProps, { deletePortfolio, updatePortfolio })(
  withRouter(portfolio)
);
