import React from 'react'
import {Button} from 'react-bootstrap'
import DiffChart from '../../../charts/DiffChart'
import PieChart from '../../../charts/PieChart'
import Instruction from './Instruction'
import StrategyParameter from './StrategyParameter'
export default function Strategy(props) {

    

    const diff_matrix = props.data.strategy.diff_matrix
    if  (!(diff_matrix !== undefined)) {
      return <div></div>
    }
    const diff_keys = Object.keys(diff_matrix)
    const diff_data = Object.values(diff_matrix).map(coin => coin.fiat)

    const balanced = props.data.strategy.balanced_portfolio
    const bal_keys = Object.keys(balanced)
    const bal_data = Object.values(balanced).map(coin => coin.pct)
    
    let params = props.data.strategy.parameters.map(param => {
      return <StrategyParameter key={param.strat_param_id} portfolio={props.data} data={param}/>
    })

    let instructions = props.data.strategy.instructions.map(instr => {
      return <Instruction data={instr}/>
    })
    return (
        <div className="strategy">
          <div className="strategyGrid">
          <Button className="action sg1">Change</Button>

          <h2 className="stratName sg2">{props.data.strategy.name}</h2>

          <div className="strategyBtns sg3">
          <Button className="action">Execute</Button>
          <Button className="action">Schedule</Button>
          </div>
          </div>
          <h4>diff matrix</h4>
          <DiffChart labels={diff_keys} data={diff_data}/>

          <h4>balanced portfolio</h4>
          <PieChart labels={bal_keys}  data = {bal_data}/>

          <h2>Trading instructions</h2>
          {instructions}


          <h2>Input parameters</h2>

       
          {params}

       
        </div>

      )
  }

  
  


    