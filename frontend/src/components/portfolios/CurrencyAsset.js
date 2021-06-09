import React from 'react'
import Asset from './Asset'
export const CurrencyAsset = (props) => {
  const symbol = props.symbol
  const value = props.value

  const positions = props.positions.map(asset => {return <Asset key={asset.id+asset.status+asset.exchange} symbol={props.symbol} value={asset.value} exchange={asset.exchange} status={asset.status}/>})
    
  return (
    <div>

    <b>{symbol}</b> {value} $     
    {props.positions !== undefined ? positions : []}

    </div>
    
  )
}

export default CurrencyAsset
