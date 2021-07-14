import React from 'react'
import Asset from './Asset.js'

import sortBy from '../../../../utils/SortBy'
import PieChart from '../graphs/PieChart.js'


export default function Assets(props) {

    if (props.assets === undefined) {
      return <div style={{margin: "20px"}}>Please add your first asset, or register credentials to fetch balances automatically.</div>
    }


    let assets = props.assets
    for(var i = 0; i < props.assets.length ; i++){
      if (assets[i].positions.length > 1) {
        assets[i].total = assets[i].positions.reduce((a, b) => a.value + b.value)
      } else {
        assets[i].total = assets[i].positions[0].value
      } 
    }
    
    assets = assets.sort(sortBy("total", false))
    const assetComponents = assets.map(asset => {return <Asset key={asset.id} total={asset.total} data={asset} />})

          
      
    return (
        <div className="assets">
          <PieChart labels={assets.map(asset => asset.symbol)} data={assets.map(asset => asset.total)}/>
    
          {assetComponents}    


        </div>
      )

  }


  


    