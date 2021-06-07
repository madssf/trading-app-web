import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter, Link, StaticRouter } from "react-router-dom";

export const PortfolioListEntry = (props) => {
  const portfolio = props.portfolio
  return (
    <div>
    <Link to= {`/portfolios/${portfolio.id}`} >{portfolio.name}</Link>
    </div>
    
  )
}

const mapStateToProps = (state) => ({
  portfolio: state.portfolio
})

const mapDispatchToProps = {
  
}

export default connect(mapStateToProps, mapDispatchToProps)(PortfolioListEntry)
