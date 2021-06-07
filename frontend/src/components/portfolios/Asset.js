import React from 'react'
import { connect } from 'react-redux'

export const Asset = (props) => {
  const asset = props.asset
  return (
    <div>
    <b>{asset.symbol}</b> {asset.name}
    <p>Value: {asset.value} $</p>
    <p>Status: {asset.status}</p>
    </div>
    
  )
}

const mapStateToProps = (state) => ({
  
})

const mapDispatchToProps = {
  
}

export default connect(mapStateToProps, mapDispatchToProps)(Asset)
