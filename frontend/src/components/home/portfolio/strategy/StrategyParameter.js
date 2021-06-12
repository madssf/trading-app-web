import React from 'react'

export default function StrategyParameter(props) {

 
    console.log(props)

    return (
        <div className="strategyParameter">
          
          <p>{props.data.name}</p>
          <p>{props.data.value}</p>
          <p>{props.data.type}</p>
          <p>{props.data.description}</p>


        </div>
      )

  }

  
  


    