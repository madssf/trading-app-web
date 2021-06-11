import React, { Component } from 'react'
import { connect } from 'react-redux'

export class PortfolioNav extends Component {


  render() {
    return (
      <div className="portfolioNav">
        <h2 className="portfolioNavTitle pfNav1">Assets</h2>
        <h2 className="portfolioNavTitle pfNav2">Graphs</h2>
        <h2 className="portfolioNavTitle pfNav3">Strategy</h2>
        <h2 className="portfolioNavTitle pfNav4">Settings</h2>
      </div>
    )
  }
}

const mapStateToProps = (state) => ({
  
})

const mapDispatchToProps = {
  
}

export default connect(mapStateToProps, mapDispatchToProps)(PortfolioNav)
