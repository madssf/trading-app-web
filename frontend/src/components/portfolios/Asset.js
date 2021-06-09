import React from 'react'

const Asset = (props) => {
  const value = props.value
  let exchange = props.exchange
  const status = props.status
  /*
  for(var i = 0; i < props.exchanges.exchanges.length ; i++){
    if (props.exchanges.exchanges[i].id === exchange) {
      exchange = props.exchanges.exchanges[i].name
    } 
  }
  */
  return (
      <div className="tinyText">
     {value} | {status} | {exchange}

      </div>
      
    )
   
  
}
export default Asset

