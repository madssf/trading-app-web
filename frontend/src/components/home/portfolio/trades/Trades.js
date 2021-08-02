import React from 'react'
import { connect } from 'react-redux'
import AddTrade from './AddTrade'
import AddDeposit from './AddDeposit'
import DepositList from './DepositList'

export const Trades = (props) => {
  console.log()
  return (
    <div>
      <AddTrade portfolio={props.portfolio.id} exchanges={props.exchanges} currencies={props.currencies} />
      <AddDeposit portfolio={props.portfolio.id} exchanges={props.exchanges} currencies={props.currencies}/>
      <DepositList deposits={props.portfolio.deposits} />
    </div>
  )
}

const mapStateToProps = (state) => ({
  
})

const mapDispatchToProps = {
  
}

export default connect(mapStateToProps, mapDispatchToProps)(Trades)
