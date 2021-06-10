import React, { Component } from 'react'
import { connect } from 'react-redux'

export class Strategy extends Component {
  render() {
    return (
      <div>
        <h3>Strategy</h3>
      </div>
    )
  }
}

const mapStateToProps = (state) => ({
  
})

const mapDispatchToProps = {
  
}

export default connect(mapStateToProps, mapDispatchToProps)(Strategy)
