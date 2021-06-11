import React, { Component } from 'react'
import { connect } from 'react-redux'

import Credentials from './Credentials'

export class Settings extends Component {
  render() {
    return (
      <div>
        <Credentials/>
      </div>
    )
  }
}

const mapStateToProps = (state) => ({
  
})

const mapDispatchToProps = {
  
}

export default connect(mapStateToProps, mapDispatchToProps)(Settings)
