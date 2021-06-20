import React from 'react'
import CurrencyAsset from './CurrencyAsset.js'

import sortBy from '../../../../utils/SortBy'
import PieChart from '../graphs/PieChart.js'


export default function Assets(props) {

    if (props.assets.length === 0) {
      return <div style={{margin: "20px"}}>Please add your first asset, or register credentials to fetch balances automatically.</div>
    }


    let totals = [{'id':props.assets[0].id, 'value': props.assets[0].value, 'symbol': props.assets[0].symbol, 'positions': [props.assets[0]]}]

    let totalsSymbols = [props.assets[0].symbol]
    for(var i = 1; i < props.assets.length ; i++){
      if (!(totalsSymbols.includes(props.assets[i].symbol))) {
          totals.push({'id':props.assets[i].id, 'value': props.assets[i].value, 'symbol': props.assets[i].symbol, 'positions': [props.assets[i]]})
          totalsSymbols.push(props.assets[i].symbol)
          
        } else {
          let j = 0
          while (j < totals.length) {
            if (props.assets[i].symbol === totals[j].symbol) {
            totals[j].value = totals[j].value + props.assets[i].value
            totals[j].positions.push(props.assets[i])

            }
          j++
          }
        }
    }

    totals = totals.sort(sortBy("value", false))
    const currencyTotals = totals.map(coin => {return <CurrencyAsset key ={coin.id} symbol={coin.symbol} value={coin.value} positions={coin.positions}/>})

      
    return (
        <div className="assets">
          <PieChart labels={totals.map(coin => coin.symbol)} data={totals.map(coin => coin.value)}/>
          {currencyTotals}    


        </div>
      )

  }


  


    