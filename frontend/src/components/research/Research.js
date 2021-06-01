import React, { Component } from 'react';

import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { Container} from "react-bootstrap";



import Sidebar from '../Sidebar';

class Research extends Component {

  render() {
    const { user } = this.props.auth;
    return (
      <div>
        <Sidebar />
        <Container>
          <div className='home'> 
          <h1>Research</h1>
          <p>{user.username}</p>
          </div>        
      </Container>
  
    </div>

     
  );
}
}

Research.propTypes = {
  logout: PropTypes.func.isRequired,
  auth: PropTypes.object.isRequired
};

const mapStateToProps = state => ({
  auth: state.auth
});

export default connect(mapStateToProps, {
})(withRouter(Research));
