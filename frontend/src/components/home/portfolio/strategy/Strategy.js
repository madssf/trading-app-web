import React from 'react'
import {Button} from 'react-bootstrap'
import StrategyParameter from './StrategyParameter'
export default function Strategy(props) {



  

    let params = props.data.strategy.parameters.map(param => {
      return <StrategyParameter key={param.strat_param_id} portfolio={props.data} data={param}/>
    })
    return (
        <div className="strategy">
          
          <h2>{props.data.strategy.name}</h2>
          <Button className="action ">Change</Button>

          <div className="strategyBtns">
          <Button className="action">Execute</Button>
          <Button className="action">Schedule</Button>
          </div>

          <p>Difference bar chart</p>
          <p>Balanced portfolio chart</p>
          <p>Trading instructions</p>



       
          {params}

       
        </div>

      )
  }

  
  


    