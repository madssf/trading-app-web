import React from 'react'
import {Button} from 'react-bootstrap'
import { connect } from 'react-redux'

export const Credentials = (props) => {
  console.log(props)
  return (
    <div>
      <Button>Edit credentials</Button>
    </div>
  )
}


const mapStateToProps = (state) => ({
  
})

const mapDispatchToProps = {
  
}

export default connect(mapStateToProps, mapDispatchToProps)(Credentials)
