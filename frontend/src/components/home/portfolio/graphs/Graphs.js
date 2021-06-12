import React from 'react'
import { connect } from 'react-redux'

export const PortfolioGraphs = (props) => {
  return (
    <div>
      <p>Performance vs index line chart</p>
      <p>Total value historic chart</p>

    </div>
  )
}

const mapStateToProps = (state) => ({
  
})

const mapDispatchToProps = {
  
}

export default connect(mapStateToProps, mapDispatchToProps)(PortfolioGraphs)
