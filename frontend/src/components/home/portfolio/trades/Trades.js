import React from 'react'
import { connect } from 'react-redux'
import AddTrade from './AddTrade'
import AddDeposit from './AddDeposit'

export const Trades = (props) => {
  return (
    <div>
      <AddTrade portfolio={props.portfolio.id} exchanges={props.exchanges} currencies={props.currencies} />
      <AddDeposit portfolio={props.portfolio.id} exchanges={props.exchanges} currencies={props.currencies}/>
    </div>
  )
}

const mapStateToProps = (state) => ({
  
})

const mapDispatchToProps = {
  
}

export default connect(mapStateToProps, mapDispatchToProps)(Trades)
