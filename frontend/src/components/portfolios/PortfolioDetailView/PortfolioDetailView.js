import React, { Component } from 'react'
import { connect } from 'react-redux'

export class PortfolioDetailView extends Component {

  
  render() {

    


    return (
      <div>
        <p> Graphs </p>
      </div>
    )
  }
}

const mapStateToProps = (state) => ({
  
})

const mapDispatchToProps = {
  
}

export default connect(mapStateToProps, mapDispatchToProps)(PortfolioDetailView)
