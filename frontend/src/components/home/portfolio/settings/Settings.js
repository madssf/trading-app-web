import React, { Component } from 'react'
import {Button} from 'react-bootstrap'
import { connect } from 'react-redux'

import Credentials from './Credentials'

export class Settings extends Component {
  render() {
    return (
      <div>
        {this.props !== undefined ? 
        <Credentials portfolio={this.props}/>
        : "No portfolio"}

      <Button>Notification settings</Button>
      </div>
    )
  }
}

const mapStateToProps = (state) => ({
  
})

const mapDispatchToProps = {
  
}

export default connect(mapStateToProps, mapDispatchToProps)(Settings)
