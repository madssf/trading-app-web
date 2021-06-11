import React, {Component } from 'react';

import PropTypes from "prop-types";
import { connect } from "react-redux";
import { Link, withRouter } from "react-router-dom";
import { Container} from "react-bootstrap";
import PortfoliosList from './PortfoliosList';
import './style.css'


class Home extends Component {


 
  render() {
    const { user } = this.props.auth;
    
    return (
          <Container>
          <div className='home'> 
          <h1>Home</h1>
          <p className="username">user: <b>{user.username}</b></p>
          <p className="email">email: <b>{user.email}</b></p>

          </div> 
          <h2>Portfolios</h2>
          <PortfoliosList/>
          <h3>Explore</h3>
          <ul>
          <li><Link to="/currencies/">Currencies</Link></li>
          <li><Link to="/strategies/">Strategies</Link></li>
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
