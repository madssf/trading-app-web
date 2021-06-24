
import React from 'react'
import { connect } from 'react-redux'
import { Button } from 'react-bootstrap'

const handleChange = () => {
  console.log("handling change")
}

export const AddPortfolio = (props) => {
  return (
    <div>
        <input className="portfolioNameInput" type="text" name="portfolioName" placeholder="Name your portfolio..." onChange={handleChange} />
      <Button>
        Add Portfolio
      </Button>
    </div>
  )
}

const mapStateToProps = (state) => ({



  
})

const mapDispatchToProps = {
  
}

export default connect(mapStateToProps, mapDispatchToProps)(AddPortfolio)
