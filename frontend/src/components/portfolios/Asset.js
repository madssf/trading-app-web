import React, { Component } from 'react'
import { toastOnError } from "../../utils/Utils";
import axios from 'axios';
import PropTypes from "prop-types";

import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import {getExchanges} from '../exchanges/ExchangesActions'
import { Container } from 'react-bootstrap';


class Asset extends Component {
  constructor(props) {
    super(props);
    this.state = {
      name: "",
    };
  }

  
  componentDidMount() {
    this.props.getExchanges();

    const exchanges = this.props.exchanges.exchanges
    for (var i = 0; i < exchanges.length; i++){
      console.log(this.props.asset.exchange)
      console.log(exchanges[i].id)

      if (this.props.asset.exchange === exchanges[i].id) {
        this.setState({name: exchanges[i].name})
        console.log('lels')
      }
    }
   
  }
  
  render() {
    
    


    return (
      <Container>
      <div className="asset">
      <p className="assetText">
     {this.props.asset.value}  
     {this.state.name !== "" ? this.state.name : "uknown"}
    
     </p>
      </div>
      </Container>
      
    
    )
  }
}

Asset.propTypes = {
  exchanges: PropTypes.object.isRequired,
  getExchanges: PropTypes.func.isRequired,
}
const mapStateToProps = state => ({
  exchanges: state.exchanges

});
export default connect(mapStateToProps, {getExchanges})(withRouter(Asset))