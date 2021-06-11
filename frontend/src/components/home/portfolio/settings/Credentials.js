import React from 'react'
import { connect } from 'react-redux'

export const Credentials = (props) => {
  return (
    <div>
      COMING SOON {props.portfolio}
    </div>
  )
}


const mapStateToProps = (state) => ({
  
})

const mapDispatchToProps = {
  
}

export default connect(mapStateToProps, mapDispatchToProps)(Credentials)
