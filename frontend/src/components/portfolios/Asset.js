import React from 'react'
import { connect } from 'react-redux'

export const Asset = (props) => {
  const asset = props.asset
  return (
    <div>
    <b>{asset.symbol}</b> {asset.name} {asset.status}: {asset.value} $
    </div>
    
  )
}

const mapStateToProps = (state) => ({
  
})

const mapDispatchToProps = {
  
}

export default connect(mapStateToProps, mapDispatchToProps)(Asset)
