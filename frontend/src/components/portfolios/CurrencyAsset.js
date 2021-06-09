import React from 'react'

export const CurrencyAsset = (props) => {
  const symbol = props.symbol
  const value = props.value
  return (
    <div>
    <b>{symbol}</b> {value} $
    </div>
    
  )
}

export default CurrencyAsset
