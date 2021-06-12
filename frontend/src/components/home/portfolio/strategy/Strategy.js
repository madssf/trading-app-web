import React, { Component } from 'react'
import { connect } from 'react-redux'
import {Button} from 'react-bootstrap'

export class Strategy extends Component {
  render() {
    return (
      <div>
        <Button className="action">Simulate</Button>
        <Button className="action">Execute</Button>

      </div>
    )
  }
}

const mapStateToProps = (state) => ({
  
})

const mapDispatchToProps = {
  
}

export default connect(mapStateToProps, mapDispatchToProps)(Strategy)
