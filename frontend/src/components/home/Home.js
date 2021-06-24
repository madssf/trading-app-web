import React, { Component } from 'react';

import PropTypes from "prop-types";
import { connect } from "react-redux";
import { Link, withRouter } from "react-router-dom";
import { Container} from "react-bootstrap";
import PortfoliosList from './PortfoliosList';
import AddPortfolio from './AddPortfolio';


class Home extends Component {


 
  render() {
    const { user } = this.props.auth;
    
    return (
          <Container>
          <div className='home'> 
          <h1>Home</h1>
          <p>Welcome, {user.username}</p>
          <p>Email: {user.email}</p>
          </div> 

          
          <PortfoliosList/>
          <AddPortfolio />
          <ul>
            <li><Link to="/currencies">Currencies</Link></li>
            <li><Link to="/strategies">Strategies</Link></li>

          </ul>
          </Container>

     
  );
}
}

Home.propTypes = {
  auth: PropTypes.object.isRequired,
};

const mapStateToProps = state => ({
  auth: state.auth,
});

export default connect(mapStateToProps)(withRouter(Home));
