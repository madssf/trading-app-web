import React, { Component } from 'react'
import { connect } from 'react-redux'

export class PortfolioDetailView extends Component {

  
  render() {

    let sum = 0
    
    for(var i = 0; i<this.props.portfolio.assets.length; i++){
      sum += this.props.portfolio.assets[i].value
    }
    sum = Math.round(sum*100)/100


    return (
      <div>
       <p className="sumText"> {sum} $ </p>
        <p> Cool graphs here </p>
      </div>
    )
  }
}

const mapStateToProps = (state) => ({
  
})

const mapDispatchToProps = {
  
}

export default connect(mapStateToProps, mapDispatchToProps)(PortfolioDetailView)
