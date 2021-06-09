import React from 'react'

const Asset = (props) => {
  if (props.asset !== undefined && props.exchanges !== undefined){
  const asset = props.asset
  let exchange = "Unknown"
  for(var i = 0; i < props.exchanges.exchanges.length ; i++){
    if (props.exchanges.exchanges[i].id === asset.exchange) {
      exchange = props.exchanges.exchanges[i].name
    }
  }
    return (
      <div>
      <b>{asset.symbol}</b> 
      <p>{asset.name}</p>
      <p>{exchange}</p>
  
      <p>{asset.status}</p>
      <p>{asset.value} $</p>
      </div>
      
    )
  } else {
    return <p>'No assets'</p>
  }
  
}
export default Asset

