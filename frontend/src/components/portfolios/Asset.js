import React from 'react'

const Asset = (props) => {
  const value = props.asset.value
  const amount = Math.round(props.asset.amount *10000)/10000

  let exchange = props.asset.exchange
  const status = props.asset.status
  /*
  for(var i = 0; i < props.exchanges.exchanges.length ; i++){
    if (props.exchanges.exchanges[i].id === exchange) {
      exchange = props.exchanges.exchanges[i].name
    } 
  }
  */
  return (
      <div className="tinyText">
     {value} | {amount} | {status} | {exchange}

      </div>
      
    )
   
  
}
export default Asset

