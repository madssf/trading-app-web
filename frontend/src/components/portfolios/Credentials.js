import React from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'

export const Credentials = (props) => {
  return (
    <div>
      {props.portfolio}
    </div>
  )
}


const mapStateToProps = (state) => ({
  
})

const mapDispatchToProps = {
  
}

export default connect(mapStateToProps, mapDispatchToProps)(Credentials)
